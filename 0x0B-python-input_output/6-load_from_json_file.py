#!/usr/bin/python3
""" Reads a JSON file and returns the corresponding Python object. """


import json


def load_from_json_file(filename):
    """
    Reads a JSON file and returns the corresponding Python object.

    Args:
        filename (str): The name of the JSON file to read.

    Returns:
        The Python object represented by the JSON file.

    Raises:
        None.
    """
    with open(filename, 'r') as f:
        obj = json.load(f)
    return obj
