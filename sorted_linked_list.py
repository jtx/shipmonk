"""
SortedLinkedList - A linked list that maintains sorted order.

This library provides a SortedLinkedList implementation that can hold either
string or integer values (but not both in the same instance). The list
automatically maintains sorted order upon insertion.
"""

from typing import Union, Optional, Iterator, TypeVar, Generic
from abc import ABC, abstractmethod


# Type variable for the sorted linked list
T = TypeVar('T', int, str)


class Node(Generic[T]):
    """A node in the sorted linked list."""
    
    def __init__(self, data: T):
        self.data: T = data
        self.next: Optional['Node[T]'] = None


class SortedLinkedList(Generic[T]):
    """
    A linked list that maintains its elements in sorted order.
    
    Can hold either string or integer values, but not both in the same instance.
    Automatically maintains sorted order when elements are inserted.
    """
    
    def __init__(self, data_type: type = None):
        """
        Initialize an empty sorted linked list.
        
        Args:
            data_type: Optional type specification (int or str). If not provided,
                      type will be inferred from the first inserted element.
        """
        self._head: Optional[Node[T]] = None
        self._size: int = 0
        self._data_type: Optional[type] = data_type
        
        # Validate data type if provided
        if data_type is not None and data_type not in (int, str):
            raise ValueError("SortedLinkedList only supports int or str types")
    
    def _validate_type(self, value: T) -> None:
        """Validate that the value matches the expected type."""
        if self._data_type is None:
            # Infer type from first element
            if not isinstance(value, (int, str)):
                raise TypeError("SortedLinkedList only supports int or str values")
            self._data_type = type(value)
        elif not isinstance(value, self._data_type):
            raise TypeError(
                f"Cannot add {type(value).__name__} to a SortedLinkedList "
                f"of {self._data_type.__name__} values"
            )
    
    def insert(self, value: T) -> None:
        """
        Insert a value into the sorted linked list.
        
        The value will be inserted in the correct position to maintain sorted order.
        
        Args:
            value: The value to insert (must be int or str, consistent with existing elements)
            
        Raises:
            TypeError: If value type doesn't match the list's established type
        """
        self._validate_type(value)
        
        new_node = Node(value)
        
        # If list is empty or new value should be first
        if self._head is None or value < self._head.data:
            new_node.next = self._head
            self._head = new_node
            self._size += 1
            return
        
        # Find the correct position to insert
        current = self._head
        while current.next is not None and current.next.data < value:
            current = current.next
        
        # Insert the new node
        new_node.next = current.next
        current.next = new_node
        self._size += 1
    
    def remove(self, value: T) -> bool:
        """
        Remove the first occurrence of a value from the list.
        
        Args:
            value: The value to remove
            
        Returns:
            True if the value was found and removed, False otherwise
        """
        if self._head is None:
            return False
        
        # Check if head needs to be removed
        if self._head.data == value:
            self._head = self._head.next
            self._size -= 1
            return True
        
        # Search for the value to remove
        current = self._head
        while current.next is not None:
            if current.next.data == value:
                current.next = current.next.next
                self._size -= 1
                return True
            current = current.next
        
        return False
    
    def contains(self, value: T) -> bool:
        """
        Check if a value exists in the list.
        
        Args:
            value: The value to search for
            
        Returns:
            True if the value exists in the list, False otherwise
        """
        current = self._head
        while current is not None:
            if current.data == value:
                return True
            # Since list is sorted, we can stop early if we've passed the value
            if current.data > value:
                break
            current = current.next
        return False
    
    def __contains__(self, value: T) -> bool:
        """Support for 'in' operator."""
        return self.contains(value)
    
    def __len__(self) -> int:
        """Return the number of elements in the list."""
        return self._size
    
    def __iter__(self) -> Iterator[T]:
        """Make the list iterable."""
        current = self._head
        while current is not None:
            yield current.data
            current = current.next
    
    def __str__(self) -> str:
        """Return a string representation of the list."""
        elements = list(self)
        return f"SortedLinkedList({elements})"
    
    def __repr__(self) -> str:
        """Return a detailed string representation of the list."""
        type_name = self._data_type.__name__ if self._data_type else "unknown"
        elements = list(self)
        return f"SortedLinkedList(type={type_name}, elements={elements})"
    
    def is_empty(self) -> bool:
        """Check if the list is empty."""
        return self._head is None
    
    def clear(self) -> None:
        """Remove all elements from the list."""
        self._head = None
        self._size = 0
        # Keep the data type for consistency
    
    def to_list(self) -> list:
        """Convert the sorted linked list to a regular Python list."""
        return list(self)
    
    def get_type(self) -> Optional[type]:
        """Get the data type of elements in this list."""
        return self._data_type


# Convenience functions for creating typed lists
def create_int_list() -> SortedLinkedList[int]:
    """Create a sorted linked list for integer values."""
    return SortedLinkedList[int](int)


def create_str_list() -> SortedLinkedList[str]:
    """Create a sorted linked list for string values."""
    return SortedLinkedList[str](str)