#!/usr/bin/python3
"""This module contains one class."""


class Square:
    """The size of a square is crucial for a square, many things depend of
       it (area computation, etc.), so you, as class builder, must control
       the type and value of this attribute. One way to have the control is
       to keep it privately. You will see in next tasks how to get, update
       and validate the size value."""

    def __init__(self, size=0):
        """Attributes of the class.
           seize: length of a side of the square."""

        """size must be an integer, otherwise raise a TypeError exception
        with the message size must be an integer
        if size is less than 0, raise a ValueError exception with the
        message size must be >= 0"""

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):

        """ Method to return thew current square area """

        return (self.__size**2)
