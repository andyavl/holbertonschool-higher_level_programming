#!/usr/bin/python3
"""
Module that defines a function to append text to a file.
"""


def append_write(filename="", text=""):
    """
    Appends a string to the end of a text file (UTF-8) and returns
    the number of characters added.

    Args:
        filename (str): The name of the file to append to.
        text (str): The string to append to the file.

    Returns:
        int: The number of characters written.

    Notes:
        - If the file does not exist, it will be created.
        - Existing content in the file is preserved.
    """
    with open(filename, mode="a", encoding="UTF8") as myFile:
        return myFile.write(text)
