#!/usr/bin/python3
"""Defines a class Rectangle with width and height validation,
and methods to compute area and perimeter.
"""


class Rectangle:
    """Represents a rectangle.

    The width and height are private instance attributes with proper validation
    using property getters and setters.

    Attributes:
        __width (int): The width of the rectangle (must be >= 0).
        __height (int): The height of the rectangle (must be >= 0).
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initializes a new Rectangle instance.

        Args:
            width (int): The width of the rectangle (default is 0).
            height (int): The height of the rectangle (default is 0).
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Getter for the width of the rectangle.

        Returns:
            int: The current width.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for the width with validation.

        Args:
            value (int): The new width to set.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter for the height of the rectangle.

        Returns:
            int: The current height.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for the height with validation.

        Args:
            value (int): The new height to set.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Computes the area of the rectangle.

        Returns:
            int: The area (width * height).
        """
        return self.height * self.width

    def perimeter(self):
        """Computes the perimeter of the rectangle.

        Returns:
            int: The perimeter (2 * (width + height)), or 0 if
            either width or height is 0.
        """
        if self.height == 0 or self.width == 0:
            return 0
        return 2 * (self.height + self.width)

    def __str__(self):
        """Returns a string representation of the rectangle
        using '#' characters.

        Returns:
            str: The rectangle represented by lines of
            the 'print_symbol' characters.
                 If width or height is 0, returns an empty string.
        """
        if self.width == 0 or self.height == 0:
            return ""
        lines = []
        for _ in range(self.height):
            lines.append(Rectangle.print_symbol * self.width)
        return "\n".join(lines)

    def __repr__(self):
        """Return a string representation of the rectangle.

        Returns:
            str: A string in the format 'Rectangle(width, height)'.
        """
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """Prints a message when a Rectangle instance is deleted.

        This method is called automatically when an instance
        is about to be destroyed.

        Side effect:
            Prints 'Bye rectangle...' to the standard output.
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
