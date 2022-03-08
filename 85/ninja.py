"""Bite 85. Write a score property."""

scores = [10, 50, 100, 175, 250, 400, 600, 800, 1000]
ranks = "white yellow orange green blue brown black paneled red".split()
BELTS = dict(zip(scores, ranks))


class NinjaBelt:
    """Keep track of Ninja belts and points."""

    def __init__(self, score: int = 0) -> None:
        """Create the object."""
        self._score = score
        self._last_earned_belt = None

    def _get_belt(self, new_score: int) -> str:
        """Might be a useful helper"""

    def _get_score(self) -> int:
        """Get the score."""

    def _set_score(self, new_score: int) -> None:
        """Set a new score."""

    score = property(
        _get_score, _set_score
    )  # TODO: Oh. This is interesting. Look this up.
