"""Bite 30. Movie data analysis."""

import csv
import os
from collections import defaultdict, namedtuple
from typing import Dict, List, Tuple
from urllib.request import urlretrieve
import sys

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


def get_movies_by_director() -> Dict[str, Movie]:
    """Convert from csv to dict, indexed by director.

    Extracts all movies from csv and stores them in a dict,
    where keys are directors, and values are a list of movies,
    use the defined Movie namedtuple
    """
    import csv
    movies = defaultdict(list)
    with open(LOCAL, newline='', encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile, quotechar='|')
        for row in reader:
            director = row["director_name"]
            movie = Movie(row["movie_title"], row["title_year"], row["imdb_score"])
            movies[director].append(movie)
    print(movies)
    sys.exit(0)
    movies_by_director = {}
    for director, movie_list in movies:
       movies_by_director[director] = movie_list
    return movies_by_director


def calc_mean_score(movies: List[Movie]) -> float:
    """Get mean for all movies.

    Helper method to calculate mean of list of Movie namedtuples,
    round the mean to 1 decimal place
    """
    return 0.0


def get_average_scores(directors: Dict[str, Movie]) -> List[Tuple[str, float]]:
    """Make list of directors by score.

    Iterate through the directors dict (returned by get_movies_by_director),
    return a list of tuples (director, average_score) ordered by highest
    score in descending order. Only take directors into account
    with >= MIN_MOVIES
    """
    return []
