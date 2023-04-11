#!/usr/bin/python3
"""
Module containing the MyInt class
"""


class MyInt(int):
    """
    MyInt class that inherits from int
    """

    def __eq__(self, other):
        """
        Invert the == operator
        """
        return int(self) != int(other)

    def __ne__(self, other):
        """
        Invert the != operator
        """
        return int(self) == int(other)
