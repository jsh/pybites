"""Bite 34. Building a Karma app - implement the User class."""

from collections import namedtuple
from datetime import datetime
from typing import List

Transaction = namedtuple("Transaction", "giver points date")
# https://twitter.com/raymondh/status/953173419486359552
Transaction.__new__.__defaults__ = (datetime.now(),)


class User:
    """Represent a user object."""

    def __init__(self, name: str) -> None:
        """Create the object."""
        self.name = name
        self.karma = 0
        self._transactions: List[int] = []

    @property
    def points(self) -> List[int]:
        """List karma points."""
        return self._transactions

    @property
    def fans(self) -> int:
        """Count fans."""
        return 0  # TODO: what is this?

    def __add__(self, trans: Transaction) -> None:
        """Add transactions."""

    def __str__(self) -> str:
        """String representation of User."""
        return f"{self.name} has a karma of {self.points} and {self.fans} fans"
