"""Bite 184. Analyze some Bite stats data."""

import os
from collections import Counter, defaultdict
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
        with open(data, encoding="utf-8") as csvfile:
            rows = list(DictReader(csvfile))
        return rows

    def __init__(self, data=DATA):
        """Save data in instance local."""
        self.rows = self._load_data(data)

    def resolved(self) -> list:
        """Return rows completed."""
        completed_rows = [row for row in self.rows if row["completed"] == "True"]
        return completed_rows

    @property
    def number_bites_accessed(self) -> int:
        """Get the number of unique Bites accessed."""
        bites = {row["bite"] for row in self.rows}
        return len(bites)

    @property
    def number_bites_resolved(self) -> int:
        """Get the number of unique Bites resolved (completed=True)."""
        resolved = self.resolved()
        bites = {row["bite"] for row in resolved}
        return len(bites)

    @property
    def number_users_active(self) -> int:
        """Get the number of unique users in the data set."""
        users = {row["user"] for row in self.rows}
        return len(users)

    @property
    def number_users_solving_bites(self) -> int:
        """Get the number of unique users that resolved one or more Bites."""
        resolved = self.resolved()
        users = {row["user"] for row in resolved}
        return len(users)

    @property
    def top_bite_by_number_of_clicks(self) -> str:
        """Get the Bite that got accessed the most (= in most rows)."""
        naccesses: defaultdict = defaultdict(int)
        for row in self.rows:
            bite = row["bite"]
            naccesses[bite] += 1
        count_accesses = Counter(naccesses)
        most_common = count_accesses.most_common(1).pop()
        bite = most_common[0]
        return bite

    @property
    def top_user_by_bites_completed(self) -> str:
        """Get the user that completed the most Bites."""
        rows = self.resolved()
        completed: defaultdict = defaultdict(int)
        for row in rows:
            user = row["user"]
            completed[user] += 1
        count_completed = Counter(completed)
        most_common = count_completed.most_common(1).pop()
        user = most_common[0]
        return user
