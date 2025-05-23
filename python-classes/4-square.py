#!/usr/bin/python3
"""Defines a class Square with size validation,
    area computation, and accessors."""


class Square:
    """Represents a square.

    The size of the square is stored as a private attribute to enforce control
    over its value using getter and setter methods.

    Attributes:
        __size (int): The size of the square (must be a non-negative integer).
    """

    def __init__(self, size=0):
        """Initializes a new Square instance. Uses the setter for validation

        Args:
            size (int): The size of the square (default is 0).
        """
        self.size = size

    def area(self):
        """Calculates and returns the area of the square.

        Returns:
            int: The computed area (size * size).
        """
        return self.__size * self.__size

    @property
    def size(self):
        """Getter for the size of the square.

        Returns:
            int: The current size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Setter for the size of the square with validation.

        Args:
            value (int): The new size to set.

        Raises:
            TypeError: If the new size is not an integer.
            ValueError: If the new size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
