#!/usr/bin/python3
"""
Module that defines a function to write text to a file.
"""


def write_file(filename="", text=""):
    """
    Writes a string to a text file (UTF-8) and returns the
    number of characters written.

    Args:
        filename (str): The name of the file to write to.
        text (str): The string to write into the file.

    Returns:
        int: The number of characters written to the file.

    Notes:
        - If the file already exists, its content will be overwritten.
        - If the file does not exist, it will be created.
    """
    with open(filename, mode="w", encoding="UTF8") as myFile:
        return myFile.write(text)
