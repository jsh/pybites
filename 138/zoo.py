"""Bite 138. OOP fun at the Zoo."""

from typing import Dict


class Animal:
    """Animal object."""

    counter = 10000
    animals: Dict[str, int] = {}

    def __init__(self, name: str):
        """Create the object."""
        if name not in Animal.animals:  # let's not have duplicates
            self._name = name
            Animal.counter += 1
            Animal.animals[self._name] = Animal.counter
        else:
            self._name = name

    def __str__(self) -> str:
        """Return 'counter. Name' as a string.

        Like '10006. Horse'
        """
        return f"{self.animals[self._name]}. {self._name.title()}"

    @classmethod
    def zoo(cls):
        """Text list of all animals in zoo.

        Every line is an animal's string representation
        """
        menagerie = []
        for animal in cls.animals:
            menagerie.append(str(cls(animal)))
        return "\n".join(menagerie)
