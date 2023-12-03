#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    checker = my_list[:]
    idx = 0
    for i in my_list:
        if i % 2 == 0:
            checker[idx] = True
        else:
            checker[idx] = False
        idx += 1

    return (checker)
