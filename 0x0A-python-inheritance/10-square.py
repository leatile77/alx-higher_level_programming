#!/usr/bin/python3
"""Defines class Square that inherits from Rectangle"""
Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """Defines a Square"""
    def __init__(self, size):
        """Initializes square.
        Args:
        size (int): size of square
        """

        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
