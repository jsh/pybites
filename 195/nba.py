#!/usr/bin/env python3
"""Bite 195. Analyze NBA Data with sqlite3."""

import csv
import os
import random
import sqlite3
import string
from collections import namedtuple
from pathlib import Path

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
):
    """Query the sqlite db."""
    argv = locals()
    del argv["operator"]

    sql = f"SELECT * FROM players"
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
    sql = f"SELECT name, MAX(CAST(avg_points AS REAL)) FROM players"
    cur.execute(sql)
    return cur.fetchall().pop()[0]


def number_of_players_from_duke() -> int:
    """Return the number of players with college == Duke University."""
    duke_players = query(college="Duke University")
    return len(duke_players)


def avg_years_active_players_stanford() -> float:
    """Return average years players from Stanford University are active.

    ("active" column)  Round to two digits.
    """
    return round(1.00, 2)


def year_with_most_new_players() -> int:
    """Return the year with the most new players.

    Hint: you can use GROUP BY on the year column.
    """
    return 1900


if __name__ == "__main__":
    print(player_with_max_points_per_game())
    #print(query(name="Michael Jordan"))
    #print(query(college="Duke University", operator="="))
