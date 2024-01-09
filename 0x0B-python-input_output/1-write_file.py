#!/usr/bin/python3
"""Defines a function that writes to a file"""
def write_file(filename="", text=""):
    """Function that writes to file and returns number of printed chars
    Args:
    filename (str): holds name of file to write to
    text (str): holds text to write to filename
    Return:
    number of characters written
    """
    with open(filename, 'w') as file:
        file.write(text)
        return (len(text))
