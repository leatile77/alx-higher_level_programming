#!/usr/bin/python3
for x in range(0, 10):
    for i in range(1, 10):
        if not i <= x:
            if x == 8 and i == 9:
                print(f"{x}{i}", end="\n")
            print(f"{x}{i}", end=", ")
        else:
             continue
