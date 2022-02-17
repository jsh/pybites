#!/usr/bin/env python3
"""Bite 178. Parse PyBites blog git commit log."""

import os
import re
from collections import Counter
from typing import Tuple
from urllib.request import urlretrieve

from collections import defaultdict, Counter
from dateutil.parser import parse

commits = os.path.join(os.getenv("TMP", "/tmp"), "commits")
urlretrieve("https://bites-data.s3.us-east-2.amazonaws.com/git_log_stat.out", commits)

# you can use this constant as key to the yyyymm:count dict
YEAR_MONTH = "{y}-{m:02d}"


def tot_changes(changes: str) -> int:
    """Add deletions and insertions."""

    insertions_pat = re.compile(r"(\d+) insertion")
    deletions_pat = re.compile(r"(\d+) deletion")

    insertions = insertions_pat.search(changes)
    insertions = int(insertions.group(1)) if insertions else 0
    deletions = deletions_pat.search(changes)
    deletions = int(deletions.group(1)) if deletions else 0
    return insertions + deletions


def get_min_max_amount_of_commits(
    commit_log: str = commits, year: int = None
) -> Tuple[str, str]:
    """Get the months with fewest and most commits.

    Calculate the amount of inserts / deletes per month from the
    provided commit log.

    Takes optional year arg, if provided only look at lines for
    that year, if not, use the entire file.

    Returns a tuple of (least_active_month, most_active_month)
    """
    log_pat = re.compile(r"\S+:\s+(.*)\s+\|\s+.*changed, (.*)$")
    # 31 insertions(+), 2 deletions(-)
    nchanges_per_month = defaultdict(int)
    with open(commit_log, encoding="utf-8") as f_in:
        for line in f_in:
            match = log_pat.match(line)
            date, changes = match.group(1, 2)
            ym_date = parse(date).strftime("%Y-%m")
            if year and ym_date[:4] != year:
                continue
            nchanges = tot_changes(changes)
            nchanges_per_month[ym_date] += nchanges
        nchanges_per_month = Counter(nchanges_per_month)
        least = nchanges_per_month.most_common()[-1]
        most = nchanges_per_month.most_common(1)[0]
        return (least[0], most[0])


if __name__ == "__main__":
    get_min_max_amount_of_commits(year="2019")
