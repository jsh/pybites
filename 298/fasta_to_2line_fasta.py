#!/usr/bin/env python3
"""Bite 298. Fasta to 2-Line Fasta."""

import os
import urllib

from Bio import SeqIO

# Fetched and truncated from
# https://www.uniprot.org/uniprot/?query=database%3A%28type%3Aembl+AE017195%29&format=fasta (Aug 01, 2020)
URL = "https://bites-data.s3.us-east-2.amazonaws.com/fasta_genes.fasta"
FASTA_FILE = os.path.join(os.getenv("TMP", "/tmp"), "fasta_genes.fasta")
if not os.path.isfile(FASTA_FILE):
    urllib.request.urlretrieve(URL, FASTA_FILE)


def fasta_to_2line_fasta(fasta_file: str, fasta_2line_file: str) -> int:
    """Convert multi-line fasta_file to 2-line fasta file.

    :param fasta_file: Filename of multi-line FASTA file
    :param fasta_2line_file: Filename of 2-line FASTA file
    :return: Number of records
    """
    with open(fasta_2line_file, "w", encoding="utf-8") as f_out:
        records = 0
        for seq_record in SeqIO.parse(fasta_file, "fasta"):
            f_out.write(f">{seq_record.description}\n")
            f_out.write(f"{seq_record.seq}\n")
            records += 1
        return records


if __name__ == "__main__":
    print(fasta_to_2line_fasta(FASTA_FILE, f"{FASTA_FILE}_converted.fasta"))
