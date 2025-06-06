#!/usr/bin/python3
"""
Module that provides a function to save a Python object
to a file in JSON format.
"""

import json


def save_to_json_file(my_obj, filename):
    """
    Writes a Python object to a text file using JSON representation.

    Args:
        my_obj (any): The Python object to serialize (e.g., dict, list).
        filename (str): The name of the file to write the JSON string to.

    Returns:
        int: The number of characters written to the file.
    """
    with open(filename, mode="w", encoding="utf-8") as myFile:
        return myFile.write(json.dumps(my_obj))
