#!/usr/bin/python3
"""Defines a function that checks class"""
def is_same_class(obj, a_class):
    """checks if the object is exactly an instance of the specified class.
    Args:
    obj (any): Object to be checked
    a_class (type): Class being checked against obj
    Return:
    True - if obj matches a_class
    False - otherwise
    """
    if type(obj) == a_class:
        return (True)
    return (False)
    
    
