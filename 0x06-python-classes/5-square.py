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

    def my_print(self):
        """print square with # char"""
        for x in range(0, self.__size):
            [print("#", end='') for y in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")
