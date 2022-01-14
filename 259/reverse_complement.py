"""Create reverse complement of a sequence."""
# See tests for a more comprehensive complementary table

from typing import Dict

SIMPLE_COMPLEMENTS_STR = """#Reduced table with bases A, G, C, T
 Base	Complementary Base
 A	T
 T	A
 G	C
 C	G
"""


def _complements(str_table: str) -> Dict[str, str]:
    pairs = str_table.split("\n")[2:]
    complements = {}
    for pair in pairs:
        pair = pair.strip()
        if not pair:
            continue
        base_info = pair.split()
        (base, compl_base) = base_info[0], base_info[-1]
        complements[base] = compl_base
    return complements


# Recommended helper function
def _clean_sequence(sequence: str, str_table: str) -> str:
    """Canonicalize sequence.

    Receives a DNA sequence and a str_table that defines valid (and
    complementary) bases
    Returns all sequences converted to upper case and remove invalid
    characters
    t!t%ttttAACCG --> TTTTTTAACCG
    """
    complements = _complements(str_table)
    valid_bases = list(complements.keys())
    sequence = sequence.upper()
    return "".join([base for base in sequence if base in valid_bases])


def reverse(sequence: str, str_table: str = SIMPLE_COMPLEMENTS_STR) -> str:
    """Reverse sequence.

    Receives a DNA sequence and a str_table that defines valid (and
    complementary) bases
    Returns a reversed string of sequence while removing all characters
    not found in str_table characters
    e.g. t!t%ttttAACCG --> GCCAATTTTTT
    """
    return _clean_sequence(sequence, str_table)[::-1]


def complement(sequence, str_table=SIMPLE_COMPLEMENTS_STR):
    """Complement sequence.

    Receives a DNA sequence and a str_table that defines valid (and
    complementary) bases
    Returns a string containing complementary bases as defined in
    str_table while removing non input_sequence characters
    e.g. t!t%ttttAACCG --> AAAAAATTGGC
    """
    sequence = _clean_sequence(sequence, str_table)
    complements = _complements(str_table)
    return "".join(complements[base] for base in sequence)


def reverse_complement(sequence, str_table=SIMPLE_COMPLEMENTS_STR):
    """Reverse-complement sequence.

    Receives a DNA sequence and a str_table that defines valid (and
    complementary) bases
    Returns a string containing complementary bases as defined in str_table
    while removing non input_sequence characters
    e.g. t!t%ttttAACCG --> CGGTTAAAAAA
    """
    sequence = _clean_sequence(
        sequence, str_table
    )  # not really necessary, but what the heck.
    return complement(reverse(sequence, str_table), str_table)
