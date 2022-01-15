#!/usr/bin/env python3
"""Bite 298. Fasta to 2-Line Fasta."""

import os
import urllib
from typing import List

from Bio import SeqIO

# Fetched and truncated from
# https://www.uniprot.org/uniprot/?query=database%3A%28type%3Aembl+AE017195%29&format=fasta (Aug 01, 2020)
URL = "https://bites-data.s3.us-east-2.amazonaws.com/fasta_genes.fasta"
FASTA_FILE = os.path.join(os.getenv("TMP", "/tmp"), "fasta_genes.fasta")
if not os.path.isfile(FASTA_FILE):
    urllib.request.urlretrieve(URL, FASTA_FILE)


def _append_2_line_fasta(two_line_fasta: List[str], fasta_list: List[str]) -> List[str]:
    """Append two_line_fasta to fasta_list."""
    assert len(two_line_fasta) == 2, two_line_fasta
    fasta_list += two_line_fasta
    return fasta_list


def fasta_to_2line_fasta(fasta_file: str, fasta_2line_file: str) -> int:
    """Convert multi-line fasta_file to 2-line fasta file.

    :param fasta_file: Filename of multi-line FASTA file
    :param fasta_2line_file: Filename of 2-line FASTA file
    :return: Number of records
    """
    # initialize lists
    fasta_list: List[str] = []
    two_line_fasta: List[str] = []
    with open(fasta_file, "r", encoding="utf-8") as f_in:
        for line in f_in:
            if line[0] == ">":
                if two_line_fasta:
                    two_line_fasta[1] += "\n"
                    _append_2_line_fasta(two_line_fasta, fasta_list)
                # re-initialize
                two_line_fasta = [line, ""]
            else:
                two_line_fasta[1] += line.strip()

        _append_2_line_fasta(two_line_fasta, fasta_list)
    # fasta_list contains all input file lines, converted to two-line fastas.
    with open(fasta_2line_file, "w", encoding="utf-8") as f_out:
        f_out.writelines(fasta_list)

    return len(fasta_list) // 2


if __name__ == "__main__":
    print(fasta_to_2line_fasta(FASTA_FILE, f"{FASTA_FILE}_converted.fasta"))
