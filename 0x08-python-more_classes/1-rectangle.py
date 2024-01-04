#!/usr/bin/python3

"""Rectangle definittion"""
class Rectangle:
    """Inside the rectangle"""
    def __init__(self, width=0, height=0):
        """Initializes the rectangle.
        
        Args:
        width (int): width of rectangle.
        height (int): height of rectangle.
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Retrieve width"""
        return self.__width

    @width.setter
    def width(self, value):
        """set width, else raise err"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieve height"""
        return self.__height

    @height.setter
    def height(self, value):
        """set height, else raise err"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
