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

    def integer_validator(self, name, value):
        """
        Validates that a parameter is a positive integer.

        Args:
            name (str): The name of the parameter.
            value (int): The value to validate.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Represents a square, a special case of a rectangle.
    Inherits from Rectangle.
    """

    def __init__(self, size):
        """
        Initializes a Square instance with equal width and height.

        Args:
            size (int): The size of the square sides.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """
        Calculates the area of the square.
        """
        return self.__size * self.__size
