#!/usr/bin/python3
""" This module Prints a square with the character # """


def print_square(size):
    """Method -  printing a square with the character #"""

    """Arg:
        size: takes an integer as a value, otherwise raise a TypeError
        with the message size must be an integer
        size les than 0, ValueError with message size must be >= 0
        size is a float and less than 0, raise a TypeError with message
        size must be an integer """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size == 0:
        return
    else:
        print('\n'.join(['#' * size for j in range(size)]))

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/4-print_square.txt")
