#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < 0:
        return None
    size = len(my_list) - 1

    if idx > size:
        return None

    else:
        return my_list[idx]
