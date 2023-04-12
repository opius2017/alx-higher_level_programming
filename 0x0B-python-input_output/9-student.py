#!/usr/bin/python3
"""
This module defines a class Student.
"""


class Student:
    """
    Defines a student by first name, last name and age.
    """
    def __init__(self, first_name, last_name, age):
        """
        Initializes a new Student instance of first name, last name and age.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Retrieves a dict representation of the Student instance.

        Returns:
            dict: A dict of the attributes of the Student instance.
        """
        return {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'age': self.age
        }
