#!/usr/bin/python3
"""Module for add_integer method."""


def add_integer(a, b=98):
    """ Add integer returns the addition of a and b

    Args:
        a: The first integer.
        b: The second integer.

    Returns: The sume of  int a and int b """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return(int(a) + int(b))

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")
