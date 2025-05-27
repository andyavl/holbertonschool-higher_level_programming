#!/usr/bin/python3
"""
This module defines a single function: `lookup`.

The function provides introspection capabilities by returning
a list of the available attributes and methods of a given object.
"""


def lookup(obj):
    """
    Returns the list of available attributes and methods of an object.

    Args:
        obj: The object to inspect.

    Returns:
        list: A list of strings containing the names of the attributes
              and methods available for the object.
    """
    return dir(obj)
