#!/usr/bin/python3
"""Module to returns the lines of a text"""


def number_of_lines(filename=""):
    with open(filename, 'r', encoding="utf-8") as f:
        return len(f.readlines())
