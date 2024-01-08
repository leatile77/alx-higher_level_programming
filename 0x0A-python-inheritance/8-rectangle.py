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
        
