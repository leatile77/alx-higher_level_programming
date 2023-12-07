#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) == str and roman_string is not None:
        romans = {'I': 1, 'V':5, 'X':10, 'L':50,'C':100, 'D':500}
        digits = 0
        prev = 0

        for i in reversed(roman_string):
            value = romans[i]
            if value < prev:
                digits -= value
            else:
                digits += value

            prev = value

        return (digits)
    else:
        return (0)
