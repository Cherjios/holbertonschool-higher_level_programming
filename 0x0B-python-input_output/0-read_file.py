#!/usr/bin/python3
"""Module to read a file"""


def read_file(filename=""):
    """Read a text file UTF8 and print it to stdout"""
    with open(filename, 'r', encoding="utf-8") as f:
        file_read = f.read()
    print(file_read, end="")
