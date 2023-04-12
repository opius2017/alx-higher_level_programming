#!/usr/bin/python3
"""
    Write a string to text file and return the number of characters written.

    :param filename: the name of the file to write to
    :type filename: str
    :param text: the text to write to the file
    :type text: str
    :return: the number of characters written to the file
    :rtype: int
    """


def write_file(filename="", text=""):
    """
    Write a UTF-8 encoded text string the number of characters written.

    :param filename: the name of the file to write to
    :type filename: str
    :param text: the text to write to the file
    :type text: str
    :return: the number of characters written to the file
    :rtype: int
    """
    count = 0
    with open(filename, "w", encoding="utf-8") as f:
        count = f.write(text)
    return count
