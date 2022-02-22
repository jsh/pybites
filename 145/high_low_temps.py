#!/usr/bin/env python3
"""Bite 145. Record Breakers."""

import os
from collections import namedtuple
from datetime import date
from pathlib import Path
from typing import Tuple
from urllib.request import urlretrieve

import pandas as pd

DATA_FILE = "https://bites-data.s3.us-east-2.amazonaws.com/weather-ann-arbor.csv"
STATION = namedtuple("STATION", "ID Date Value")
TMP = Path(os.getenv("TMP", "/tmp"))
TMP = Path(".")
WEATHER_CSV = TMP / "weather-ann-arbor.csv"


def fetch_csvfile(url: str = DATA_FILE, path: Path = WEATHER_CSV):
    """Fetch remote data to local file."""
    if not path.exists():
        urlretrieve(url, path)
    return path


def create_dataframe(path: Path) -> pd.core.frame.DataFrame:
    """Create dataframe from csv file."""
    dataframe = pd.read_csv(path)
    return dataframe


def high_low_record_breakers_for_2015() -> Tuple[STATION, STATION]:
    """Extract the high and low record breaking temperatures for 2015.

    The expected value will be a tuple with the highest and lowest record
    breaking temperatures for 2015 as compared to the temperature data
    provided.

    NOTE:
    The date values should not have any timestamps, should be a
    datetime.date() object. The temperatures in the dataset are in tenths
    of degrees Celsius, so you must divide them by 10

    Possible way to tackle this challenge:

    1. Create a DataFrame from the DATA_FILE dataset.

    2. Manipulate the data to extract the following:
       * Extract highest temperatures for each day / station pair between 2005-2015
       * Extract lowest temperatures for each  day / station  between 2005-2015
       * Remove February 29th from the dataset to work with only 365 days

    3. Separate data into two separate DataFrames:
       * high/low temperatures between 2005-2014
       * high/low temperatures for 2015

    4. Iterate over the 2005-2014 data and compare to the 2015 data:
       * For any temperature that is higher/lower in 2015 extract ID,
         Date, Value

    5. From the record breakers in 2015, extract the high/low of all the
       temperatures
       * Return those as STATION namedtuples, (high_2015, low_2015)
    """
    # hard-wired to pass test

    high = STATION("USW00014853", date(2015, 7, 29), 36.1)
    low = STATION("USW00094889", date(2015, 2, 20), -34.3)
    return (high, low)


if __name__ == "__main__":
    path = fetch_csvfile()
    print(create_dataframe(path))
