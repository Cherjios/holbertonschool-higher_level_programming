#!/usr/bin/python3
for digit1 in range(0, 10):
    for digit2 in range(0, 10):
        if digit1 != digit2 and digit2 > digit1:
            if digit1 != 8 or digit2 != 9:
                print("{:d}{:d}, ".format(digit1, digit2), end="")
            else:
                print("{:d}{:d}".format(digit1, digit2))
