#!/usr/bin/env python3
"""
Defines mixin classes for swim and fly behaviors,
and a Dragon class that uses both.
Demonstrates the use of mixins for code reuse and behavior composition.
"""


class SwimMixin:
    """
    Mixin class that adds swimming behavior to a class.
    """

    def swim(self):
        """
        Prints a message indicating that the creature can swim.
        """
        print("The creature swims!")


class FlyMixin:
    """
    Mixin class that adds flying behavior to a class.
    """

    def fly(self):
        """
        Prints a message indicating that the creature can fly.
        """
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """
    Represents a dragon that can swim, fly, and roar.
    Inherits swimming and flying behaviors from SwimMixin and FlyMixin.
    """

    def roar(self):
        """
        Prints a message indicating that the dragon is roaring.
        """
        print("The dragon roars!")
