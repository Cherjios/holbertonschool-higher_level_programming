#!/usr/bin/python3
"""Module for Rectangle class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A class Square that inherits from Rectangle"""

    def __init__(self, size):
        """Sub class representing a Rectangle"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Method that returns area of a Rectangle"""
        return self.__size * self.__size

    def __str__(self):
        """String Method"""
        return "[Square] {}/{}".format(self.__size, self.__size)
