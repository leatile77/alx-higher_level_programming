#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    if idx < 0:
        return my_list
    size = len(my_list) - 1
    if idx > size:
        return my_list
    else:
        my_list[idx] = element
        return my_list
