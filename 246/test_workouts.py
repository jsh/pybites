"""Unit-test workouts.py."""

import pytest

from workouts import print_workout_days


@pytest.mark.parametrize(
    "selector, expected_output",
    [
        ("foo", "No matching workout\n"),
        ("#2", "Thu, Fri\n"),
        ("lower", "Tue, Fri\n"),
        ("card", "Wed\n"),
        (" ", "Mon, Tue, Wed, Thu, Fri\n"),
    ],
)
def test_print_workout_days(selector: str, expected_output: str, capsys) -> None:
    """Unit-test print_workout_days."""
    print_workout_days(selector)
    captured = capsys.readouterr()
    assert captured.out == expected_output
