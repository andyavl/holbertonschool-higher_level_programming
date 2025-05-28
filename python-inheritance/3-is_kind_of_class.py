#!/usr/bin/python3
"""
Defines a function that checks if an object is an instance
or inherits from a specified class.
"""


def is_kind_of_class(obj, a_class):
    """
    Returns True if obj is an instance of a_class or a subclass,
    otherwise False.
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
