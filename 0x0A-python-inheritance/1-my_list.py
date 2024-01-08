#!/usr/bin/python3
"""Defines a class that inherits from list."""
class MyList(list):
    """Defines a function that sorts and prints a list of ints"""
    def print_sorted(self):
        """Prints sorted list"""
        print(sorted(self))
    
