#!/usr/bin/python3
"""
Adds all arguments to a Python list and saves them to a file in JSON format.
"""


import json
import sys

from load_from_json_file import load_from_json_file
from save_to_json_file import save_to_json_file

filename = "add_item.json"

try:
    items = load_from_json_file(filename)
except FileNotFoundError:
    items = []

items += sys.argv[1:]

save_to_json_file(items, filename)
