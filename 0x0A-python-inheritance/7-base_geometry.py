#!/usr/bin/python3
"""Defines a base geometry class"""
class BaseGeometry:
    """Base Geometry"""
    def area(self):
        """Raises:
        Exception: not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates that parameter is an int > 0
        Args:
        name (str): Name of argument
        value (int): argument to be validated
        Raises:
        TypeError: if value not int
        ValueError: if value <= 0
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
