#!/usr/bin/python3
"""
Module for class_to_json function.
"""


def class_to_json(obj):
    """Return the dictionary description with simple data structure."""
    return obj.__dict__
