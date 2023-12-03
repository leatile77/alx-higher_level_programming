#!/usr/bin/python3
def multiple_returns(sentence):
    first = ''
    size = 0
    my_tuple = (0, 0)
    
    if sentence == "":
        first = None
        size = 0
    else:
        first = sentence[0]
        size = len(sentence)

    my_tuple = (size, first)

    return my_tuple
