#!/usr/bin/python3
"""Defines a function for JSON representation of object."""
import json
def to_json_string(my_obj):
    """Function that returns JSON of an object.
    Args:
    my_obj (str): object to be used as JSON representation
    Return:
    JSON representation of an object
    """

    json_rep = json.dumps(my_obj)
    return json_rep
