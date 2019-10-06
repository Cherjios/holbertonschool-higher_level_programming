#!/usr/bin/python3
"""Module for printing My Name"""


def say_my_name(first_name, last_name=""):
    """Function that take tow strings and prints them"""

    """Args:
        first_name: The first string.
        last_name: The second string.
    first_name and last_name must be strings otherwise, 
    raise a TypeError exception with the message first_name must be a string or 
    last_name must be a string"""

    if not isinstance (first_name, (str)):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, (str)):
        raise TypeError("last_name must be a string")
    print ("My name is {} {}".format(first_name, last_name))

if __name__=="__main__":
    import doctest
    doctest.testfile("tests/3-say_my_name.txt")

