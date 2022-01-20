#!/usr/bin/env python3
"""Bite 310. Create file pairs."""

import re
from typing import List, Tuple


def _casefold(string: str) -> str:
    return string.casefold()


def _valid_name(filename: str) -> bool:
    """Check for valid filename.

    - SampleName can contain letters, number or special characters (including _)
    - The number following S runs from 1 to 99
    - The number following L runs from 001 to 999
    - R1 stands for file 1 and R2 for file 2 of a pair (no other numbers are allowed)
    - The last number block runs from 001 to 999
    - The file name extension should end in fastq.gz (no extra extensions such as fastq.gz.md5)
    """
    pat = re.compile(
        r"\S+_S([1-9]|\d)_L\d\d[1-9]_R(1|2)_\d\d[1-9].fastq.gz", flags=re.IGNORECASE
    )
    return bool(pat.fullmatch(filename))


def _pair(filename, r2s):
    first = filename.upper()
    first = first.replace("_R1_", "_R2_")
    for second in r2s:
        if first.casefold() == second.casefold():
            return (filename, second)
    return None


def pair_files(filenames: List[str]) -> List[Tuple[str, str]]:
    """Pair *_R1_* with *_R2_*.

    Function that pairs filenames

    filenames: list[str] containing filenames
    returns: list[tuple[str, str]] containing filename pairs
    """
    filenames = [filename for filename in filenames if _valid_name(filename)]
    r1s = [
        filename for filename in filenames if "_R1_" in filename or "_r1_" in filename
    ]
    r2s = [
        filename for filename in filenames if "_R2_" in filename or "_r2_" in filename
    ]
    pairs = []
    for filename in r1s:
        if next_pair := _pair(filename, r2s):
            pairs.append(next_pair)
    return pairs


# Set up for your convenience during testing
if __name__ == "__main__":
    my_filenames = [
        "Sample1_S1_L001_R1_001.FASTQ.GZ",
        "Sample1_S1_L001_R2_001.fastq.gz",
        "Sample2_S2_L001_R1_001.fastq.gz",
        "sample2_s2_l001_r2_001.fastq.gz",
    ]
    # ('Sample1_S1_L001_R1_001.FASTQ.GZ', 'Sample1_S1_L001_R2_001.fastq.gz')
    # ('Sample2_S2_L001_R1_001.fastq.gz', 'sample2_s2_l001_r2_001.fastq.gz')

    for pair in pair_files(my_filenames):
        print(pair)
