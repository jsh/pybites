"""Bite 158. Subclass the list built-in."""

from typing import List


class IntList(list):
    """Lists of integers that understand mean() and median().

    Raise TypeError for non-int values.
    """

    def __init__(self, elements: List[int] = []) -> None:
        """Create the object."""
        for elem in elements:
            if not isinstance(elem, int):
                raise TypeError
        super().__init__(elements)
