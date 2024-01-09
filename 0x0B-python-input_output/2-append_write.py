#!/usr/bin/python3
"""Defines a function that appends to a file"""
def append_write(filename="", text=""):
    """Function that appends to file and returns number of printed chars
    Args:
    filename (str): holds name of file to append to
    text (str): holds text to append to filename
    Return:
    number of characters appended
    """
    with open(filename, 'a') as file:
        file.write(text)
        return (len(text))
