"""Bite 24. ABC's and class inheritance."""
from abc import ABC, abstractmethod
from typing import Any, List


class Challenge(ABC):
    """Keep track of a challenge number name."""

    def __init__(self, number: int, title: str) -> None:
        """Construct the abstract object."""
        self.number = number
        self.title = title

    @abstractmethod
    def verify(self, something: Any) -> bool:
        """method docstring."""

    @property
    @abstractmethod
    def pretty_title(self):
        """property docstring."""


class BlogChallenge(Challenge):
    """A Challenge with merged prs."""

    def __init__(self, number: int, title: str, merged_prs: List[int]) -> None:
        """Create the object."""
        super().__init__(number, title)
        self.merged_prs = merged_prs

    def verify(self, pr: int) -> bool:
        """Verify pr in merged_prs."""
        return pr in self.merged_prs

    @property
    def pretty_title(self) -> str:
        """Pretty-print blog challenge."""
        return f"PCC{self.number} - {self.title}"


class BiteChallenge(Challenge):
    """Another Challenge with merged prs."""

    def __init__(self, number: int, title: str, result: str) -> None:
        """Create the object."""
        super().__init__(number, title)
        self.result = result

    def verify(self, result: str) -> bool:
        """Verify result is the bite challenge's result."""
        return result == self.result

    @property
    def pretty_title(self) -> str:
        """Pretty-print bite challenge."""
        return f"Bite {self.number}. {self.title}"
