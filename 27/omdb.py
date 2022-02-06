#!/usr/bin/env python3
"""Bite 27. Parse omdb movie json data."""

import json
import os
from pathlib import Path
from typing import Dict, List
from urllib.request import urlretrieve


def retrieve_json():
    """Retrieve the json to see what it looks like."""
    tmp = Path(os.getenv("TMP", "/tmp"))
    s3 = "https://bites-data.s3.us-east-2.amazonaws.com/"
    data = "omdb_data"

    data_local = tmp / data
    if not Path(data_local).exists():
        urlretrieve(s3 + data, data_local)


def get_movie_data(files: list) -> List[Dict]:
    """Parse movie json files into a list of dicts."""
    return []


def get_single_comedy(movies: list) -> str:
    """Return the movie with Comedy in Genres."""
    return ""


def get_movie_most_nominations(movies: list) -> str:
    """Return the movie that had the most nominations."""
    return ""


def get_movie_longest_runtime(movies: list) -> str:
    """Return the movie that has the longest runtime."""
    return ""

if __name__ == "__main__":
    print("hello")
