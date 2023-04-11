#!/usr/bin/python3
"""Module documentation"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Class documentation"""

    def __init__(self, size):
        """Initialize Square"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """Return Square description"""
        return "[Square] {}/{}".format(self.__size, self.__size)
