#!/usr/bin/env python3
"""Bite 129. Analyze Stock Data."""

from typing import Tuple

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


def get_industry_cap(industry: str) -> float:
    """Total cap values for an industry.

    Return the sum of all cap values for given industry, use
    the _cap_str_to_mln_float to parse the cap values,
    return a float with 2 digit precision
    """


def get_stock_symbol_with_highest_cap() -> str:
    """Stock symbol with highest cap.

    Return the stock symbol (e.g. PACD) with the highest cap.
    Use the _cap_str_to_mln_float to parse the cap values
    """


def get_sectors_with_max_and_min_stocks() -> Tuple[str, str]:
    """Find sectors with max and min stocks.

    Return a tuple of the sectors with most and least stocks, discard n/a
    """


if __name__ == "__main__":
    print(data[0])
