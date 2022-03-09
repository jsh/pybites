"""Bite 158. Subclass the list built-in."""

import decimal
import statistics
from typing import Any, List


def validate(elem) -> None:
    """Ensure the element is arithmetic.

    Raise a TypeError if not.
    """
    if not isinstance(elem, (int, float, decimal.Decimal)):
        raise TypeError


def validate_list(elems: List[Any]) -> bool:
    """Ensure all list elements are arithmetic."""
    for elem in elems:
        validate(elem)
    return True


class IntList(list):
    """Lists of integers that understand mean() and median().

    Raise TypeError for non-int values.
    """

    def __init__(self, elements: List[int]) -> None:
        """Create the object."""
        for elem in elements:
            validate(elem)
        super().__init__(elements)

    def append(self, elem):
        """Append a new element."""
        validate(elem)
        super().append(elem)

    def __iadd__(self, other):
        """In-place add a list."""
        validate_list(other)
        return super().__iadd__(other)

    def __add__(self, other):
        """Add two lists."""
        validate_list(other)
        return super().__add__(other)

    @property
    def mean(self) -> float:
        """Calculate the mean."""
        float_list = [float(elem) for elem in self]
        return statistics.mean(float_list)

    @property
    def median(self) -> int:
        """Calculate the median."""
        return statistics.median(self)
