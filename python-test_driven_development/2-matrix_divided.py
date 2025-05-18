#!/usr/bin/python3
"""
This module provides a function that divides all elements of a matrix.
Only lists of integers or floats are accepted as a matrix.
All rows must be of equal size and div must be a number.
Each result is rounded to 2 decimal places.
Raises an error for invalid input or division by zero.
"""


def matrix_divided(matrix, div):
    """
    Divides all matrix elements by div and returns a new matrix.
    Checks for valid input types and uniform row sizes.
    Raises TypeError or ZeroDivisionError on invalid input.
    Results are rounded to 2 decimal places.
    """
    div_matrix = []

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    row_length = len(matrix[0])
    for i in range(len(matrix)):
        if len(matrix[i]) != row_length:
            raise TypeError(
                "Each row of the matrix must have the same size"
            )
        for j in range(len(matrix[i])):
            if not isinstance(matrix[i][j], (int, float)):
                raise TypeError(
                    "matrix must be a matrix (list of lists) "
                    "of integers/floats"
                )

    for i in range(len(matrix)):
        row = []
        for j in range(len(matrix[i])):
            row.append(round(matrix[i][j] / div, 2))
        div_matrix.append(row)

    return div_matrix
