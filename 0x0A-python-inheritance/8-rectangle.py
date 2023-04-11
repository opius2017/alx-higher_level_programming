#!/usr/bin/python3
"""
Module - 9-rectangle
"""


class BaseGeometry:
    """
    Class - BaseGeometry
    """
    def area(self):
        """
        Method - area
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Method - integer_validator
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """
    Class - Rectangle
    """
    def __init__(self, width, height):
        """
        Method - __init__
        """
        self.__width = 0
        self.__height = 0
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """
        Method - __str__
        """
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)

    def area(self):
        """
        Method - area
        """
        return self.__width * self.__height

    def print(self):
        """
        Method - print
        """
        print("[Rectangle] {:d}/{:d}".format(self.__width, self.__height))
