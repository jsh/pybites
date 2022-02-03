"""Bite 130. Analyze some basic Car Data."""

from collections import Counter

import requests

from typing import Set

CAR_DATA = "https://bites-data.s3.us-east-2.amazonaws.com/cars.json"

# pre-work: load JSON data into program

with requests.Session() as session:
    data = session.get(CAR_DATA).json()


# TODO: write the code
def most_prolific_automaker(year: int) -> str:
    """Find most prolific automaker of the year.

    Given year 'year' return the automaker that released
    the highest number of new car models
    """


def get_models(automaker: str, year: none) -> Set[str]:
    """Get models for automakker and year.

    Filter cars 'data' by 'automaker' and 'year',
    return a set of models (a 'set' to avoid duplicate models)
    """
