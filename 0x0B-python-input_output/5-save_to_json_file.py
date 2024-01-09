#!/usr/bin/python3
"""Defines a module that writes object as JSON rep to a file"""
import json
def save_to_json_file(my_obj, filename):
    """Function that writes object to file, but as JSON rep.
    Args:
    my_obj (any): Object to write as JSON representation
    filename (str): Name of File to write to
    """
    json_rep = json.dumps(my_obj)
    with open(filename, 'w') as file:
        file.write(json_rep)
