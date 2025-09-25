# SortedLinkedList

“Implement a library providing SortedLinkedList
(linked list that keeps values sorted). It should be
able to hold string or int values, but not both. Try to
think about what you'd expect from such library as a
user in terms of usability and best practices, and
apply those.
”

This is a simple PHP class that keeps a list of numbers or strings in sorted order. When you add something to it, it automatically puts it in the right place.

You can either put all numbers or all strings in the list, but not both at the same time.

### This has apparently been solved already with the SplDoublyLinkedList class introduced in php 5! This is just an implementation of it that auto sorts.

## What you need

PHP 8.1 or newer.

## How to install

Run `composer install`. Make sure php 8.1 is installed along with composer.

## How to use it

Here's a basic example with numbers:

```php

<?php

use Jtx\SortedLinkedList\SortedLinkedList;

$list = new SortedLinkedList();

$list->addValue(1);
$list->addValue(2);
$list->addValue(3);
$list->addValue(4);

// This will give you [1, 2, 3, 4]
$sorted = $list->toArray();

// Check if something is in there
if ($list->hasValue(4)) {
    echo "Found it!";
}

// Remove something
$list->removeValue(2);

// Get the first item
$first = $list->getValue(0);
```

It works the same way with strings:

```php
$words = new SortedLinkedList();
$words->addValue('jimmy');
$words->addValue('kristy'); 
$words->addValue('mom');

$sorted = $words->toArray();
```

## Type checking

The list won't let you mix numbers and strings:

```php
$list = new SortedLinkedList();
$list->addValue(42);

// This will throw an TypeMismatchException
$list->addValue('Heyooo!');
```

## What methods can you use

These are all basic values from the base class SplDoublyLinkedList - Just making an adapter basically.

`addValue($value)` - Add to the array

`removeValue($value)` - Remove from the array. Returns bool if we find the key and dump it

`hasValue($value)` - return bool if key exists or not

`getValue($index)` - grab the value of the index

`toArray()` - Return the array

`count()` - Count of the keys in the. array

`isEmpty()` - Return bool true / false

`clearAll()` - just go $array = [] basically, empty the array
