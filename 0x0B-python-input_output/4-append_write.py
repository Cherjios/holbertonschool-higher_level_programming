#!/usr/bin/python3
"""Module to appends a string to a text file"""


def append_write(filename="", text=""):
    """Method to appends a string into the file text"""
    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
