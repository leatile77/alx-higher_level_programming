#!/usr/bin/python3

"""A class called Square"""


class Square:
    """Inside the square"""

    def __init__(self, size=0):
        """Initializes a square.

        Args:
            size (int): The size of the square.
        """
        self.__size = size

    @property
    def size(self):
            """Get /& Set size"""
            return self.__size
        
    @size.setter
    def size(self, value):
        """set size accordingly, else error"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the area"""
        return (self.__size * self.__size)
