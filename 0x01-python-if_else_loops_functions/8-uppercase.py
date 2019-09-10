#!/usr/bin/python3
def uppercase(str):
    for c in str:
        if ord(c) == 32:
            print(c, end="")
            continue
        if ord(c) >= 65 and ord(c) <= 90:
            print(c, end="")
        elif ord(c) >= 48 and ord(c) <= 57:
            print(c, end="")
        else:
            c = chr(ord(c) - 32)
            print(c, end="")
    print()
