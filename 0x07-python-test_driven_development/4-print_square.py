#!/usr/bin/python3
"""Defines a function that prints a square using #"""
def print_square(size):
    """
    Args:
    size (int): size of sides of square
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")

    for i in range(0, size):
        for j in range(0, size):
            print("#", end='')
        print("")
