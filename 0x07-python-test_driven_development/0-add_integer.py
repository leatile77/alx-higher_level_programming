#!/usr/bin/python3
"""Defines a function that adds 2 numbers.
Accepts integer or float.
Type casts first into integers.
Returns their sum
"""

def add_integer(a, b=98):
    """Adds a and b.
    Args:
    a (int/float): first arg
    b (int/float): second arg
    Raises:
    TypeError: if either a or b is not type int or float.
    """
    
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
