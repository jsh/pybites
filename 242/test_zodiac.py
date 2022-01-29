"""Bite 242. Zodiacal data parsing."""

import json
import os
from datetime import datetime
from pathlib import Path
from typing import List
from urllib.request import urlretrieve

import pytest

from zodiac import (
    Sign,
    get_sign_by_date,
    get_sign_with_most_famous_people,
    get_signs,
    signs_are_mutually_compatible,
)

# original source: https://zodiacal.herokuapp.com/api
URL = "https://bites-data.s3.us-east-2.amazonaws.com/zodiac.json"
TMP = os.getenv("TMP", "/tmp")
PATH = Path(TMP, "zodiac.json")


@pytest.fixture(scope="module")
def signs() -> List[Sign]:
    """Return list of signs."""
    if not PATH.exists():
        urlretrieve(URL, PATH)
    with open(PATH, encoding="utf-8") as f_in:
        data = json.loads(f_in.read())
    return get_signs(data)


def test_fixture(signs) -> None:
    """Trying out the fixture."""
    print(signs[0])


def test_get_sign_with_most_famous_people(signs) -> None:
    assert get_sign_with_most_famous_people(signs) == ("Scorpio", 35)


def test_signs_are_mutually_compatible(signs) -> None:
    assert signs_are_mutually_compatible(signs, "Aries", "Leo")
    assert not signs_are_mutually_compatible(signs, "Scorpio", "Saggitarius")


def test_get_sign_by_date(signs) -> None:
    first_day = datetime.fromordinal(1)
    assert get_sign_by_date(signs, first_day) == "Capricorn"