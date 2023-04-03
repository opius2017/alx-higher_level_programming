#!/usr/bin/python3
"""
This module defines a Rectangle class
"""


class Rectangle:
    """
    A Rectangle class with private attributes width and height
    """

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """ Initializes a Rectangle instance """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """ Retrieves the width of a Rectangle instance """
        return self.__width

    @width.setter
    def width(self, value):
        """ Sets the width of a Rectangle instance """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """ Retrieves the height of a Rectangle instance """
        return self.__height

    @height.setter
    def height(self, value):
        """ Sets the height of a Rectangle instance """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """ Returns the area of a Rectangle instance """
        return self.__width * self.__height

    def perimeter(self):
        """ Returns the perimeter of a Rectangle instance """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """ Returns a string representation of a Rectangle instance """
        if self.__width == 0 or self.__height == 0:
            return ""
        return "\n".join(["#" * self.__width for _ in range(self.__height)])

    def __repr__(self):
        """ Returns a string representation of a Rectangle instance
            that can be used to recreate it """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """ Prints a message when a Rectangle instance is deleted """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
