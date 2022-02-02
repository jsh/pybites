"""Bite 249. Test a movie DB class."""

import os
import random
import sqlite3
import string

import pytest

from movies import MovieDb

salt = "".join(random.choice(string.ascii_lowercase) for i in range(20))
DB = os.path.join(os.getenv("TMP", "/tmp"), f"movies_{salt}.db")
# https://www.imdb.com/list/ls055592025/
DATA = [
    ("The Godfather", 1972, 9.2),
    ("The Shawshank Redemption", 1994, 9.3),
    ("Schindler's List", 1993, 8.9),
    ("Raging Bull", 1980, 8.2),
    ("Casablanca", 1942, 8.5),
    ("Citizen Kane", 1941, 8.3),
    ("Gone with the Wind", 1939, 8.1),
    ("The Wizard of Oz", 1939, 8),
    ("One Flew Over the Cuckoo's Nest", 1975, 8.7),
    ("Lawrence of Arabia", 1962, 8.3),
]
TABLE = "movies"


@pytest.fixture
def db(request):
    """Fixture to instantiate movie class."""
    # instantiate MovieDb class using above constants
    # do proper setup / teardown using MovieDb methods
    # https://docs.pytest.org/en/latest/fixture.html (hint: yield)
    # TODO: setup with __init__()
    # TODO: tear-down with drop_table

    database = MovieDb(DB, DATA, TABLE)
    return database

    def fin():
        database.drop_table()

    request.add_finalizer(fin)


def test_init(db):
    assert isinstance(db, MovieDb)
    assert db.table == "movies"
    assert isinstance(db.cur, sqlite3.Cursor)
    assert db.data == DATA
    assert isinstance(db.con, sqlite3.Connection)


def test_query(db):
    """Unit-test query."""
    # TODO: lots of args, test them all
    datum = DATA[0]
    reply = db.query(*datum)
    assert reply == Null


def test_add(db):
    """Unit-test add."""


def test_delete(db):
    """Unit-test delete."""
