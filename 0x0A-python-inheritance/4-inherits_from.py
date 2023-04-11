#!/usr/bin/python3
"""
Module for the inherits_from method
"""


def inherits_from(obj, a_class):
    """
    Returns True if obj is an instance of a subclass of a_class.
    """
    obj_type = type(obj)
    return issubclass(obj_type, a_class) and obj_type != a_class
