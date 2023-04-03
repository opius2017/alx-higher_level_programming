#!/usr/bin/python3
"""
This module defines a Rectangle class
"""


class Rectangle:
    """
    Rectangle class definition
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Initializes a Rectangle instance with a given width and height
        """
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    @property
    def width(self):
        """
        Getter method for the width of the Rectangle instance
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter method for the width of the Rectangle instance
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """
        Getter method for the height of the Rectangle instance
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter method for the height of the Rectangle instance
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """
        Computes the area of the Rectangle instance
        """
        return self.width * self.height

    def perimeter(self):
        """
        Computes the perimeter of the Rectangle instance
        """
        return (2 * (self.width + self.height)
                if self.width != 0 and self.height != 0 else 0)

    def __str__(self):
        """
        Returns the string representation of the Rectangle instance
        """
        if self.width == 0 or self.height == 0:
            return ""
        else:
            symbol = str(self.print_symbol)
            return "\n".join([symbol * self.width] * self.height)

    def __repr__(self):
        """
        Returns a string representation of the Rectangle instance
        """
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """
        Prints a message when a Rectangle instance is deleted
        """
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
