#!/usr/bin/env python3
"""Bite 4. Top 10 PyBites tags."""

import os
import urllib.request
import xml.etree.ElementTree as ET
from collections import Counter
from typing import List, Optional, Tuple

# prep
tmp = os.getenv("TMP", "/tmp")
tempfile = os.path.join(tmp, "feed")
urllib.request.urlretrieve(
    "https://bites-data.s3.us-east-2.amazonaws.com/feed", tempfile
)

with open(tempfile, encoding="utf-8") as f_in:
    content = f_in.read().lower()


def tags(parent: ET.Element) -> List[Optional[str]]:
    """Extract tags in parent into a list."""
    tag_list = []
    if parent.tag == "category":
        tag_list.append(parent.text)  # you've hit a leaf
        return tag_list
    for child in parent:
        tag_list = tag_list + tags(child)
    return tag_list


def get_pybites_top_tags(n: int = 10) -> List[Tuple[Optional[str], int]]:
    """Use Counter to get the top 10 PyBites tags from the feed.

    data already loaded into the content variable
    """
    root = ET.fromstring(content)
    tag_counts = Counter(tags(root))
    most_common = tag_counts.most_common(n)
    return most_common if most_common else []
