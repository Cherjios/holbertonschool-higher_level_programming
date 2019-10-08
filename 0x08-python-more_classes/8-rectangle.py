#!/usr/bin/python3
"""This module is to define a rectangle"""


class Rectangle:
    """Rectangle defining the width (self)"""

    number_of_instances = 0
    """Number of instance"""

    print_symbol = "#"
    """Print symbol any char"""

    def __init__(self, width=0, height=0):
        """Setting arguments"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    def area(self):
        """" Returns the area of the rectangle"""
        return(self.width * self.height)

    def perimeter(self):
        """ Returns the perimeter of the rectangle"""
        if not self.width or not self.height:
            return 0
        return 2*(self.width + self.height)

    def __str__(self):
        """Returns string representation of rectangle with ##"""
        if not self.width or not self.height:
            return ""
        return((str(self.print_symbol) * self.width + "\n") *
               self.height)[:-1]

    def __repr__(self):
        """Returns the formal representation of rectangle"""
        return "Rectangle(" + str(self.width) + ", " + str(self.height) + ")"

    def __del__(self):
        """Delete class  when it is called"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Returns the bigger of two rectangles.
        Args:
            rect_1: The first rectangle.
            rect_2: The second rectangle.
        Raises:
            TypeError: If rect_1, rect_2 are not instances of Rectangle.
        Returns:
            The rectangle with the larger area.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_2.area() > rect_1.area():
            return rect_2
        return rect_1
