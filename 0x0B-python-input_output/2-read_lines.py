#!/usr/bin/python3
"""Module that prints n lines of a text file"""


def read_lines(filename="", nb_lines=0):
    """Method to read line per line"""
    with open(filename, 'r') as f:
        if nb_lines <= 0:
            print(f.read(), end="")
            return
        for line in f:
            print(line, end="")
            nb_lines -= 1
            if nb_lines <= 0:
                break
