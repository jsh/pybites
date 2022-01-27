"""Unit-test color."""
from unittest.mock import patch

import pytest

import color


@pytest.fixture(scope="module")
def gen() -> str:
    return color.gen_hex_color()


def my_sample(range_in, num):
    # mock for sample()
    correct_range = range(0, 256)
    if range_in != correct_range:
        raise ValueError(f"{range_in} must be range(0, 256)")
    if num != 3:
        raise ValueError(f"{num} must be 3")
    return 1, 2, 3


@patch("color.sample", my_sample)
def test_gen_hex_color(gen) -> None:
    """Unit-test gen_hex_color."""
    out = next(gen)
    print(out)
    assert out == "#010203"
    out = next(gen)
    print(out)
    assert next(gen) == "#010203"
