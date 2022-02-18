"""Bite 195. Analyze NBA Data with sqlite3."""
# pylint: disable=unused-argument,too-many-locals,too-many-arguments

import csv
import os
import random
import sqlite3
import string
from collections import Counter, namedtuple
from pathlib import Path
from statistics import mean

import requests

DATA_URL = "https://query.data.world/s/ezwk64ej624qyverrw6x7od7co7ftm"
TMP = Path(os.getenv("TMP", "/tmp"))

SALT = "".join(random.choice(string.ascii_lowercase) for i in range(20))
DB = TMP / f"nba_{SALT}.db"

Player = namedtuple(
    "Player", ("name year first_year team college active " "games avg_min avg_points")
)

conn = sqlite3.connect(DB)
cur = conn.cursor()


def import_data() -> None:
    """Pull down CSV data, convert to sqlite3 database."""
    with requests.Session() as session:
        content = session.get(DATA_URL).content.decode("utf-8")

    reader = csv.DictReader(content.splitlines(), delimiter=",")

    players = []
    for row in reader:
        players.append(
            Player(
                name=row["Player"],
                year=row["Draft_Yr"],
                first_year=row["first_year"],
                team=row["Team"],
                college=row["College"],
                active=row["Yrs"],
                games=row["Games"],
                avg_min=row["Minutes.per.Game"],
                avg_points=row["Points.per.Game"],
            )
        )

    cur.execute(
        """CREATE TABLE IF NOT EXISTS players
                  (name, year, first_year, team, college, active,
                  games, avg_min, avg_points)"""
    )
    cur.executemany("INSERT INTO players VALUES (?,?,?,?,?,?,?,?,?)", players)
    conn.commit()


import_data()


def query(
    name=None,
    year=None,
    first_year=None,
    team=None,
    college=None,
    active=None,
    games=None,
    avg_min=None,
    avg_points=None,
    operator="LIKE",
    fields="*",
):
    """Query the sqlite db."""
    argv = locals()
    del argv["operator"]
    del argv["fields"]

    sql = f"SELECT {fields} FROM players"
    params = []
    for key, value in argv.items():
        if value is not None:
            sql += f" WHERE {key} {operator} ?"
            params.append(value)
    cur.execute(sql, params)
    return cur.fetchall()


def player_with_max_points_per_game() -> str:
    """The player with highest average points per game.

    (don't forget to CAST to numeric in your SQL query)
    """
    most_ave_points = query(fields="name, MAX(CAST(avg_points AS REAL))")
    return most_ave_points.pop()[0]


def number_of_players_from_duke() -> int:
    """Return the number of players with college == Duke University."""
    duke_players = query(college="Duke University")
    return len(duke_players)


def avg_years_active_players_stanford() -> float:
    """Return average years players from Stanford University are active.

    ("active" column)  Round to two digits.
    """
    active_years = query(fields="active", college="Stanford University")
    active_years = [int(entry[0]) for entry in active_years]
    ave_active_years = mean(active_years)
    return round(ave_active_years, 2)


def year_with_most_new_players() -> int:
    """Return the year with the most new players.

    Hint: you can use GROUP BY on the year column.
    """
    sql = "SELECT year, COUNT(*) FROM players GROUP BY year"
    cur.execute(sql)
    new_per_year: Counter = Counter()
    for year, count in cur.fetchall():
        new_per_year[int(year)] = count
    return new_per_year.most_common(1).pop()[0]
