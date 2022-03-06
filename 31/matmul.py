"""Bite 31. Matrix multiplication / @ operator."""

from typing import List


class Matrix(object):
    """Implement matrix object with multiplication."""

    def __init__(self, values: List[List[int]]) -> None:
        """Create Matrix object."""
        self.values = values

    def __repr__(self) -> str:
        """Show the contents."""
        return f'<Matrix values="{self.values}">'
