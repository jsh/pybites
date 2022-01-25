"""Bite 239. Test FizzBuzz."""

from typing import Any

import pytest

from fizzbuzz import fizzbuzz


@pytest.mark.parametrize(
    "integer, expected_output",
    [
        pytest.param(3, "Fizz", id="divisible by three"),
        pytest.param(5, "Buzz", id="divisible by five"),
        pytest.param(15, "Fizz Buzz", id="divisible by both"),
        pytest.param(7, 7, id="divisible by neither"),
        pytest.param(0, "Fizz Buzz", id="zero"),
        pytest.param(-5, "Buzz", id="negative number"),
    ],
)
def test_fizzbuzz(integer: int, expected_output: Any) -> None:
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
