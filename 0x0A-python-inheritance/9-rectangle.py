#!/usr/bin/python3
"""Defines class that inherits from BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """Defines Rectangle using BaseGeometry."""
    def __init__(self, width, height):
        """Initialize a new Rectangle.
        Args:
        width (int): width of Rectangle
        height (int): height of Rectangle
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
        
    def area(self):
        """Returns area of a rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """Returns print() and str() representation of Rectangle."""
        strr = "[" + str(self.__class__.__name__) + "] "
        strr += str(self.__width) + "/" + str(self.__height)
        return strr
