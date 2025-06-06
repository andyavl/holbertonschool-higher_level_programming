#!/usr/bin/python3
"""
Module that provides a function to convert a Python object to a JSON string.
"""

import json


def to_json_string(my_obj):
    """
    Returns the JSON representation of a Python object as a string.

    Args:
        my_obj (any): The Python object to serialize.

    Returns:
        str: The JSON-formatted string representation of `my_obj`.
    """
    return json.dumps(my_obj)
