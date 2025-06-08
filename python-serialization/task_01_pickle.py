#!/usr/bin/env python3
"""
This module defines a CustomObject class that supports serialization
and deserialization using the pickle module.
"""

import pickle


class CustomObject:
    """
    Represents a custom object with a name, age, and student status.

    This class provides methods to display its attributes,
    serialize itself to a binary file, and deserialize itself from a file.
    """

    def __init__(self, name, age, is_student):
        """
        Initializes a new CustomObject instance.

        Args:
            name (str): The name of the person.
            age (int): The age of the person.
            is_student (bool): Indicates if the person is a student.
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """
        Prints the attributes of the object in a readable format.
        """
        print(f"Name: {self.name}\nAge: {self.age}\n"
              f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """
        Serializes the object and saves it to a binary file using pickle.

        Args:
            filename (str): The name of the file to save the object to.
        """
        with open(filename, "wb") as myFile:
            pickle.dump(self, myFile)

    @classmethod
    def deserialize(cls, filename):
        """
        Loads and returns a CustomObject instance from a binary file.

        Args:
            filename (str): The name of the file to read from.

        Returns:
            CustomObject or None: The deserialized object if successful,
            or None if the file is not found or contains invalid data.
        """
        try:
            with open(filename, "rb") as myFile:
                return pickle.load(myFile)
        except (FileNotFoundError, pickle.UnpicklingError):
            return None
