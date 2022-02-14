"""Bite 90. What South Park characters talk most?"""
# pylint: disable=line-too-long

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
    csv_lines = content.splitlines()
    csv_reader = csv.DictReader(csv_lines)
    words = defaultdict(list)
    for row in csv_reader:
        character = row["Character"]
        episode = row["Episode"]
        nwords = len(row["Line"].split())
        words[character].append((episode, nwords))

    words_per_character_by_episode = {}
    for character in words:
        words_per_episode: defaultdict = defaultdict(int)
        for episode, nwords in words[character]:
            words_per_episode[episode] += nwords
        words_per_character_by_episode[character] = Counter(words_per_episode)

    return words_per_character_by_episode
