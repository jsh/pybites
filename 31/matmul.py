"""Bite 31. Matrix multiplication / @ operator."""

from typing import List


class MatrixError(Exception):
    """Matrix object doesn't have the right shape."""


class Matrix(object):
    """Implement matrix object with multiplication."""

    def __init__(self, values: List[List[int]]) -> None:
        """Create Matrix object."""
        self.values = values
        self.validate()

    @property
    def row(self) -> int:
        return len(self.values)

    @property
    def col(self) -> int:
        return len(self.values[0])

    def validate(self) -> None:
        ncol = self.col
        for row in self.values:
            try:
                len(row) == ncol
            except:
                raise MatrixError(f"{row} must have {ncol} elements")
            for elem in row:
                try:
                    isinstance(elem, int)
                except:
                    raise MatrixError(f"{elem} must be int")

    def __repr__(self) -> str:
        """Show the contents."""
        return f'<Matrix values="{self.values}">'

    def __matmul__(self, other: List[List[int]]) -> List[List[int]]:
        """Multiply two matrices."""
        assert self.col == other.row, f"{self.col} must equal {other.row}"

    def __rmatmul__(self, other: List[List[int]]) -> List[List[int]]:
        """Multiply two matrices."""
        assert self.col == other.row, f"{self.col} must equal {other.row}"

    def __imatmul__(self, other: List[List[int]]) -> List[List[int]]:
        """Multiply two matrices."""
        assert self.col == other.row, f"{self.col} must equal {other.row}"
