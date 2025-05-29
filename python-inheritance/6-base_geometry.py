#!/usr/bin/python3
"""
Defines a base class for geometry operations.
"""


class BaseGeometry:
    """
    Base class for geometry-related classes.
    """

    def area(self):
        """
        Raises an exception indicating that area() is not implemented.
        """
        raise Exception("area() is not implemented")
