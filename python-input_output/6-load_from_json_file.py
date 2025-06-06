#!/usr/bin/python3
"""
Module that provides a function to load a Python object from a JSON file.
"""

import json


def load_from_json_file(filename):
    """
    Creates a Python object from a JSON file.

    Args:
        filename (str): The path to the JSON file.

    Returns:
        object: The Python object created from the JSON file.
    """
    with open(filename, mode="r", encoding="utf-8") as myFile:
        return json.load(myFile)
