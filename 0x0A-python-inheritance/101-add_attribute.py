#!/usr/bin/python3
"""
Class contains a function that adds a new attribute to an object
"""


def add_attribute(obj, attr, value):
    """
    Adds a new attribute to an object if it’s possible.

    Args:
        obj (object): The object to which the attribute will be added.
        attr (str): The name of the attribute to be added.
        value (any): The value of the attribute to be added.

    Raises:
        TypeError: If the attribute cannot be added to the object.

    Returns:
        None.
    """

    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")

    setattr(obj, attr, value)
