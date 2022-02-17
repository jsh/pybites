"""Bite 184. Analyze some Bite stats data."""

import os
from csv import DictReader
from urllib.request import urlretrieve

TMP = os.getenv("TMP", "/tmp")
LOGS = "bite_output_log.txt"
DATA = os.path.join(TMP, LOGS)
S3 = "https://bites-data.s3.us-east-2.amazonaws.com"
if not os.path.isfile(DATA):
    urlretrieve(f"{S3}/{LOGS}", DATA)


class BiteStats:
    """Get statistics on Pybites data."""

    def _load_data(self, data) -> list:
        """Resolve data into rows."""
        return []

    def __init__(self, data=DATA):
        """Save data in instance local."""
        self.rows = self._load_data(data)

    @property
    def number_bites_accessed(self) -> int:
        """Get the number of unique Bites accessed."""

    @property
    def number_bites_resolved(self) -> int:
        """Get the number of unique Bites resolved (completed=True)."""

    @property
    def number_users_active(self) -> int:
        """Get the number of unique users in the data set."""

    @property
    def number_users_solving_bites(self) -> int:
        """Get the number of unique users that resolved one or more Bites."""

    @property
    def top_bite_by_number_of_clicks(self) -> str:
        """Get the Bite that got accessed the most (= in most rows)."""

    @property
    def top_user_by_bites_completed(self) -> str:
        """Get the user that completed the most Bites."""


if __name__ == "__main__":
    print(BiteStats().rows)
