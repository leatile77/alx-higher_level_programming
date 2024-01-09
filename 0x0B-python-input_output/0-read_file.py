#!/usr/bin/python3
"""Defines a function that reads and prints from file"""
def read_file(filename=""):
    """Function that Reads from file and prints
    Args:
    filename (str): holds name of file ro be read
    """
    with open(filename) as file:
        print(file.read(), end="")
