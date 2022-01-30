"""Bite 248. Test a number guessing game."""
from unittest.mock import patch

import pytest

from guess import MAX_NUMBER, GuessGame, InvalidNumber

# write test code to reach 100% coverage and a 100% mutpy score


def test_dummy() -> None:
    pass


def test_init() -> None:
    game = GuessGame(1)
    assert game.secret_number == 1
    assert game.max_guesses == 5
    assert game.attempt == 0


@pytest.mark.parametrize(
    "secret_number, err_msg",
    [
        ("foo", "Not a number"),
        (-1, "Negative number"),
        (MAX_NUMBER + 1, "Number too high"),
    ],
)
def test_validate(secret_number, err_msg) -> None:
    with pytest.raises(InvalidNumber) as exc:
        game = GuessGame(secret_number)
    assert err_msg in str(exc)


def test_call() -> None:
    game = GuessGame(1)
    # game()
