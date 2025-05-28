#!/usr/bin/python3
"""
Defines a class MyList that inherits from the built-in list.
"""


class MyList(list):
    """
    A subclass of list that includes a method to print list in sorted order.
    """

    def print_sorted(self):
        """
        Prints the list in ascending sorted order (does not modify the list).
        """
        print(sorted(self))
