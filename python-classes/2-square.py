#!/usr/bin/python3
"""Defines a class Square with size validation."""


class Square:
    """Represents a square.

    Attributes:
        __size (int): The size of the square (private).
        Must be a non-negative integer.
    """

    def __init__(self, size=0):
        """Initializes a new Square.

        Args:
            size (int): The size of the square (default is 0).

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
