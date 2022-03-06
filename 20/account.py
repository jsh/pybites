"""Bite 20. Write a context manager."""


class Account:
    """Represent an account with transactions."""

    def __init__(self):
        """Create the object."""
        self._transactions = []

    @property
    def balance(self) -> int:
        """Report the balance."""
        return sum(self._transactions)

    def __add__(self, amount: int):
        """Add a transaction."""
        self._transactions.append(amount)

    def __sub__(self, amount: int):
        """Subtract a transaction."""
        self._transactions.append(-amount)

    # add 2 dunder methods here to turn this class
    # into a 'rollback' context manager
