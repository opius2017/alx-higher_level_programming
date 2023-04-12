#!/usr/bin/python3
"""Defines a Student class."""


class Student:
    """Represent a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize a new instance of the Student class."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieve a dictionary representation of a Student instance.

        Args:
            attrs (list): A list of attribute names to retrieve.

        Returns:
            dict: A dict containing the Student instance attributes.
        """
        if attrs is None:
            return self.__dict__
        else:
            return {key: val
                    for key, val in self.__dict__.items()
                    if key in attrs}

    def reload_from_json(self, json):
        """
        Replace attrib of Student instance with values from a dict.

        Args:
            json (dict): A dict containing attrib names and values.

        Returns:
            None
        """
        for key, val in json.items():
            setattr(self, key, val)
