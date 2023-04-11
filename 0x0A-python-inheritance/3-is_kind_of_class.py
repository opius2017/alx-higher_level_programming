#!/usr/bin/python3
""" A class that checks the inheritance function """


def is_kind_of_class(obj, a_class):
    """
    Determines if an object is an instance of a class or a subclass of a class.

    Args:
        obj: The object to check.
        a_class: The class or superclass to check against.

    Returns:
        True if obj is instance of a_class or subclass, False otherwise.
    """
    return isinstance(obj, a_class)
