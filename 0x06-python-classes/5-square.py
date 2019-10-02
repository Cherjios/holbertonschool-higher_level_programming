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
        self.size = size

    @property
    def size(self):
        """ Property for the lenght of a side of square"""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):

        """ Method to return thew current square area """

        return (self.__size ** 2)

    def my_print(self):
        """ Prints in stdout the square with the character #"""
        for i in range(self.size):
            for j in range(self.size):
                print("#", end="\n" if j is self.size - 1 and i != j else "")
        print()
