"""Bite 30. Movie data analysis."""

import csv
import os
from collections import defaultdict, namedtuple
from typing import Dict, List, Sequence
from urllib.request import urlretrieve

BASE_URL = "https://bites-data.s3.us-east-2.amazonaws.com/"
TMP = os.getenv("TMP", "/tmp")

FNAME = "movie_metadata.csv"
REMOTE = os.path.join(BASE_URL, FNAME)
LOCAL = os.path.join(TMP, FNAME)
urlretrieve(REMOTE, LOCAL)

MOVIE_DATA = LOCAL
MIN_MOVIES = 4
MIN_YEAR = 1960

Movie = namedtuple("Movie", "title year score")


def get_movies_by_director() -> Dict[str, List[Movie]]:
    """Convert from csv to dict, indexed by director.

    Extracts all movies from csv and stores them in a dict,
    where keys are directors, and values are a list of movies,
    use the defined Movie namedtuple
    """
    directors = defaultdict(list)
    with open(LOCAL, newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            name = row["director_name"]
            title = row["movie_title"]
            year = row["title_year"]
            score = row["imdb_score"]
            if not (name and title and year and score):
                continue
            movie = Movie(title, int(year), float(score))
            if movie.year < MIN_YEAR:
                continue
            directors[name].append(movie)
    return directors


def calc_mean_score(movies: List[Movie]) -> float:
    """Get mean for all movies.

    Helper method to calculate mean of list of Movie namedtuples,
    round the mean to 1 decimal place
    """
    mean = sum([movie.score for movie in movies]) / len(movies)
    return round(mean, 1)


def get_average_scores(directors: Dict[str, List[Movie]]) -> Sequence:
    """Make list of directors by score.

    Iterate through the directors dict (returned by get_movies_by_director),
    return a list of tuples (director, average_score) ordered by highest
    score in descending order. Only take directors into account
    with >= MIN_MOVIES
    """
    scores = [
        (name, calc_mean_score(movies))
        for name, movies in directors.items()
        if len(movies) >= MIN_MOVIES
    ]
    scores = sorted(scores, key=lambda x: x[1], reverse=True)
    return scores
