#!/usr/bin/python3
"""Defines a function that checks instance/inherited instance"""
def is_kind_of_class(obj, a_class):
    """checks if the object is an instance of, or if obj is an instance of a class that inherited from the specified class.
    Args:
    obj (any): Object to be checked
    a_class (type): Class being checked against obj
    Return:
    True - if obj matches a_class
    False - otherwise
    """
    if isinstance(obj, a_class):
        return (True)
    return (False)
    
    
