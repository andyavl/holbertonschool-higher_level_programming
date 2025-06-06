#!/usr/bin/python3
"""
Module that provides a function to convert a JSON string to a Python object.
"""

import json


def from_json_string(my_str):
    """
    Returns the Python object represented by a JSON string.

    Args:
        my_str (str): A string containing a valid JSON document.

    Returns:
        any: The Python data structure represented by the JSON string.
    """
    return json.loads(my_str)
