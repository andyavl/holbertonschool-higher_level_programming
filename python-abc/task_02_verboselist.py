#!/usr/bin/env python3
"""
This module defines a custom list class `VerboseList`
that extends Python's built-in list.
"""


class VerboseList(list):
    """
    A subclass of the built-in list that provides verbose output
    whenever elements are added or removed. It overrides append,
    extend, remove, and pop methods to print informative messages.
    """
    def append(self, item):
        """
        Adds a single item to the end of the list and prints a message.

        Args:
            item: The item to append.
        """
        super().append(item)
        print("Added [{}] to the list.".format(item))

    def extend(self, item):
        """
        Adds all elements from the iterable to the end of
        the list and prints a message.

        Args:
            item (iterable): An iterable of items to extend the list with.
        """
        super().extend(item)
        print("Extended the list with [{}] items.".format(len(item)))

    def remove(self, item):
        """
        Removes the first occurrence of the item from the list
        and prints a message.

        Args:
            item: The item to remove.

        Raises:
            ValueError: If the item is not in the list.
        """
        super().remove(item)
        print("Removed [{}] from the list.".format(item))

    def pop(self, index=-1):
        """
        Removes and returns the item at the given position in the list.
        If no index is specified, removes and returns the last item.
        Prints a message about the item removed.

        Args:
            index (int, optional): The index of the item to remove.
            Defaults to -1.

        Returns:
            The item that was removed.
        """
        item = super().pop(index)
        print("Popped [{}] from the list.".format(item))
        return item
