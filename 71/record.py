"""Bite 71. Keep state in a class + make its instance callable."""


class RecordScore:
    """Class to track a game's maximum score."""

    def __init__(self):
        """Create RecordScore object."""
        self.record_score = None

    def __call__(self, score: int) -> int:
        """If score is higher than current record_score, reset to score."""
        if (self.record_score is None) or (score > self.record_score):
            self.record_score = score
        return self.record_score
