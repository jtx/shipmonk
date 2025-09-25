# SortedLinkedList Library

A Python library providing a SortedLinkedList implementation - a linked list that automatically maintains sorted order for integer or string values (but not both in the same instance).

## Features

- ✅ **Automatic Sorting**: Elements are automatically inserted in sorted order
- ✅ **Type Safety**: Supports either `int` or `str` values, but not both in the same list
- ✅ **Standard Operations**: Insert, remove, search, iteration support
- ✅ **Pythonic Interface**: Supports `len()`, `in` operator, iteration, and string representation
- ✅ **Memory Efficient**: True linked list implementation (not backed by Python list)
- ✅ **Duplicate Handling**: Properly handles duplicate values
- ✅ **Comprehensive Testing**: Full test suite with edge cases

## Quick Start

```python
from sorted_linked_list import SortedLinkedList, create_int_list, create_str_list

# Create lists for specific types
int_list = create_int_list()
str_list = create_str_list()

# Or let the type be inferred from first element
auto_list = SortedLinkedList()

# Insert elements (automatically sorted)
int_list.insert(5)
int_list.insert(2)
int_list.insert(8)
print(int_list)  # SortedLinkedList([2, 5, 8])

# String example
str_list.insert("zebra")
str_list.insert("apple")
str_list.insert("banana")
print(str_list)  # SortedLinkedList(['apple', 'banana', 'zebra'])
```

## API Reference

### Creating Lists

```python
# Generic list (type inferred from first element)
lst = SortedLinkedList()

# Explicitly typed lists
int_list = SortedLinkedList(int)
str_list = SortedLinkedList(str)

# Convenience functions
int_list = create_int_list()
str_list = create_str_list()
```

### Core Methods

```python
# Insert element (maintains sorted order)
lst.insert(value)

# Remove first occurrence of value
success = lst.remove(value)  # Returns True if found and removed

# Check if value exists
exists = lst.contains(value)
exists = value in lst        # Pythonic way

# Get list size
size = len(lst)

# Check if empty
is_empty = lst.is_empty()

# Clear all elements
lst.clear()

# Convert to Python list
python_list = lst.to_list()

# Get the type of elements
element_type = lst.get_type()
```

### Iteration and Display

```python
# Iterate through elements (in sorted order)
for item in lst:
    print(item)

# String representation
print(lst)        # SortedLinkedList([1, 2, 3])
print(repr(lst))  # SortedLinkedList(type=int, elements=[1, 2, 3])
```

## Type Safety

The library enforces type consistency:

```python
lst = SortedLinkedList()
lst.insert(42)          # Type is now 'int'
lst.insert("hello")     # TypeError: Cannot add str to SortedLinkedList of int values
```

## Examples

See `example_usage.py` for comprehensive examples including:
- Integer sorting
- String sorting  
- Type safety demonstrations
- Duplicate value handling

## Running Tests

```bash
python -m unittest test_sorted_linked_list.py -v
```

## Implementation Notes

- Uses a true linked list structure (not a Python list wrapper)
- Insertion is O(n) to maintain sorted order
- Search is O(n) but can terminate early due to sorted nature
- Removal is O(n)
- Memory efficient - only stores the data and next pointers

## Files

- `sorted_linked_list.py` - Main library implementation
- `test_sorted_linked_list.py` - Comprehensive test suite
- `example_usage.py` - Usage examples and demonstrations
