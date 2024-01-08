#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Define unittest for max_integer()."""
    def test_unordered_list(self):
        """Test un-ordered list of ints"""
        uo = [1, 3, 2, 4]
        self.assertEqual(max_integer(uo), 4)

     def test_ordered_list(self):
        """Test ordered list of ints"""
        o = [1, 2, 3, 4]
        self.assertEqual(max_integer(o), 4)

     def test_max_at_start(self):
        """Test list of ints with max value at start"""
        start = [4, 3, 2, 1]
        self.assertEqual(max_integer(start), 4)

     def test_one_elem(self):
        """Test list with one element"""
        uno = [4]
        self.assertEqual(max_integer(uno), 4)

     def test_empty_list(self):
        """Test empty list"""
        empt = []
        self.assertEqual(max_integer(empt), None)

     def test_float_list(self):
        """Test list of floats"""
        fl = [1.1, 5.3, 4.2, 6.4]
        self.assertEqual(max_integer(fl), 6.4)

     def test_ints_floats(self):
        """Test list of ints and floats"""
        uo = [-1, 3, -7.2, 4.5]
        self.assertEqual(max_integer(uo), 4.5)

     def test_string(self):
        """Test string"""
        str = "me"
        self.assertEqual(max_integer(str), 'm')
        
     def test_string_list(self):
        """Test list of strings"""
        str = ["i", "too"]
        self.assertEqual(max_integer(str), "too")

     def test_empty_string(self):
        """Test empty string"""
        self.assertEqual(max_integer(""), None)

if __name__ == '__main__':
    unittest.main()
