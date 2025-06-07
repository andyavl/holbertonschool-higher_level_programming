#!/usr/bin/python3
"""
This module defines a Student class that includes basic attributes and
a method for serializing selected attributes to JSON format.
"""


class Student:
    """
    Represents a student with a first name, last name, and age.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a new Student instance.

        Args:
            first_name (str): The student's first name.
            last_name (str): The student's last name.
            age (int): The student's age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Returns a dictionary representation of the instance for
        JSON serialization.

        Args:
            A list of attribute names (strings) to include.
            If provided, only these attributes are returned.
            If not a list of strings, the full dictionary is returned.

        Returns:
            A dictionary containing the selected attributes or all attributes.
        """
        if attrs is None:
            return self.__dict__
        else:
            result = {}
            for i in attrs:
                if hasattr(self, i):
                    result[i] = getattr(self, i)
            return result
