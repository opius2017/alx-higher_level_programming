#!/usr/bin/python3
"""
Module for Rectangle class that inherits from BaseGeometry.
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    A class to represent a rectangle using BaseGeometry.
    """

    def __init__(self, width, height):
        """
        Initialize a new Rectangle instance.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
