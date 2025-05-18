#!/usr/bin/python3
"""
This module provides a function that adds two numbers.
Only integers and floats are accepted as input.
Floats are cast to integers before the addition.
If the input is invalid, a TypeError is raised.
The result is returned as an integer.
"""


def add_integer(a, b=98):
    """
    Adds two integers or floats after casting.
    Raises a TypeError if the inputs are not int or float.
    Returns the sum as an integer.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
