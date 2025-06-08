#!/usr/bin/env python3
"""
This module provides utility functions for serializing data to a JSON file
and deserializing data from a JSON file.
"""

import json


def serialize_and_save_to_file(data, filename):
    """
    Serializes a Python object and saves it to a file in JSON format.

    Args:
        data (any): The Python object to serialize.
        filename (str): The name of the file to write the JSON data to.
    """
    with open(filename, "w") as myFile:
        json.dump(data, myFile)


def load_and_deserialize(filename):
    """
    Loads JSON data from a file and deserializes it into a Python object.

    Args:
        filename (str): The name of the file to read from.

    Returns:
        any: The deserialized Python object.
    """
    with open(filename, "r") as myFile:
        return json.load(myFile)
