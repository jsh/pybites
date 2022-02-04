#!/usr/bin/env python3
"""Bite 18. Find the most common word."""

import os
import re
import urllib.request
from collections import Counter

# data provided
tmp = os.getenv("TMP", "/tmp")
stopwords_file = os.path.join(tmp, "stopwords")
harry_text = os.path.join(tmp, "harry")
urllib.request.urlretrieve(
    "https://bites-data.s3.us-east-2.amazonaws.com/stopwords.txt", stopwords_file
)
urllib.request.urlretrieve(
    "https://bites-data.s3.us-east-2.amazonaws.com/harry.txt", harry_text
)


def get_harry_most_common_word():
    """Find most common word in Harry Potter text."""
    # get Harry Potter text, lower-case.
    with open(harry_text, encoding="utf-8") as f_in:
        text = f_in.read()
    text = re.sub(r"[^\w\s]+", "", text).lower()
    words = text.split()
    # remove stopwords
    with open(stopwords_file, encoding="utf-8") as f_in:
        stopwords = f_in.read().splitlines()
    words = [word for word in words if word not in stopwords]
    word_freqs = Counter(words)
    return word_freqs.most_common()[0]
