"""Bite 243. Test code that parses JSON and IP ranges."""

import json
import os
from ipaddress import IPv4Network
from pathlib import Path
from typing import List
from urllib.request import urlretrieve

import pytest

from ips import ServiceIPRange, get_aws_service_range, parse_ipv4_service_ranges

URL = "https://bites-data.s3.us-east-2.amazonaws.com/ip-ranges.json"
TMP = os.getenv("TMP", "/tmp")
PATH = Path(TMP, "ip-ranges.json")
IP = IPv4Network("192.0.2.8/29")


@pytest.fixture(scope="module")
def json_file() -> Path:
    """Import data into tmp folder."""
    urlretrieve(URL, PATH)
    return PATH


@pytest.fixture(scope="module")
def service_ranges(json_file) -> List[ServiceIPRange]:
    """List of services ranges from data."""
    return parse_ipv4_service_ranges(json_file)


@pytest.fixture(scope="module")
def dummy_json() -> str:
    """Completely bogus JSON data."""
    return '{ \
      "syncToken": "1575592390", \
      "createDate": "2019-12-06-00-33-10", \
      "prefixes": [ \
        { \
          "ip_prefix": "127.0.0.1", \
          "region": "local-west-1", \
          "service": "MYTEST" \
        } \
      ] \
    }'


def test_class() -> None:
    """Unit-test the class itself."""
    sipr = ServiceIPRange(
        service="MYSERVICE",
        region="MYREGION",
        cidr=IPv4Network("1.2.3.4/32"),
    )
    assert isinstance(sipr, ServiceIPRange)
    assert sipr.service == "MYSERVICE"
    assert (
        str(sipr)
        == "1.2.3.4/32 is allocated to the MYSERVICE service in the MYREGION region"
    )


def test_parse_ipv4_service_ranges(dummy_json):
    """Unit-test parse_ipv4_service_ranges."""
    data = json.loads(dummy_json)
    prefixes = data["prefixes"]
    prefix = prefixes[0]
    service_list = [
        ServiceIPRange(
            service=prefix["service"],
            region=prefix["region"],
            cidr=IPv4Network(prefix["ip_prefix"]),
        )
    ]
    json_file = Path(TMP, "dummy.json")
    with open(json_file, "w", encoding="utf-8") as json_out:
        json.dump(data, json_out)

    assert parse_ipv4_service_ranges(json_file) == service_list


@pytest.mark.parametrize(
    "input_ip, expected_output",
    [
        (
            "54.250.251.0",
            [
                "54.250.0.0/16 is allocated to the AMAZON service in the ap-northeast-1 region",
                "54.250.0.0/16 is allocated to the EC2 service in the ap-northeast-1 region",
                "54.250.251.0/24 is allocated to the WORKSPACES_GATEWAYS service in the ap-northeast-1 region",
            ],
        )
    ],
)
def test_get_aws_service_range(input_ip, expected_output, service_ranges) -> None:
    """Unit-test get_aws_service_range."""
    services = get_aws_service_range(input_ip, service_ranges)
    service_list = []
    for service in services:
        service_list.append(str(service))
    assert expected_output == service_list


def test_bad_ip(service_ranges) -> None:
    """Unit-test bad IP value throws correct exception."""
    with pytest.raises(ValueError) as excinfo:
        get_aws_service_range("foo", service_ranges)
    assert "Address must be a valid IPv4 address" in str(excinfo.value)


def test_nonexistent_ip(service_ranges) -> None:
    """IP not in services returns empty list."""
    assert get_aws_service_range("127.0.0.1", service_ranges) == []
