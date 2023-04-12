#!/usr/bin/python3
""" Writes a Python object to a text file in JSON format. """


import json


def save_to_json_file(my_obj, filename):
    """
    Writes a Python object to a text file in JSON format.

    Args:
        my_obj (object): The Python object to be serialized.
        filename (str): The name of the file to write to.

    Returns:
        None.

    Raises:
        None.
    """
    with open(filename, 'w') as f:
        json.dump(my_obj, f)
