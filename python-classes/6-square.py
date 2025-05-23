#!/usr/bin/python3
"""Defines a class Square with size and position validation,
area computation, and visual representation.
"""


class Square:
    """Represents a square.

    Attributes:
        __size (int): The size of the square (must be a non-negative integer).
        __position (tuple): A tuple of 2 positive integers representing the
        horizontal and vertical offset when printing the square.
    """

    def __init__(self, size=0, position=(0, 0)):
        """Initializes a new Square instance.

        Args:
            size (int): The size of the square (default is 0).
            position (tuple): The position for printing
            the square (default is (0, 0)).
        """
        self.size = size
        self.position = position

    def area(self):
        """Calculates and returns the area of the square.

        Returns:
            int: The computed area of the square.
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
        """Setter for the size with validation.

        Args:
            value (int): The new size to set.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Getter for the position of the square.

        Returns:
            tuple: The current position (horizontal, vertical offset).
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Setter for the position with validation.

        Args:
            value (tuple): A tuple of 2 positive integers.

        Raises:
            TypeError: If value is not a valid position tuple.
        """
        if (
            not isinstance(value, tuple) or
            len(value) != 2 or
            not all(isinstance(num, int) and num >= 0 for num in value)
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """Prints the square using the '#' character with
        the given position offset.

        If size is 0, prints an empty line.
        """
        if self.__size == 0:
            print()
            return

        for _ in range(self.__position[1]):
            print()

        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
