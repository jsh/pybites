"""Bite 243. Test code that parses JSON and IP ranges."""

import os
import json
from ipaddress import IPv4Network
from pathlib import Path
from urllib.request import urlretrieve
from typing import List

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

@pytest.fixture(scope="module")
def service_ranges(json_file) -> List[ServiceIPRange]:
    return parse_ipv4_service_ranges(json_file)

@pytest.fixture(scope="module")
def dummy_json() -> str:
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
    sipr = ServiceIPRange(
        service="MYSERVICE",
        region="MYREGION",
        cidr="1.2.3.4/69",
    )
    assert isinstance(sipr, ServiceIPRange)
    assert sipr.service == "MYSERVICE"
    assert repr(sipr) == "ServiceIPRange(service='MYSERVICE', region='MYREGION', cidr='1.2.3.4/69')"
    assert str(sipr) == "1.2.3.4/69 is allocated to the MYSERVICE service in the MYREGION region"

def test_parse_ipv4_service_ranges(dummy_json):
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
       ("54.250.0.0",
            [
            "54.250.0.0/16 is allocated to the AMAZON service in the ap-northeast-1 region",
            "54.250.0.0/16 is allocated to the EC2 service in the ap-northeast-1 region",
            "54.250.251.0/24 is allocated to the WORKSPACES_GATEWAYS service in the ap-northeast-1 region",
            ]
        )
    ]
)
def test_get_aws_service_range(input_ip, expected_output, service_ranges) -> None:
    services = get_aws_service_range(input_ip, service_ranges)
    service_list = []
    for service in services:
        service_list.append(str(service))
        
    expected_output = service_list

def test_bad_ip(service_ranges) -> None:
    """Bad value."""
    with pytest.raises(ValueError):
        get_aws_service_range("foo", service_ranges)


def test_nonexistent_ip(service_ranges) -> None:
    """Bad value."""
    assert get_aws_service_range("127.0.0.1", service_ranges) == []
