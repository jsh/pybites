#!/usr/bin/env python3
"""Bite 202. Analyze some Bite stats data - part II."""

import csv
import os
from pathlib import Path
from urllib.request import urlretrieve

data = "https://bites-data.s3.us-east-2.amazonaws.com/bite_levels.csv"
TMP = Path(os.getenv("TMP", "/tmp"))
stats = TMP / "bites.csv"

if not stats.exists():
    urlretrieve(data, stats)


def get_most_complex_bites(N=10, stats=stats) -> list[str]:
    """Parse the bites.csv file (= stats variable passed in).

    see example output in the Bite description.
    Return a list of Bite IDs (int or str values are fine) of the N
    most complex Bites.

    output can also be list[int]
    """
    return ["6", "9"]


if __name__ == "__main__":
    res = get_most_complex_bites()
    print(res)
