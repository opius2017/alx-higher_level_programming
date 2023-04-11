#!/usr/bin/python3
"""
Module: Defines a rectangle sub-class
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Represent a class to define square using Rectangle class.
    """
    def __init__(self, size):
        """
        Initialize a new Square.
        Args:
            size (int): The size of the new Square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """Return the string representation of the Square."""
        return "[Square] {}/{}".format(self.__size, self.__size)

    def area(self):
        """Return the area of the Square."""
        return self.__size ** 2
