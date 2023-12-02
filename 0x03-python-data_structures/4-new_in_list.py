#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if my_list == None:
        return None
    new_list = my_list[:]
    if idx < 0:
        return new_list

    size = len(my_list) - 1
    if idx > size:
        return new_list
    else:
        new_list[idx] = element
        return new_list
