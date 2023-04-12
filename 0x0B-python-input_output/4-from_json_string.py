#!/usr/bin/python3
""" Converts a JSON string to an object. """


import json


def from_json_string(my_str):
    """
    Converts a JSON string to an object.

    Args:
        my_str (str): A string containing JSON data.

    Returns:
        An object represented by the JSON data in my_str.

    """
    return json.loads(my_str)
