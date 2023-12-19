#!/usr/bin/python3

"""A class called Square"""


class Square:
    """Inside the square"""

    def __init__(self, size=0, position=(0, 0)):
        """Initializes a square.

        Args:
            size (int): The size of the square.
        """
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        "get/set squares current position"
        return self.__position

    @position.setter
    def position(self, value):
        """set position of square"""
        if (not isinstance(value, tuple) or not len(value) == 2 or not all(isinstance(i, int) for i in value) or not all(i >= 0 for i in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Returns the area"""
        return (self.__size * self.__size)

    def my_print(self):
        """print square with # char"""
        if self.__size == 0:
            print("")
            return

        [print ("") for k in range(0, self.__position[1])]
        for x in range(0, self.__size):
            [print("#", end='') for m in range(0, self.__position[0])]
            [print("#", end='') for y in range(0, self.__size)]
            print("")
