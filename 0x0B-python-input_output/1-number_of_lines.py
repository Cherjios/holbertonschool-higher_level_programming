#!/usr/bin/python3
"""Module to returns the lines of a text"""


def number_of_lines(filename=""):
    with open(filename, 'r') as f:
        for num, l in enumerate(f):
            pass
        return num + 1
