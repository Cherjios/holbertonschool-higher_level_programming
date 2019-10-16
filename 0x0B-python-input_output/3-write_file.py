#!/usr/bin/python3
"""Module to write a string to a text file"""


def write_file(filename="", text=""):
    """Method to write a string into the file text"""
    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
