<?php

declare(strict_types=1);

namespace Jtx\SortedLinkedList\Exceptions;

use InvalidArgumentException;

class TypeMismatchException extends InvalidArgumentException
{
    /**
     * @param string $attemptedType
     * @param string $existingType
     */
    public function __construct(string $attemptedType, string $existingType)
    {
        parent::__construct(
            "{$attemptedType} isn't compatible with {$existingType}"
        );
    }
}
