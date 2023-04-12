#!/usr/bin/python3
"""Appends a string at the end of a text file show nos of characters added. """


def append_write(filename="", text=""):
    """Appends a string at the end of a text file (UTF8).

    Args:
        filename (str): The name of the file to append to. "".
        text (str): The string to append to the file. Defaults to "".

    Returns:
        int: The number of characters added to the file.

    Examples:
        >>> append_write("test.txt", "Hello, World!")
        13
        >>> append_write("test.txt", "你好，世界！")
        7
    """
    count = 0
    with open(filename, mode="a", encoding="utf-8") as file:
        count = file.write(text)
    return count
