"""Bite 34. Building a Karma app - implement the User class."""

from collections import namedtuple
from datetime import datetime
from typing import List

# Transaction = namedtuple("Transaction", "giver points date")
# https://twitter.com/raymondh/status/953173419486359552
# Transaction.__new__.__defaults__ = (datetime.now(),)
Transaction = namedtuple("Transaction", "giver points date", defaults=(datetime.now(),))


class User:
    """Represent a user object."""

    def __init__(self, name: str) -> None:
        """Create the object."""
        self.name = name
        self.karma = 0
        self._transactions: List[Transaction] = []

    @property
    def points(self) -> List[int]:
        """List karma points."""
        return [transaction.points for transaction in self._transactions]

    @property
    def fans(self) -> int:
        """Count fans."""
        fans = {transaction.giver for transaction in self._transactions}
        return len(fans)

    def __add__(self, transaction: Transaction) -> None:
        """Add transactions."""
        self._transactions.append(transaction)
        self.karma += transaction.points

    def __str__(self) -> str:
        """String representation of User."""
        return f"{self.name} has a karma of {self.karma} and {self.fans} fan" + (
            "s" if self.fans > 1 else ""
        )
