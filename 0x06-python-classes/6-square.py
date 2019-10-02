#!/usr/bin/python3
"""This module contains one class."""


class Square:
    """The size of a square is crucial for a square, many things depend of
       it (area computation, etc.)"""

    def __str__(self):
        self.my_print()

    def __init__(self, size=0, position=(0, 0)):
        """Attributes of the class.
           seize: length of a side of the square."""

        self.size = size
        self.position = position

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

    @property
    def position(self):
        """ Property for the position of the squre"""

        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or len(value) != 2 or \
         len([x for x in value if isinstance(x, int) and x >= 0]) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value

    def area(self):

        """ Method to return thew current square area """

        return (self.__size ** 2)

    def my_sprint(self):
        """Returns string representation of this square."""
        ret = ""
        if not self.size:
            return "\n"

        for i in range(self.position[1]):
                ret += "\n"
        for i in range(self.size):
            for j in range(self.position[0]):
                ret += " "
            for j in range(self.size):
                ret += "#"
            ret += "\n"
        return ret

    def my_print(self):
        """ Prints in stdout the square with the character #"""
        print(self.my_sprint(), end="")
