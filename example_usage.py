#!/usr/bin/env python3
"""
Example usage of the SortedLinkedList library.

This file demonstrates how to use the SortedLinkedList for both integers and strings.
"""

from sorted_linked_list import SortedLinkedList, create_int_list, create_str_list


def demonstrate_integer_list():
    """Demonstrate usage with integers."""
    print("=== Integer SortedLinkedList Demo ===")
    
    # Create a sorted linked list for integers
    int_list = create_int_list()
    
    # Insert numbers in random order
    numbers = [42, 17, 89, 3, 56, 23, 91, 8]
    print(f"Inserting numbers: {numbers}")
    
    for num in numbers:
        int_list.insert(num)
    
    print(f"Sorted result: {int_list}")
    print(f"Length: {len(int_list)}")
    print(f"Type: {int_list.get_type()}")
    
    # Demonstrate search
    search_value = 56
    if search_value in int_list:
        print(f"✓ Found {search_value} in the list")
    else:
        print(f"✗ {search_value} not found in the list")
    
    # Demonstrate removal
    remove_value = 17
    if int_list.remove(remove_value):
        print(f"✓ Removed {remove_value} from the list")
        print(f"List after removal: {int_list}")
    else:
        print(f"✗ Could not remove {remove_value}")
    
    # Demonstrate iteration
    print("Iterating through the list:")
    for i, value in enumerate(int_list):
        print(f"  {i}: {value}")
    
    print()


def demonstrate_string_list():
    """Demonstrate usage with strings."""
    print("=== String SortedLinkedList Demo ===")
    
    # Create a sorted linked list for strings
    str_list = create_str_list()
    
    # Insert words in random order
    words = ["python", "algorithm", "sorted", "linked", "list", "example", "zebra", "apple"]
    print(f"Inserting words: {words}")
    
    for word in words:
        str_list.insert(word)
    
    print(f"Sorted result: {str_list}")
    print(f"Length: {len(str_list)}")
    print(f"Type: {str_list.get_type()}")
    
    # Demonstrate search
    search_word = "algorithm"
    if str_list.contains(search_word):
        print(f"✓ Found '{search_word}' in the list")
    else:
        print(f"✗ '{search_word}' not found in the list")
    
    # Convert to regular Python list
    python_list = str_list.to_list()
    print(f"As Python list: {python_list}")
    
    print()


def demonstrate_type_safety():
    """Demonstrate type safety features."""
    print("=== Type Safety Demo ===")
    
    # Create a list and add an integer
    mixed_list = SortedLinkedList()
    mixed_list.insert(42)
    
    print(f"List after inserting integer: {mixed_list}")
    print(f"Inferred type: {mixed_list.get_type()}")
    
    # Try to add a string (this will fail)
    try:
        mixed_list.insert("hello")
        print("✗ This should not happen!")
    except TypeError as e:
        print(f"✓ Type safety working: {e}")
    
    print()


def demonstrate_duplicates():
    """Demonstrate handling of duplicate values."""
    print("=== Duplicate Handling Demo ===")
    
    duplicate_list = SortedLinkedList()
    
    # Insert duplicate values
    values = [5, 3, 5, 1, 3, 5, 2, 1]
    print(f"Inserting values with duplicates: {values}")
    
    for val in values:
        duplicate_list.insert(val)
    
    print(f"Sorted result: {duplicate_list}")
    
    # Remove one occurrence
    duplicate_list.remove(5)
    print(f"After removing one '5': {duplicate_list}")
    
    print()


def main():
    """Run all demonstrations."""
    print("SortedLinkedList Library Usage Examples")
    print("=" * 50)
    print()
    
    demonstrate_integer_list()
    demonstrate_string_list()
    demonstrate_type_safety()
    demonstrate_duplicates()
    
    print("All demonstrations completed successfully!")


if __name__ == "__main__":
    main()