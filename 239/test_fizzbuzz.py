"""Bite 239. Test FizzBuzz."""

from typing import Any

import pytest

from fizzbuzz import fizzbuzz

# write one or more pytest functions below, they need to start with test_


@pytest.mark.parametrize(
    "integer, expected_output",
    [
        (3, "Fizz", "divisible by three"),
        (5, "Buzz", "divisible by five"),
        (15, "Fizz Buzz", "divisible by both"),
        (7, 7, "divisible by neither"),
        (0, "Fizz Buzz", "zero"),
        (-5, "Buzz", "negative number"),
    ],
)
def test_fizzbuzz(integer: int, expected_output: str) -> None:
    """Unit-test fizzbuzz."""
    assert fizzbuzz(integer) == expected_output


@pytest.mark.parametrize(
    "bad_input, expected_exception",
    [
        ("foo", TypeError),
    ],
)
def test_invalid_input(bad_input: Any, expected_exception) -> None:
    """Check bad input."""
    with pytest.raises(expected_exception):
        assert fizzbuzz(bad_input)
