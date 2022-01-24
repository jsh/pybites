"""Bite 241. Write tests for list_to_decimal."""
from typing import Any, List

import pytest

from numbers_to_dec import list_to_decimal


@pytest.mark.parametrize(
    "numlist, expected_output",
    [
        ([0, 4, 2, 8], 428),
        ([1, 2], 12),
        ([3], 3),
    ],
)
def test_good_input(numlist: List[int], expected_output: int) -> None:
    """Good list returns correct answer."""
    assert list_to_decimal(numlist) == expected_output


@pytest.mark.parametrize(
    "numlist, exception",
    [
        ([6, 4, 2, True], TypeError),
        ([-3, 6], ValueError),
        ([0, 10], ValueError),
        ([3.6, 4, 1], TypeError),
        (["4", 5, 3, 1], TypeError),
    ],
)
def test_exception(numlist: List[Any], exception: type) -> None:
    """Bad list raises correct exception."""
    with pytest.raises(exception):
        assert list_to_decimal(numlist)
