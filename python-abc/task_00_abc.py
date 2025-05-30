#!/usr/bin/env python3
"""
Defines an abstract Animal class and its concrete subclasses Dog and Cat.
"""

from abc import ABC, abstractmethod


class Animal(ABC):
    """
    Abstract base class representing an animal.
    """

    @abstractmethod
    def sound(self):
        """
        Abstract method to be implemented by subclasses.
        Should return the sound made by the animal.
        """
        pass


class Dog(Animal):
    """
    Concrete class representing a dog, inherits from Animal.
    """

    def sound(self):
        """
        Returns the sound a dog makes.
        """
        return "Bark"


class Cat(Animal):
    """
    Concrete class representing a cat, inherits from Animal.
    """

    def sound(self):
        """
        Returns the sound a cat makes.
        """
        return "Meow"
