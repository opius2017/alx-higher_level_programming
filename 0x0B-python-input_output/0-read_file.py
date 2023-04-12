#!/usr/bin/python3
"""
This module defines a function that reads a text file and prints it to stdout.
"""


def read_file(filename=""):
    """
    Read a file with the given filename and print contents to stdout.

    Args:
        filename (str): File name to read. Defaults to an empty string.
    """
    with open(filename, encoding="UTF8") as f:
        for line in f:
            print(line, end="")
