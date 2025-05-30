#!/usr/bin/env python3
"""
Defines animal classes: Fish, Bird, and a FlyingFish that inherits from both.
Demonstrates method overriding and multiple inheritance.
"""


class Fish:
    """
    Represents a fish with swimming behavior and a water-based habitat.
    """

    def swim(self):
        """
        Prints a message indicating the fish is swimming.
        """
        print("The fish is swimming")

    def habitat(self):
        """
        Prints a message describing the habitat of the fish.
        """
        print("The fish lives in water")


class Bird:
    """
    Represents a bird with flying behavior and a sky-based habitat.
    """

    def fly(self):
        """
        Prints a message indicating the bird is flying.
        """
        print("The bird is flying")

    def habitat(self):
        """
        Prints a message describing the habitat of the bird.
        """
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """
    Represents a flying fish, which can both swim and fly.
    Inherits behaviors from both Fish and Bird.
    """

    def fly(self):
        """
        Prints a message indicating the flying fish is soaring through the air.
        Overrides Bird's fly method.
        """
        print("The flying fish is soaring!")

    def swim(self):
        """
        Prints a message indicating the flying fish is swimming.
        Overrides Fish's swim method.
        """
        print("The flying fish is swimming!")

    def habitat(self):
        """
        Prints a message describing the dual habitat of the flying fish.
        Overrides both Fish and Bird habitat methods.
        """
        print("The flying fish lives both in water and the sky!")
