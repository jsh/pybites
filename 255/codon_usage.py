#!/usr/bin/env python3
"""Bite 255. Codon Usage."""

import os
from collections import Counter
from typing import Counter, Dict, List, Set, Tuple  # pylint: disable=reimported
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

# Converted from http://ftp.ncbi.nlm.nih.gov/genomes/archive/old_refseq/Bacteria/Staphylococcus_aureus_Newman_uid58839/NC_009641.ffn  # pylint: disable=line-too-long
URL = "https://bites-data.s3.us-east-2.amazonaws.com/NC_009641.txt"

# Order of bases in the table
BASE_ORDER = ["U", "C", "A", "G"]


def _preload_sequences(url: str = URL) -> List[str]:
    """Return coding sequences, one sequence each line.

    Provided helper function
    Returns coding sequences, one sequence each line
    """
    filename = os.path.join(os.getenv("TMP", "/tmp"), "NC_009641.txt")
    if not os.path.isfile(filename):
        urlretrieve(url, filename)
    with open(filename, "r", encoding="utf-8") as f_in:
        return f_in.readlines()


def _clean_sequences(sequences: List[str]) -> List[str]:
    bases = set(BASE_ORDER)
    sequences = [
        sequence.strip().upper() for sequence in sequences
    ]  # uppercase and strip newlines
    sequences = [
        sequence
        for sequence in sequences
        if set(sequence) == set(bases) and len(sequence) % 3 == 0
    ]  # remove sequences with bad bases, bad lengths
    return sequences


def _table(sequence: str):
    """Create a dictionary of codon frequencies in a sequence."""
    codons = [sequence[i : i + 3] for i in range(0, len(sequence), 3)]
    table: Counter = Counter()
    for codon in codons:
        table[codon] += 1
    return table


def _tt_str_to_aa_dict(translation_table_str: str) -> Tuple[Dict[str, str], Set[str]]:
    tt_rows = translation_table_str.split("\n")
    rows = [row.split() for row in tt_rows]
    table_dict = {row[0]: row[2].upper() for row in rows if len(row) == 3}
    aas = table_dict["AAs"]
    starts = table_dict["Starts"]
    base1 = table_dict["Base1"].replace("T", "U")
    base2 = table_dict["Base2"].replace("T", "U")
    base3 = table_dict["Base3"].replace("T", "U")
    assert len(aas) == len(starts) == len(base1) == len(base2) == len(base3)
    aa_dict = {}
    start_codons: Set[str] = set()
    for col, amino_acid in enumerate(aas):
        codon = base1[col] + base2[col] + base3[col]
        aa_dict[codon] = amino_acid
        if starts[col] == "M":
            start_codons.update(codon)
    return aa_dict, start_codons


def _codon_table_to_str(
    codon_table: Counter, translation_table_str: str
) -> str:  # pylint: disable=too-many-locals
    header = "|  Codon AA  Freq  Count  |  Codon AA  Freq  Count  |  Codon AA  Freq  Count  |  Codon AA  Freq  Count  |"
    separator = "-" * len(header)
    totals = sum(codon_table.values())
    freq_table = [header, separator]
    aa_dict, start_codons = _tt_str_to_aa_dict(translation_table_str)
    for b_1 in BASE_ORDER:
        for b_3 in BASE_ORDER:
            line = [""]
            for b_2 in BASE_ORDER:
                codon = b_1 + b_2 + b_3
                count = codon_table[codon]
                line.append(
                    f"{codon:<3}:  {aa_dict[codon]:<3}{round(count*1000/totals,1):>5} {count:>6}  "
                )
            nline = "|  ".join(line) + "|"
            freq_table.append(nline)
        freq_table.append(separator)
    freq_table_string = "\n".join(freq_table)
    return freq_table_string


def return_codon_usage_table(
    sequences: List[str] = _preload_sequences(),
    translation_table_str: str = TRANSL_TABLE_11,
) -> str:
    """Find frequency of each codon.

    Receives a list of gene sequences and a translation table string
    Returns a string with all bases and their frequencies in a table
    with the following fields:
    codon_triplet: amino_acid_letter frequency_per_1000 absolute_occurrences

    Skip invalid coding sequences:
       --> must consist entirely of codons (3-base triplet)
    """
    codon_table: Counter = Counter()
    sequences = _preload_sequences()
    sequences = _clean_sequences(sequences)
    for sequence in sequences:
        codon_table += _table(sequence)
    return _codon_table_to_str(codon_table, translation_table_str)


if __name__ == "__main__":
    print(return_codon_usage_table())
