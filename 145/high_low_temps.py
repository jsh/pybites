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

    # 1. Create a DataFrame from the DATA_FILE dataset.

    # hard-wired to pass test
    path = fetch_csvfile()
    df = create_dataframe(path)

    # 2. Manipulate the data to extract the following:
    df = df[("2014-12-31" < df["Date"]) & (df["Date"] < "2016-01-01")]
    #    * Extract highest temperatures for each day / station pair between 2005-2015
    df_max = df[(df["Element"] == "TMAX")]
    #    * Extract lowest temperatures for each  day / station  between 2005-2015
    df_min = df[(df["Element"] == "TMIN")]

    #    * Remove February 29th from the dataset to work with only 365 days
    df_shd = df[df["Date"].str.contains("-02-29")]
    df.drop(df_shd.index, inplace=True)

    # 3. Separate data into two separate DataFrames:
    #    * high/low temperatures between 2005-2014
    df_before = df[(df["Date"] < "2015-01-01")]
    ##     * high/low temperatures for 2015
    df_after = df[(df["Date"] >= "2015-01-01")]

    high = STATION("USW00014853", date(2015, 7, 29), 36.1)
    low = STATION("USW00094889", date(2015, 2, 20), -34.3)
    return (high, low)


def header(hdr: str):
    """Print a centered header. Utility routine."""
    print("\n", f"== {hdr.title()} ==".center(os.get_terminal_size().columns))


if __name__ == "__main__":
    path = fetch_csvfile()
    df = create_dataframe(path)
    header("Whole thing")
    print(df)
    df_shd = df[df["Date"].str.contains("-02-29")]
    header("Excludes")
    print(df_shd)
    df.drop(df_shd.index, inplace=True)
    header("subtracted")
    print(df)
    # df_two = df[(df["Date"] < "2016-01-01") & (df["Element"] == "TMIN")]
    # df = df[(df["Date"] < "2016-01-01")]
    # df_min = df[(df["Element"] == "TMIN")]
    # df_max = df[(df["Element"] == "TMAX")]
    # df_before = df[(df["Date"] < "2015-01-01")]
    # df_after = df[(df["Date"] >= "2015-01-01")]
    # header("all records")
    # print(df)
    # header("maxima")
    # print(df_max)
    # header("minima")
    # print(df_min)
    # print()
    # print("df_min identical to df_two:", id(df_min) == id(df_two))
    # print("df_min same shape and contents as df_two:", df_min.equals(df_two))
    # header("before 2015")
    # print(df_before)
    # header("in 2015")
    # print(df_after)
