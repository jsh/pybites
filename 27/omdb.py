"""Bite 27. Parse omdb movie json data."""

import json
from operator import itemgetter
from typing import Dict, List


def get_movie_data(files: List[str]) -> List[Dict]:
    """Parse movie json files into a list of dicts."""
    movie_data = []
    for file in files:
        with open(file, encoding="utf-8") as f_in:
            movie_data.append(json.load(f_in))
    return movie_data


def get_single_comedy(movies: List[Dict]) -> str:
    """Return the movie with Comedy in Genres."""
    comedies = [movie["Title"] for movie in movies if "Comedy" in movie["Genre"]]
    return comedies.pop() if comedies else ""


def get_movie_most_nominations(movies: List[Dict]) -> str:
    """Return the movie that had the most nominations."""
    for movie in movies:
        movie["Nominations"] = int(movie["Awards"].split()[-2])
    by_nominations = sorted(movies, key=itemgetter("Nominations"), reverse=True)

    return by_nominations[0]["Title"]


def get_movie_longest_runtime(movies: List[Dict]) -> str:
    """Return the movie that has the longest runtime."""
    for movie in movies:
        movie["Runtime"] = int(movie["Runtime"].split()[0])
    by_runtime = sorted(movies, key=itemgetter("Runtime"), reverse=True)
    return by_runtime[0]["Title"]
