#!/usr/bin/python3
"""
Module that defines a simple file-reading function.
"""


def read_file(filename=""):
    """
    Reads the contents of a text file (UTF-8 encoding) and prints it to stdout.

    Args:
        filename (str): The path to the file to be read.
    """
    with open(filename, encoding="UTF8") as myFile:

        print(myFile.read(), end="")
