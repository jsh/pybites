"""Bite 248. Test a number guessing game."""
from unittest.mock import patch

import pytest

from guess import MAX_NUMBER, GuessGame, InvalidNumber

# write test code to reach 100% coverage and a 100% mutpy score

def my_input():
	return 2

def test_init() -> None:
    """Unit-test __init__()."""
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
    """Unit-test _validate()."""
    with pytest.raises(InvalidNumber, match=err_msg) as exc:
        game = GuessGame(secret_number)

#@patch("guess.input", side_effect=[1, 3, 2])
@patch("guess.input", my_input)
#@patch("guess.input", side_effect=[1, 3, 2])
def test_call(capsys) -> None:
    """Unit-test __call__()."""
    game = GuessGame(2)
    game()
    captured = capsys.readouterr()
