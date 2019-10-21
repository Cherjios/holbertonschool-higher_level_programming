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
