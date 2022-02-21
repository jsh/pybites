"""Bite 316. To rent or to stream movies?"""

from collections import defaultdict
from datetime import date
from typing import Dict, NamedTuple, Sequence


class MovieRented(NamedTuple):
    """Describe rental istory for one movie."""

    title: str
    price: int
    date: date


RentingHistory = Sequence[MovieRented]
STREAMING_COST_PER_MONTH = 12
STREAM, RENT = "stream", "rent"


def choice(cost: int) -> str:
    """Choose 'rent' unless the cost is more than streaming cost."""
    return "rent" if cost <= STREAMING_COST_PER_MONTH else "stream"


def rent_or_stream(
    renting_history: RentingHistory,
    streaming_cost_per_month: int = STREAMING_COST_PER_MONTH,
) -> Dict[str, str]:
    """Whether renting movies one by one is cheaper than streaming movies by months.

    Determine this PER MONTH for the movies in renting_history.

    Return a dict of:
    keys = months (YYYY-MM)
    values = 'rent' or 'stream' based on what is cheaper

    Check out the tests for examples.
    """
    price_for_month: defaultdict = defaultdict(int)
    for movie in renting_history:
        price_for_month[str(movie.date)[:-3]] += movie.price
    ans = {month: choice(cost) for month, cost in price_for_month.items()}
    return ans
