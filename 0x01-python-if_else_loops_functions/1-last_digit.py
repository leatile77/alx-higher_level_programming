#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    last = ((number * -1) % 10) * -1
else:
    last = number % 10

start_text = "Last digit of %d is %d" % (number, last)

if last > 5:
    print(start_text, "and is greater than 5")
elif last == 0:
    print(start_text, "and is 0")
else:
    print(start_text, "and less than 6 and not 0")
