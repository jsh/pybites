"""Bite 243. Test code that parses JSON and IP ranges."""

import os
from ipaddress import IPv4Network
from pathlib import Path
from urllib.request import urlretrieve

import pytest

from ips import ServiceIPRange, get_aws_service_range, parse_ipv4_service_ranges

URL = "https://bites-data.s3.us-east-2.amazonaws.com/ip-ranges.json"
TMP = os.getenv("TMP", "/tmp")
PATH = Path(TMP, "ip-ranges.json")
IP = IPv4Network("192.0.2.8/29")


@pytest.fixture(scope="module")
def json_file() -> Path:
    """Import data into tmp folder"""
    urlretrieve(URL, PATH)
    return PATH


def test_nothing() -> None:
    """Dummy, just to have a test."""
