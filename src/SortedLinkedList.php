<?php

declare(strict_types=1);

namespace Jtx\SortedLinkedList;

use InvalidArgumentException;
use SplDoublyLinkedList;
use Iterator;
use Countable;
use Jtx\SortedLinkedList\Exceptions\TypeMismatchException;

/**
 * @implements Iterator<int, string|int>
 */
class SortedLinkedList implements Iterator, Countable
{
    /** @var SplDoublyLinkedList<string|int> */
    private SplDoublyLinkedList $items;
    private ?string $valueType = null;

    public function __construct()
    {
        $this->items = new SplDoublyLinkedList();
        $this->items->setIteratorMode(SplDoublyLinkedList::IT_MODE_FIFO);
    }

    /**
     * @param string|int $value
     *
     * @return void
     */
    public function addValue(string|int $value): void
    {
        $this->checkType($value);

        if ($this->items->isEmpty()) {
            $this->items->push($value);
            return;
        }

        $pos = $this->getInsertPos($value);
        $this->insertAt($value, $pos);
    }

    /**
     * @param string|int $value
     *
     * @return bool
     */
    public function removeValue(string|int $value): bool
    {
        if ($this->valueType === null || $this->items->isEmpty()) {
            return false;
        }

        $this->checkType($value);

        $pos = $this->findPos($value);
        if ($pos === -1) {
            return false;
        }

        $this->removeAt($pos);

        return true;
    }

    /**
     * @param string|int $value
     *
     * @return bool
     */
    public function hasValue(string|int $value): bool
    {
        if ($this->valueType === null || $this->items->isEmpty()) {
            return false;
        }

        $this->checkType($value);

        return $this->findPos($value) !== -1;
    }

    /**
     * @param int $index
     *
     * @return string|int
     */
    public function getValue(int $index): string|int
    {
        if ($index < 0 || $index >= $this->items->count()) {
            throw new InvalidArgumentException("Index out of range: {$index}");
        }

        $this->items->rewind();
        for ($i = 0; $i < $index; $i++) {
            $this->items->next();
        }

        return $this->items->current();
    }

    /**
     * @return array<int, string|int>
     */
    public function toArray(): array
    {
        $result = [];
        $this->items->rewind();

        while ($this->items->valid()) {
            $result[] = $this->items->current();
            $this->items->next();
        }

        return $result;
    }

    /**
     * @return void
     */
    public function clearAll(): void
    {
        $this->items = new SplDoublyLinkedList();
        $this->items->setIteratorMode(SplDoublyLinkedList::IT_MODE_FIFO);
        $this->valueType = null;
    }

    /**
     * @return bool
     */
    public function isEmpty(): bool
    {
        return $this->items->isEmpty();
    }

    /**
     * @return int
     */
    public function count(): int
    {
        return $this->items->count();
    }

    /**
     * @return string|int
     */
    public function current(): string|int
    {
        return $this->items->current();
    }

    /**
     * @return int
     */
    public function key(): int
    {
        return $this->items->key();
    }

    /**
     * @return void
     */
    public function next(): void
    {
        $this->items->next();
    }

    /**
     * @return void
     */
    public function rewind(): void
    {
        $this->items->rewind();
    }

    /**
     * @return bool
     */
    public function valid(): bool
    {
        return $this->items->valid();
    }

    /**
     * @param string|int $value
     *
     * @return void
     */
    private function checkType(string|int $value): void
    {
        $currentType = is_string($value) ? 'string' : 'int';

        if ($this->valueType === null) {
            $this->valueType = $currentType;
        } elseif ($this->valueType !== $currentType) {
            throw new TypeMismatchException($currentType, $this->valueType);
        }
    }

    /**
     * @param string|int $value
     *
     * @return int
     */
    private function getInsertPos(string|int $value): int
    {
        $pos = 0;
        $this->items->rewind();

        while ($this->items->valid()) {
            if ($value <= $this->items->current()) {
                break;
            }
            $this->items->next();
            $pos++;
        }

        return $pos;
    }

    /**
     * @param string|int $value
     *
     * @return int
     */
    private function findPos(string|int $value): int
    {
        $pos = 0;
        $this->items->rewind();

        while ($this->items->valid()) {
            if ($this->items->current() === $value) {
                return $pos;
            }
            $this->items->next();
            $pos++;
        }

        return -1;
    }

    /**
     * @param string|int $value
     * @param int        $pos
     *
     * @return void
     */
    private function insertAt(string|int $value, int $pos): void
    {
        if ($pos === 0) {
            $this->items->unshift($value);
        } elseif ($pos >= $this->items->count()) {
            $this->items->push($value);
        } else {
            $newList = new SplDoublyLinkedList();
            $newList->setIteratorMode(SplDoublyLinkedList::IT_MODE_FIFO);
            $this->items->rewind();

            for ($i = 0; $i < $pos; $i++) {
                $newList->push($this->items->current());
                $this->items->next();
            }

            $newList->push($value);

            while ($this->items->valid()) {
                $newList->push($this->items->current());
                $this->items->next();
            }

            $this->items = $newList;
        }
    }

    /**
     * @param int $pos
     *
     * @return void
     */
    private function removeAt(int $pos): void
    {
        if ($pos === 0) {
            $this->items->shift();
        } elseif ($pos === $this->items->count() - 1) {
            $this->items->pop();
        } else {
            $newList = new SplDoublyLinkedList();
            $newList->setIteratorMode(SplDoublyLinkedList::IT_MODE_FIFO);
            $this->items->rewind();

            for ($i = 0; $i < $this->items->count(); $i++) {
                if ($i !== $pos) {
                    $newList->push($this->items->current());
                }
                $this->items->next();
            }

            $this->items = $newList;
        }

        if ($this->items->isEmpty()) {
            $this->valueType = null;
        }
    }
}
