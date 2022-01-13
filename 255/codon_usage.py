#!/usr/bin/env python3
"""Print codon usage statistics."""

# TODO: convert T->U
# TODO: print out a codon at a time

import os
import re
from typing import Dict, List, Tuple
from urllib.request import urlretrieve

# Translation Table:
# https://www.ncbi.nlm.nih.gov/Taxonomy/Utils/wprintgc.cgi#SG11
# Each column represents one entry. Codon = {Base1}{Base2}{Base3}
# All Base 'T's need to be converted to 'U's to convert DNA to RNA
TRANSL_TABLE_11 = """
    AAs  = FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG
  Starts = ---M------**--*----M------------MMMM---------------M------------
  Base1  = TTTTTTTTTTTTTTTTCCCCCCCCCCCCCCCCAAAAAAAAAAAAAAAAGGGGGGGGGGGGGGGG
  Base2  = TTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGG
  Base3  = TCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAG
"""

# Converted from http://ftp.ncbi.nlm.nih.gov/genomes/archive/old_refseq/Bacteria/Staphylococcus_aureus_Newman_uid58839/NC_009641.ffn  # noqa E501
URL = "https://bites-data.s3.us-east-2.amazonaws.com/NC_009641.txt"

# Order of bases in the table
BASE_ORDER = ["U", "C", "A", "G"]


def _preload_sequences(url: str = URL) -> List[str]:
    """Return coding sequences, one sequence each line.

    Provided helper function
    """
    filename = os.path.join(os.getenv("TMP", "/tmp"), "NC_009641.txt")
    if not os.path.isfile(filename):
        urlretrieve(url, filename)
    with open(filename, "r", encoding="utf-8") as f_seq:
        return f_seq.readlines()


def translation_table_to_dict(translation_table: str) -> Dict[str, Tuple[str, str]]:
    """Convert translation table to {codon: (AA, Start)}."""
    codons = [
        "".join([f, s, t]) for f in BASE_ORDER for s in BASE_ORDER for t in BASE_ORDER
    ]
    pat = re.compile(r"(\S+)\s+=\s+(\S+)")
    transl_rows = re.findall(pat, translation_table)
    transl_dict = {entry[0]: entry[1] for entry in transl_rows}
    assert (
        len(transl_dict["AAs"])
        == len(transl_dict["Starts"])
        == len(transl_dict["Base1"])
        == len(transl_dict["Base2"])
        == len(transl_dict["Base3"])
        == len(codons)
    )
    return dict(zip(codons, zip(transl_dict["AAs"], transl_dict["Starts"])))


def return_codon_usage_table(
    sequences: List[str] = _preload_sequences(),
    translation_table_str: str = TRANSL_TABLE_11,
) -> str:
    """Convert sequence and tranlation table to table of bases and frequencies.

    Receives a list of gene sequences and a translation table string
    Returns a string with all bases and their frequencies in a table
    with the following fields:
    codon_triplet: amino_acid_letter frequency_per_1000 absolute_occurrences

    Skip invalid coding sequences:
       --> must consist entirely of codons (3-base triplet)
    """


if __name__ == "__main__":
    for codon, val in translation_table_to_dict(TRANSL_TABLE_11).items():
        print(codon, val)
