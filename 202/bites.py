#!/usr/bin/env python3
"""Bite 202. Analyze some Bite stats data - part II."""

import csv
import os
import re
from pathlib import Path
from typing import Dict
from urllib.request import urlretrieve

data = "https://bites-data.s3.us-east-2.amazonaws.com/bite_levels.csv"
TMP = Path(os.getenv("TMP", "/tmp"))
stats = TMP / "bites.csv"

if not stats.exists():
    urlretrieve(data, stats)


def difficulty(row: Dict[str, str]) -> float:
    """Get difficulty from row."""
    return float(row["Difficulty"])


def get_most_complex_bites(N=10, stats=stats) -> list[str]:
    """Parse the bites.csv file (= stats variable passed in).

    see example output in the Bite description.
    Return a list of Bite IDs (int or str values are fine) of the N
    most complex Bites.

    output can also be list[int]
    """
    with open(stats, encoding="utf-8-sig") as cvsfile:
        reader = csv.DictReader(cvsfile, delimiter=";")
        rows = [row for row in reader if row["Difficulty"] != "None"]
    bites = sorted(rows, key=difficulty, reverse=True)
    hardest = [bite["Bite"] for bite in bites[:N]]
    pat = re.compile(r"Bite (\d+)\. .*")
    hardest_list = []
    for bite in hardest:
        match = pat.match(bite)
        if match and match[1]:
            hardest_list.append(match[1])
    return hardest_list


if __name__ == "__main__":
    print(get_most_complex_bites(4))
