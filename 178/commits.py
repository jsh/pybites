"""Bite 178. Parse PyBites blog git commit log."""

import os
from collections import Counter
from typing import Tuple
from urllib.request import urlretrieve

from dateutil.parser import parse

commits = os.path.join(os.getenv("TMP", "/tmp"), "commits")
urlretrieve("https://bites-data.s3.us-east-2.amazonaws.com/git_log_stat.out", commits)

# you can use this constant as key to the yyyymm:count dict
YEAR_MONTH = "{y}-{m:02d}"


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
