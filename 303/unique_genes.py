"""Bite 303. Unique genes."""

import gzip
import os
import re
from collections import defaultdict

from Bio import SeqIO  # type: ignore


def ntags(entry):
    """Count locus_tags."""
    return len(entry[1])


def convert_to_unique_genes(filename_in, filename_out):
    """De-dup and sort fasta file.

    Takes a standard FASTA file or gzipped FASTA file,
    de-duplicates the file, sorts by number of occurrences and
    outputs the result in a standard FASTA file

    filename_in: str Filename of FASTA file containing duplicated genes
    filename_out: str Filename of FASTA file to output reduced file

    returns None
    """
    try:
        with gzip.open(filename_in) as f_in, open(
            filename_out, "r", encoding="utf-8"
        ) as f_out:
            f_in.readlines()
            f_out.writelines()
        os.replace(filename_out, filename_in)
    except gzip.BadGzipFile:
        pass
    pat = re.compile(r"\S+\s\[locus_tag=(.*)]")
    record_list = defaultdict(list)

    for record in SeqIO.parse(filename_in, "fasta"):
        locus_tag = pat.match(record.description)[1]
        record_list[record.seq].append(locus_tag)
    record_list = sorted(record_list.items(), key=ntags, reverse=True)
    with open(filename_out, "w", encoding="utf-8") as f_out:
        for record in record_list:
            seq, locus_tags = record
            plural = "s" if len(locus_tags) > 1 else ""
            locus_tags = ",".join(locus_tags)
            f_out.write(f"> narI [locus_tag{plural}={locus_tags}]\n")
            f_out.write(f"{seq}\n")
