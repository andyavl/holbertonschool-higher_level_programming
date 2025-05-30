#!/usr/bin/env python3
"""
Defines a custom iterator class that counts the number of items iterated.
"""


class CountedIterator:
    """
    Iterator that wraps around any iterable and counts how
    many items have been iterated.
    """

    def __init__(self, iterable):
        """
        Initializes the CountedIterator with the given iterable.

        Args:
            iterable: Any object that implements the iterable protocol.
        """
        self._iterator = iter(iterable)
        self._count = 0

    def __iter__(self):
        """
        Returns the iterator object itself.

        Returns:
            self: The iterator instance.
        """
        return self

    def __next__(self):
        """
        Returns the next item from the iterator and
        increments the internal count.

        Returns:
            The next item from the underlying iterable.

        Raises:
            StopIteration: When there are no more items to return.
        """
        item = next(self._iterator)
        self._count += 1
        return item

    def get_count(self):
        """
        Returns the number of items that have been iterated so far.

        Returns:
            int: The current count of items returned by __next__.
        """
        return self._count
