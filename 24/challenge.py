"""Bite 24. ABC's and class inheritance."""
from abc import ABC, abstractmethod
from typing import List


class Challenge(ABC):
    """Keep track of a challenge number name."""

    def __init__(self, number: int, title: str) -> None:
        """Construct the abstract object."""
        self.number = number
        self.title = title

    @abstractmethod
    def verify(self):
        """method docstring."""

    @property
    def pretty_title(self):
        """property docstring."""


class BlogChallenge(Challenge):
    """A Challenge with merged prs."""

    def __init__(self, number: int, title: str, prs: List[int]) -> None:
        """Create the object."""
        super().__init__(number, title)
        self.prs = prs


class BiteChallenge(Challenge):
    """Another Challenge with merged prs."""

    def __init__(self, number: int, title: str, prs: List[int]) -> None:
        """Create the object."""
        super().__init__(number, title)
        self.prs = prs
