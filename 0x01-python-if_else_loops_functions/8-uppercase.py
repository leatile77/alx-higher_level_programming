#!/usr/bin/python3

def conv_upper(char):
    if ord(char) >= 97 and ord(char) <= 122:
        return (ord(char) - 32)
    else:
        return ord(char)

def uppercase(str):
    new_str = ""
    for letter in str:
        new_str += "%c" % conv_upper(letter)
    print("{:s}".format(new_str))
