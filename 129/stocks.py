"""Bite 129. Analyze Stock Data."""

from collections import defaultdict
from typing import Dict, Tuple

import requests

STOCK_DATA = "https://bites-data.s3.us-east-2.amazonaws.com/stocks.json"

# pre-work: load JSON data into program

with requests.Session() as s:
    data = s.get(STOCK_DATA).json()


# pylint: disable=inconsistent-return-statements
def _cap_str_to_mln_float(cap: str) -> float:
    """Turn cap data into floats.

    If cap = 'n/a' return 0, else:
       - strip off leading '$',
       - if 'M' in cap value, strip it off and return value as float,
       - if 'B', strip it off, multiply by 1,000 and return
         value as float
    """
    if cap == "n/a":
        return float(0)
    cap = cap.lstrip("$")
    if cap[-1] == "M":
        return float(cap[:-1])
    if cap[-1] == "B":
        return 1000 * float(cap[:-1])


def _datum_to_cap(datum: Dict) -> float:
    """Cap value of a datum."""
    return _cap_str_to_mln_float(datum["cap"])


def get_industry_cap(industry: str) -> float:
    """Total cap values for an industry.

    Return the sum of all cap values for given industry, use
    the _cap_str_to_mln_float to parse the cap values,
    return a float with 2 digit precision
    """
    industry_data = [datum for datum in data if industry == datum["industry"]]
    caps = [datum["cap"] for datum in industry_data]
    caps = [_cap_str_to_mln_float(cap) for cap in caps]
    return round(sum(caps), 2)


def get_stock_symbol_with_highest_cap() -> str:
    """Stock symbol with highest cap.

    Return the stock symbol (e.g. PACD) with the highest cap.
    Use the _cap_str_to_mln_float to parse the cap values
    """
    highest = max(data, key=_datum_to_cap)
    return highest["symbol"]


def get_sectors_with_max_and_min_stocks() -> Tuple[str, str]:
    """Find sectors with max and min stocks.

    Return a tuple of the sectors with most and least stocks, discard n/a
    """
    good_data = [datum for datum in data if datum["sector"] != "n/a"]
    nstocks: defaultdict = defaultdict(int)
    for datum in good_data:
        sector = datum["sector"]
        nstocks[sector] += 1
    most = max(nstocks, key=nstocks.get)
    least = min(nstocks, key=nstocks.get)
    return (most, least)
