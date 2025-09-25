"""
Tests for SortedLinkedList implementation.
"""

import unittest
from sorted_linked_list import SortedLinkedList, create_int_list, create_str_list


class TestSortedLinkedList(unittest.TestCase):
    """Test cases for SortedLinkedList functionality."""
    
    def test_empty_list_creation(self):
        """Test creating an empty list."""
        lst = SortedLinkedList()
        self.assertTrue(lst.is_empty())
        self.assertEqual(len(lst), 0)
        self.assertEqual(list(lst), [])
        self.assertIsNone(lst.get_type())
    
    def test_typed_list_creation(self):
        """Test creating lists with explicit types."""
        int_list = create_int_list()
        str_list = create_str_list()
        
        self.assertEqual(int_list.get_type(), int)
        self.assertEqual(str_list.get_type(), str)
        self.assertTrue(int_list.is_empty())
        self.assertTrue(str_list.is_empty())
    
    def test_integer_insertion_and_sorting(self):
        """Test inserting integers and verifying sorted order."""
        lst = SortedLinkedList()
        
        # Insert integers in random order
        values = [5, 2, 8, 1, 9, 3]
        for val in values:
            lst.insert(val)
        
        # Verify sorted order
        expected = [1, 2, 3, 5, 8, 9]
        self.assertEqual(list(lst), expected)
        self.assertEqual(len(lst), 6)
        self.assertEqual(lst.get_type(), int)
    
    def test_string_insertion_and_sorting(self):
        """Test inserting strings and verifying sorted order."""
        lst = SortedLinkedList()
        
        # Insert strings in random order
        values = ["zebra", "apple", "banana", "cherry", "date"]
        for val in values:
            lst.insert(val)
        
        # Verify sorted order
        expected = ["apple", "banana", "cherry", "date", "zebra"]
        self.assertEqual(list(lst), expected)
        self.assertEqual(len(lst), 5)
        self.assertEqual(lst.get_type(), str)
    
    def test_type_enforcement(self):
        """Test that mixing types raises an error."""
        lst = SortedLinkedList()
        
        # First insertion determines type
        lst.insert(5)
        self.assertEqual(lst.get_type(), int)
        
        # Trying to insert string should raise TypeError
        with self.assertRaises(TypeError):
            lst.insert("hello")
    
    def test_explicit_type_enforcement(self):
        """Test explicit type specification."""
        int_list = SortedLinkedList(int)
        str_list = SortedLinkedList(str)
        
        # Valid insertions
        int_list.insert(42)
        str_list.insert("hello")
        
        # Invalid insertions
        with self.assertRaises(TypeError):
            int_list.insert("invalid")
        
        with self.assertRaises(TypeError):
            str_list.insert(123)
    
    def test_invalid_type_specification(self):
        """Test that invalid types raise ValueError."""
        with self.assertRaises(ValueError):
            SortedLinkedList(float)
    
    def test_contains_functionality(self):
        """Test the contains method and 'in' operator."""
        lst = SortedLinkedList()
        values = [3, 1, 4, 1, 5, 9, 2, 6]
        
        for val in values:
            lst.insert(val)
        
        # Test contains method
        self.assertTrue(lst.contains(5))
        self.assertTrue(lst.contains(1))
        self.assertFalse(lst.contains(7))
        self.assertFalse(lst.contains(0))
        
        # Test 'in' operator
        self.assertIn(5, lst)
        self.assertIn(1, lst)
        self.assertNotIn(7, lst)
        self.assertNotIn(0, lst)
    
    def test_remove_functionality(self):
        """Test removing elements."""
        lst = SortedLinkedList()
        values = [3, 1, 4, 1, 5, 9, 2, 6]
        
        for val in values:
            lst.insert(val)
        
        initial_length = len(lst)
        
        # Remove existing element
        self.assertTrue(lst.remove(5))
        self.assertEqual(len(lst), initial_length - 1)
        self.assertNotIn(5, lst)
        
        # Remove first occurrence of duplicate
        self.assertTrue(lst.remove(1))
        self.assertEqual(len(lst), initial_length - 2)
        self.assertIn(1, lst)  # Should still contain the other 1
        
        # Try to remove non-existent element
        self.assertFalse(lst.remove(10))
        self.assertEqual(len(lst), initial_length - 2)
    
    def test_remove_from_empty_list(self):
        """Test removing from empty list."""
        lst = SortedLinkedList()
        self.assertFalse(lst.remove(1))
    
    def test_remove_head_element(self):
        """Test removing the head element."""
        lst = SortedLinkedList()
        lst.insert(1)
        lst.insert(2)
        lst.insert(3)
        
        # Remove head (smallest element)
        self.assertTrue(lst.remove(1))
        self.assertEqual(list(lst), [2, 3])
    
    def test_iteration(self):
        """Test that iteration works correctly."""
        lst = SortedLinkedList()
        values = [5, 2, 8, 1, 9]
        
        for val in values:
            lst.insert(val)
        
        # Test iteration
        result = []
        for item in lst:
            result.append(item)
        
        self.assertEqual(result, [1, 2, 5, 8, 9])
    
    def test_string_representation(self):
        """Test string representations."""
        lst = SortedLinkedList()
        
        # Empty list
        self.assertEqual(str(lst), "SortedLinkedList([])")
        
        # List with elements
        lst.insert(3)
        lst.insert(1)
        lst.insert(2)
        
        self.assertEqual(str(lst), "SortedLinkedList([1, 2, 3])")
        self.assertIn("type=int", repr(lst))
        self.assertIn("elements=[1, 2, 3]", repr(lst))
    
    def test_clear_functionality(self):
        """Test clearing the list."""
        lst = SortedLinkedList()
        lst.insert(1)
        lst.insert(2)
        lst.insert(3)
        
        self.assertFalse(lst.is_empty())
        self.assertEqual(len(lst), 3)
        
        lst.clear()
        
        self.assertTrue(lst.is_empty())
        self.assertEqual(len(lst), 0)
        self.assertEqual(list(lst), [])
        # Type should be preserved
        self.assertEqual(lst.get_type(), int)
    
    def test_to_list_conversion(self):
        """Test converting to regular Python list."""
        lst = SortedLinkedList()
        values = [3, 1, 4, 1, 5]
        
        for val in values:
            lst.insert(val)
        
        python_list = lst.to_list()
        self.assertEqual(python_list, [1, 1, 3, 4, 5])
        self.assertIsInstance(python_list, list)
    
    def test_duplicate_values(self):
        """Test handling duplicate values."""
        lst = SortedLinkedList()
        
        # Insert duplicates
        lst.insert(5)
        lst.insert(3)
        lst.insert(5)
        lst.insert(1)
        lst.insert(3)
        lst.insert(5)
        
        # Should maintain all duplicates in sorted order
        expected = [1, 3, 3, 5, 5, 5]
        self.assertEqual(list(lst), expected)
        self.assertEqual(len(lst), 6)
        
        # Removing should only remove first occurrence
        lst.remove(5)
        self.assertEqual(list(lst), [1, 3, 3, 5, 5])
        
        lst.remove(3)
        self.assertEqual(list(lst), [1, 3, 5, 5])
    
    def test_edge_cases(self):
        """Test various edge cases."""
        lst = SortedLinkedList()
        
        # Single element
        lst.insert(42)
        self.assertEqual(list(lst), [42])
        self.assertEqual(len(lst), 1)
        
        # Remove single element
        lst.remove(42)
        self.assertTrue(lst.is_empty())
        
        # Insert after clearing
        lst.insert(10)
        self.assertEqual(list(lst), [10])
    
    def test_large_dataset(self):
        """Test with a larger dataset."""
        import random
        
        lst = SortedLinkedList()
        values = list(range(100))
        random.shuffle(values)
        
        # Insert all values
        for val in values:
            lst.insert(val)
        
        # Should be in sorted order
        self.assertEqual(list(lst), list(range(100)))
        self.assertEqual(len(lst), 100)
        
        # Remove some values
        for i in range(0, 100, 10):  # Remove 0, 10, 20, ..., 90
            self.assertTrue(lst.remove(i))
        
        expected = [i for i in range(100) if i % 10 != 0]
        self.assertEqual(list(lst), expected)
        self.assertEqual(len(lst), 90)


if __name__ == '__main__':
    unittest.main()