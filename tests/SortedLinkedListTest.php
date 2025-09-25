<?php

declare(strict_types=1);

namespace Jtx\SortedLinkedList\Tests;

use InvalidArgumentException;
use Jtx\SortedLinkedList\Exceptions\TypeMismatchException;
use Jtx\SortedLinkedList\SortedLinkedList;
use PHPUnit\Framework\TestCase;

class SortedLinkedListTest extends TestCase
{
    private SortedLinkedList $list;

    protected function setUp(): void
    {
        $this->list = new SortedLinkedList();
    }

    /**
     * Just checking that a new list starts empty like it should
     */
    public function testBasicFunctionality(): void
    {
        $this->assertTrue($this->list->isEmpty());
        $this->assertEquals(0, $this->list->count());
    }

    /**
     * Make sure when we add numbers they get sorted automatically
     */
    public function testAddingNumbers(): void
    {
        $this->list->addValue(5);
        $this->list->addValue(2);
        $this->list->addValue(8);
        $result = $this->list->toArray();
        $this->assertEquals([2, 5, 8], $result);
        $this->assertEquals(3, $this->list->count());
    }

    /**
     * Same thing but with strings - should sort alphabetically
     */
    public function testStrings(): void
    {
        $this->list->addValue('books');
        $this->list->addValue('apes');
        $this->assertEquals(['apes', 'books'], $this->list->toArray());
        $this->assertTrue($this->list->hasValue('apes'));
        $this->assertFalse($this->list->hasValue('kristy'));
    }

    /**
     * Test that we can remove items and it returns true/false correctly
     */
    public function testRemoval(): void
    {
        $this->list->addValue(10);
        $this->list->addValue(20);
        $this->list->addValue(15);
        $removed = $this->list->removeValue(15);
        $this->assertTrue($removed);
        $this->assertEquals([10, 20], $this->list->toArray());
        $notRemoved = $this->list->removeValue(99);
        $this->assertFalse($notRemoved);
    }

    /**
     * Should be able to get items by their position in the sorted list
     */
    public function testGetByIndex(): void
    {
        $this->list->addValue(100);
        $this->list->addValue(50);
        $this->assertEquals(50, $this->list->getValue(0));
        $this->assertEquals(100, $this->list->getValue(1));
    }

    /**
     * Don't let people mix strings and numbers
     */
    public function testTypeChecking(): void
    {
        $this->list->addValue(42);
        $this->expectException(TypeMismatchException::class);
        $this->list->addValue('not a number');
    }

    /**
     * Clear the array
     */
    public function testClear(): void
    {
        $this->list->addValue(1);
        $this->list->addValue(2);
        $this->assertFalse($this->list->isEmpty());
        $this->list->clearAll();
        $this->assertTrue($this->list->isEmpty());
    }

    /**
     * Make sure we can loop through the list with foreach
     */
    public function testIteration(): void
    {
        $nums = [3, 1, 5];
        foreach ($nums as $n) {
            $this->list->addValue($n);
        }
        $collected = [];
        foreach ($this->list as $value) {
            $collected[] = $value;
        }
        $this->assertEquals([1, 3, 5], $collected);
    }

    /**
     * If someone adds the same value twice, keep both copies
     */
    public function testDuplicateValues(): void
    {
        $this->list->addValue(7);
        $this->list->addValue(3);
        $this->list->addValue(7);
        $this->list->addValue(1);
        $this->assertEquals([1, 3, 7, 7], $this->list->toArray());
    }

    /**
     * Asking for an index that doesn't exist should blow up
     */
    public function testInvalidIndex(): void
    {
        $this->list->addValue(123);
        $this->expectException(InvalidArgumentException::class);
        $this->list->getValue(10);
    }

    /**
     * Negative numbers should work fine too - maybe. The test said int, so .... negatives are still int's
     */
    public function testNegatives(): void
    {
        $this->list->addValue(-5);
        $this->list->addValue(10);
        $this->list->addValue(-2);
        $this->assertEquals([-5, -2, 10], $this->list->toArray());
    }

    /**
     * Test strings to be sorted automatically
     */
    public function testStringSorting(): void
    {
        // Add strings in random order
        $this->list->addValue('kristy');
        $this->list->addValue('jimmy');
        $this->list->addValue('anna');
        $this->list->addValue('pam');
        $this->list->addValue('puppy');
        
        // Should be automatically sorted alphabetically
        $expected = ['anna', 'jimmy', 'kristy', 'pam', 'puppy'];
        $this->assertEquals($expected, $this->list->toArray());
        $this->assertEquals(5, $this->list->count());
    }
}
