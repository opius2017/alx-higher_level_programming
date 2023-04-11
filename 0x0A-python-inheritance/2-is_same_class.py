#!/usr/bin/python3
"""Defines a function that checks if an object is instance of a class"""


def is_same_class(obj, a_class):
    """
    Returns True if the object is exactly an instance of the specified class;
    otherwise False.

    Args:
        obj (object): The object to check.
        a_class (class): The specified class to check.

    Returns:
        bool: True if the object is exactly an instance of the specified class;
        otherwise False.
    """
    return type(obj) == a_class
