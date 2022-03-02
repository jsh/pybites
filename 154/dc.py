"""Bite 154. Write your own Data Class."""

from dataclasses import dataclass


@dataclass(order=True)
class Bite:
    """Class for keeping track of a Bite."""

    number: int
    title: str
    level: str = "Beginner"

    def __post_init__(self):
        """Capitalize Bite title."""
        self.title = self.title.capitalize()
