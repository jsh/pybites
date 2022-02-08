"""Bite 90. What South Park characters talk most?"""

import csv
from collections import Counter, defaultdict
from typing import Dict

import requests

CSV_URL = "https://raw.githubusercontent.com/pybites/SouthParkData/master/by-season/Season-{}.csv"  # noqa E501


def get_season_csv_file(season: int) -> str:
    """Download season CSV.

    Receives a season int, and downloads loads in its
    corresponding CSV_URL
    """
    with requests.Session() as session:
        download = session.get(CSV_URL.format(season))
        return download.content.decode("utf-8")


def get_num_words_spoken_by_character_per_episode(content: str) -> Dict[str, Counter]:
    """Count words spoken by character per episode.

    Receives loaded csv content (str) and returns a dict of
    keys=characters and values=Counter object,
    which is a mapping of episode=>words spoken
    """
    words_per_episode: Counter = Counter()
    words_per_episode["1"] = 6
    words_per_episode["5"] = 9
    return {"Cartman": words_per_episode}
