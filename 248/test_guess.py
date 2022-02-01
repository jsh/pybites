"""Bite 248. Test a number guessing game."""
import sys
from unittest.mock import patch

import pytest

from guess import MAX_NUMBER, GuessGame, InvalidNumber

# write test code to reach 100% coverage and a 100% mutpy score


def my_input():
    """Mock input, return 5."""
    return 5


def my_bad_input():
    """Mock bad input."""
    return "FOO"


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
    with pytest.raises(InvalidNumber, match=err_msg):
        GuessGame(secret_number)


@pytest.mark.parametrize(
    "secret_number, expected_output",
    [
        (10, "Guess a number"),
        (10, "Too low"),
        (0, "Too high"),
        (MAX_NUMBER, "Too low"),
        (5, "You guessed it"),
    ],
)
@patch("guess.input", my_input)
def test_call(secret_number, expected_output, capsys) -> None:
    """Unit-test __call__()."""
    game = GuessGame(secret_number, max_guesses=1)
    game()
    out, err = capsys.readouterr()
    assert expected_output in out


@patch("guess.input", return_value=1)
def test_call_too_many_guesses(mock_input, capsys) -> None:
    """Test __call__() with too many guesses."""
    game = GuessGame(1, max_guesses=0)
    game()
    out, err = capsys.readouterr()
    assert out.strip() == "Sorry, the number was 1"


@patch("guess.input", side_effect=["foo"])
def test_call_bad_input(mock_input, capsys) -> None:
    """Test __call__() bad input."""
    game = GuessGame(4)
    with pytest.raises(StopIteration):
        game()
    out, err = capsys.readouterr()
    assert "Enter a number, try again" in out
