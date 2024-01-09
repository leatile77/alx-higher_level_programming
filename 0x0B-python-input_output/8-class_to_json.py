#!/usr/bin/python3
"""Defines a function for class to json"""
def class_to_json(obj):
    """Function that returns dictionary description for JSON serialization of an object.
    Args:
    obj (object): Instance of a class
    Return:
    dictionary description
    """
    return obj.__dict__
