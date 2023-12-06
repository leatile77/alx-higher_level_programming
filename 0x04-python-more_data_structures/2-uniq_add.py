#!/usr/bin/python3
def uniq_add(my_list=[]):
    result = 0
    uniq_list = set(my_list)

    for i in uniq_list:
        result += i

    return (result)
