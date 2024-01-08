#!/usr/bin/python3
"""Defines a function that indents text."""
def text_indentation(text):
    """
    Args:
    text (str): text to indent
    """
    ind = 0
    
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    while ind < len(text) and text[ind] == ' ':
        ind += 1 # remove space at start of line

    while ind < len(text):
        
        if text[ind] == '\n':
            print(text[ind])
            ind += 1
        elif text[ind] in ".?:":
            print(text[ind], end="")
            ind += 1
            while ind < len(text) and text[ind] == ' ':
                ind += 1
            print("\n")

        else:
            print(text[ind], end="")
            ind += 1

    while ind < len(text) and text[ind] == ' ':
        ind += 1 # remove space at end of line
