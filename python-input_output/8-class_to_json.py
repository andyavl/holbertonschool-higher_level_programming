#!/usr/bin/python3
"""
Module that provides a function to convert an object to a JSON-serializable dictionary.
"""


def class_to_json(obj):
    """
    Returns the dictionary description of an object.

    This function is typically used to prepare data for JSON serialization.

    Args:
        obj: An instance of a class with serializable attributes.

    Returns:
        dict: A dictionary containing all the serializable attributes of the object.
    """
    return obj.__dict__
