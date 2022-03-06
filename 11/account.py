"""Bite 11. Enrich a class with dunder methods."""

from typing import List


class Account:
    """Hold an account balance and transactions."""

    def __init__(self, name: str, start_balance: int = 0):
        """Create the object."""
        self.name = name
        self.start_balance = start_balance
        self._transactions: List[int] = []

    @property
    def balance(self) -> int:
        """Calculate the current balance."""
        return self.start_balance + sum(self._transactions)

    # add dunder methods below
