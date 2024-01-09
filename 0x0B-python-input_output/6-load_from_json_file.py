#!/usr/bin/python3
"""Defines a module that reads JSON file, and creates object from it."""
import json
def load_from_json_file(filename):
    """Function that creates object from json file.
    Args:
    filename (str): Name of File to read from
    Returns:
    object created from JSON representation read from json file
    """
    with open(filename) as file:
        json_rep = file.read()
    my_obj = json.loads(json_rep)

    return my_obj
