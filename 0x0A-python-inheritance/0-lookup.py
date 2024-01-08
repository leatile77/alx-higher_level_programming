#!/usr/bin/python3
"""Defines a funtion that retrieves available methods and attributes of object"""
def lookup(obj):
    """Returns a list of methods and attributes."""
    return (dir(obj))
