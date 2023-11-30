#!/usr/bin/python3
x = 0
while x <= 89:
    if x % 10 == 0:
        x += 1 + x // 10
    print("{:02d}".format(x), end='\n' if x == 89 else ', ')
    x += 1
