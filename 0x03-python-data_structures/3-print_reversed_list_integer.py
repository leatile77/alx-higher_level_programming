#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    size = len(my_list) - 1
    if size <= 0 :
        return None
    else:
        for i in reversed(my_list):
            print("{:d}".format(i))
