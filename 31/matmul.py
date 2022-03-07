"""Bite 31. Matrix multiplication / @ operator."""

from typing import List


class MatrixError(Exception):
    """Matrix object has a problem."""


class Matrix:
    """Implement matrix object with multiplication."""

    def __init__(self, values: List[List[int]]) -> None:
        """Create Matrix object."""
        self.values = values
        self.validate()

    @property
    def row(self) -> int:
        """Number of rows."""
        return len(self.values)

    @property
    def col(self) -> int:
        """Number of columns."""
        return len(self.values[0])

    def validate(self) -> None:
        """Sanity-check the matrix."""
        ncol = self.col
        for row in self.values:
            if len(row) != ncol:
                raise MatrixError(f"{row} must have {ncol} elements")
            for elem in row:
                if not isinstance(elem, int):
                    raise MatrixError(f"{elem} must be int")

    def __repr__(self) -> str:
        """Show the contents."""
        return f'<Matrix values="{self.values}">'

    @staticmethod
    def scalar_prod(scalar: int, vector: List[int]) -> List[int]:
        """A simple, scalar product: scalar*vector."""
        return [scalar * coeff for coeff in vector]

    @staticmethod
    def linear_combo(scalars: List[int], vectors: List[List[int]]) -> List[int]:
        """Linear combination of vectors using scalar factors."""
        # sanity checks
        size = len(vectors[0])
        assert len(scalars) == len(
            vectors
        ), f"{scalars} must have same number of elements as {vectors}"
        for vector in vectors:
            assert len(vector) == size, f"vector {vector} must have length {size}"
        # now the linear combination
        lin_comb = [0] * size
        for scalar, vector in zip(scalars, vectors):
            scp = Matrix.scalar_prod(scalar, vector)
            lin_comb = [a + b for a, b in zip(lin_comb, scp)]
        return lin_comb

    def __matmul__(self, other: "Matrix") -> "Matrix":
        """Multiply two matrices.

        Each row in product is a linear combinations of rows in other.
        """
        assert self.col == other.row, f"{self.col} must equal {other.row}"
        product = []
        for s_row in self.values:
            product.append(Matrix.linear_combo(s_row, other.values))
        return Matrix(product)

    def __rmatmul__(self, other: "Matrix") -> "Matrix":
        """Multiply two matrices, reversed."""
        assert self.row == other.col, f"{self.col} must equal {other.row}"
        return self.__matmul__(other)

    def __imatmul__(self, other: "Matrix") -> "Matrix":
        """Multiply two matrices."""
        assert self.col == other.row, f"{self.col} must equal {other.row}"
        product = self.__matmul__(other)
        self.values = product.values
        return self
