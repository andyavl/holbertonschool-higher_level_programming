#!/usr/bin/python3
"""
This module provides a function to generate Pascal's Triangle
up to a given number of rows.
"""


def pascal_triangle(n):
    """
    Generates Pascal's Triangle up to the nth row.

    Pascal's Triangle is a triangular array where each number
    is the sum of the two numbers directly above it.

    Args:
        n (int): The number of rows of the triangle to generate.

    Returns:
        list of lists: A list containing `n` lists, each representing a row
        of Pascal's Triangle. Returns an empty list if n <= 0.
    """
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(n - 1):
        prev_row = triangle[-1]
        new_row = [1]

        for j in range(len(prev_row) - 1):
            new_row.append(prev_row[j] + prev_row[j + 1])

        new_row.append(1)
        triangle.append(new_row)

    return triangle
