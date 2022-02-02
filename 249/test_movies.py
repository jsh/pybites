"""Bite 249. Test a movie DB class."""

import os
import random
import sqlite3
import string

import pytest

from movies import MovieDb

salt = "".join(random.choice(string.ascii_lowercase) for i in range(20))
DB = os.path.join(os.getenv("TMP", "/tmp"), f"movies_{salt}.db")
# DB = f"movies.db"  # TODO: remove
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
    database = MovieDb(DB, DATA, TABLE)
    database.init()
    yield database
    database.drop_table()


def test_init(db):
    """Db is initialized."""
    assert isinstance(db, MovieDb)
    assert db.table == TABLE
    assert isinstance(db.cur, sqlite3.Cursor)
    assert db.data == DATA
    assert isinstance(db.con, sqlite3.Connection)


def test_query(db):
    """Query returns correct results."""
    datum = DATA[0]
    reply = db.query(*datum)
    assert reply == [(1,) + datum]
    assert len(db.query(year=1939)) == 2
    assert len(db.query(score_gt=8.3)) == 5
    assert len(db.query(title="Montenegro")) == 0
    assert len(db.query(title="The")) == 5


def test_add(db):
    """Add adds a retrievable record."""
    crumb = ("Crumb", 1994, 9.5)
    db.add("Crumb", 1994, 9.5)
    assert db.query(title="Crumb")[0][1:] == crumb


def test_delete(db):
    """Delete deletes a record."""
    crumb = ("Crumb", 1994, 9.5)
    db.add(*crumb)
    idx = db.query(title="Crumb")[0][0]
    db.delete(idx)
