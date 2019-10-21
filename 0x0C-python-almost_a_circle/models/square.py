#!/usr/bin/python3
"""This module is to define the Class Square that inherits from Rectangle"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Defining class Square"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initializing Square class"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """String method"""
        return"[Square] ({}) {}/{} - {}".format(
              self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """Getter for size"""
        return self.width

    @size.setter
    def size(self, value):
        """Setter for size"""
        self.width = value
        self.height = value
        self.width

    def update(self, *args, **kwargs):
        """Assigning arguments"""
        if args:
            data = ["id", "size", "x", "y"]
            for num, elem in enumerate(args):
                setattr(self, data[num], elem)
            return
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)

    def to_dictionary(self):
        """Returns the dictionary representation of a square"""
        return{"id": self.id, "size": self.size, "x": self.x, "y": self.y}
