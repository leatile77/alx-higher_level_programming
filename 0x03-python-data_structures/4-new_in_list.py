#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new_list = my_list[:]
    if len(my_list) <= idx and idx <= 0:
        return new_list
    else:
        new_list[idx] = element
        return new_list
