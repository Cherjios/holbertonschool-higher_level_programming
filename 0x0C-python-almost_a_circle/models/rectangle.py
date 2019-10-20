#!/usr/bin/python3
"""This module is to define class Rectangle"""

from models.base import Base


class Rectangle(Base):
    """Defining class Reactangle"""

    print_symbol = "#"

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializing Reactangle"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Getter for width"""
        return self.__width

    @property
    def height(self):
        """Getter for height"""
        return self.__height

    @property
    def x(self):
        """Getter for x"""
        return self.__x

    @property
    def y(self):
        """Getter for y"""
        return self.__y

    @width.setter
    def width(self, value):
        """Setter for widht"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """Setter for height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        """Setter for x"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        """Setter for y"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """" Returns the area of the rectangle"""
        return(self.width * self.height)

    def display(self):
        """Returns string representation of rectangle with ##"""
        for i in range(self.__y):
            print()
        for i in range(self.height):
            for i in range(self.__x):
                print(" ", end="")
            for i in range(self.width):
                print("#", end="")
            print()

    def __str__(self):
        """String method"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
               self.id, self.__x, self.__y, self.__width, self.__height)