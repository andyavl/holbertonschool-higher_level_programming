#!/usr/bin/python3
"""
Defines a function that checks if an object is an inherited
instance of a class.
"""


def inherits_from(obj, a_class):
    """
    Returns True if obj is an instance of a subclass of a_class,
    otherwise False.
    """
    if isinstance(obj, a_class) and type(obj) is not a_class:
        return True
    else:
        return False
