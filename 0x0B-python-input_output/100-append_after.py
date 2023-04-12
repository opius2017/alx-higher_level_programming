#!/usr/bin/python3
"""
Append a line of text to a file, after each line containing a specific string
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Appends a line of text to file, after each line with a specific string

    Args:
        filename (str): The name of the file to append to
        search_string (str): The string to search in each line of the file
        new_string (str): String to append to file

    Returns:
        None
    """
    with open(filename, mode="r+", encoding="utf-8") as f:
        lines = f.readlines()
        f.seek(0)
        for line in lines:
            f.write(line)
            if search_string in line:
                f.write(new_string)
        f.truncate()
