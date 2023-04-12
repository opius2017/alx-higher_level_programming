#!/usr/bin/python3
"""Module that contains the to_json_string function."""


import json


def to_json_string(my_obj):
    """Return the JSON representation of an object.

    Args:
        my_obj: the object to serialize to JSON.

    Returns:
        The JSON string representation of the object.

    """
    return json.dumps(my_obj)
