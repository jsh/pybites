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
    def __len__(self):
        """Return # of transactions."""
        return len(self._transactions)

    def __str__(self):
        """Report the account name and balance."""
        return f"{self.name} account - balance: {self.balance}"

    def __add__(self, summand):
        """Add money."""
        if not isinstance(summand, int):
            raise TypeError
        self._transactions.append(summand)

    def __sub__(self, subtrahend):
        """Subtract money."""
        if not isinstance(subtrahend, int):
            raise TypeError
        self._transactions.append(-1 * subtrahend)

    def __getitem__(self, index):
        """Index into the transactions."""
        return self._transactions[index]

    def __gt__(self, other):
        """Left balance gt right."""
        return self.balance > other.balance

    def __ge__(self, other):
        """Left balance ge right."""
        return self.balance >= other.balance

    def __lt__(self, other):
        """Left balance lt right."""
        return self.balance < other.balance

    def __le__(self, other):
        """Left balance le right."""
        return self.balance <= other.balance

    def __eq__(self, other):
        """Left balance == right."""
        return self.balance == other.balance
