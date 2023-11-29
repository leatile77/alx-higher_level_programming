#!/usr/bin/python3
for x in range(00, 100):
    if x < 10:
        print(f"0{x}", end=', ')
        continue
    print(f"{x}", end='\n' if x == 99 else ", ")
