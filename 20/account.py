"""Bite 20. Write a context manager."""

from typing import List


class Account:
    """Represent an account with transactions."""

    def __init__(self) -> None:
        """Create the object."""
        self._transactions: List[int] = []

    @property
    def balance(self) -> int:
        """Report the balance."""
        return sum(self._transactions)

    def __add__(self, amount: int) -> None:
        """Add a transaction."""
        self._transactions.append(amount)

    def __sub__(self, amount: int) -> None:
        """Subtract a transaction."""
        self._transactions.append(-amount)

    # add 2 dunder methods here to turn this class
    # into a 'rollback' context manager

    def __enter__(self) -> "Account":
        """Save transaction history on entrance to context mgr."""
        self._save_transactions = self._transactions.copy()
        return self

    def __exit__(self, exc_type, exc_value, traceback) -> None:
        """Restore transaction history on context mgr exit if balance < 0."""
        if self.balance < 0:
            self._transactions = self._save_transactions
