#!/usr/bin/python3
"""Defines a function for object represented by JSON string."""
import json
def from_json_string(my_str):
    """Function that returns object of JSON string.
    Args:
    my_str (str): JSON string to be returned as object
    Return:
    object represented by a JSON string
    """
    obj_rep = json.loads(my_str)
    return obj_rep
