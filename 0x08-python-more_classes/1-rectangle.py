#!/usr/bin/python3
"""This module is to define a rectangle"""


class Rectangle:
    """Rectangle defining the width (self)"""

    def __init__(self, width=0, height=0):
        """Setting arguments"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """ Property for the width of the Rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter the widht"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >=0")
        self.__width = value

    @property
    def height(self):
        """ Property for the height of the Rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter the height"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >=0")
        self.__height = value
