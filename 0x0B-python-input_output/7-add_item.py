#!/usr/bin/python3
"""
Adds all arguments to a Python list and saves them to a file in JSON format.
"""


import sys
import json
from typing import List
from os import path
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


def add_item(args: List[str], filename: str) -> None:
    """
    Adds all arguments to a list and save to a JSON file format.
    """
    items = []
    if path.exists(filename):
        items = load_from_json_file(filename)
    items.extend(args[1:])
    save_to_json_file(items, filename)


if __name__ == '__main__':
    add_item(sys.argv, 'add_item.json')
