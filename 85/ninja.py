"""Bite 85. Write a score property."""

from typing import Optional

SCORES = [10, 50, 100, 175, 250, 400, 600, 800, 1000]
RANKS = "white yellow orange green blue brown black paneled red".split()
BELTS = dict(zip(SCORES, RANKS))


class NinjaBelt:
    """Keep track of Ninja belts and points."""

    def __init__(self, score: int = 0) -> None:
        """Create the object."""
        self._score = score
        self._last_earned_belt: Optional[str] = None

    def _get_belt(self, new_score: int) -> Optional[str]:
        """Check to see what belt new_score earns."""
        earned_belt = self._last_earned_belt
        for cutoff, belt in BELTS.items():
            if new_score < cutoff:
                break
            earned_belt = belt
        return earned_belt

    def _get_score(self) -> int:
        """Get the score."""
        return self._score

    def _set_score(self, new_score: int) -> None:
        """Set a new score."""
        if not isinstance(new_score, int):
            raise ValueError("Score takes an int")
        if new_score < self._score:
            raise ValueError("Cannot lower score")
        self._score = new_score
        earned_belt = self._get_belt(new_score)
        if earned_belt == self._last_earned_belt:
            message = f"Set new score to {new_score}"
        else:
            self._last_earned_belt = earned_belt
            message = f"Congrats, you earned {new_score} points"
            if self._last_earned_belt:
                belt = self._last_earned_belt.title()
            message += f" obtaining the PyBites Ninja {belt} Belt"
        print(message)

    score = property(_get_score, _set_score, None, "I am the 'score' property.")
