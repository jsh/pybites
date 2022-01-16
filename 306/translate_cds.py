"""Use translation table to translate coding sequence to protein."""
# TODO: Add imports

import Bio.Seq  # type: ignore
from Bio.Data import CodonTable

# Note on Bio.Seq table ids: These can be found in the
# Seq.CodonTable.ambiguous_generic_by_name variable


def translate_cds(cds: str, translation_table: str) -> str:
    """Translate coding sequence to protein.

    :param cds: str: DNA coding sequence (CDS)
    :param translation_table: str: translation table
        as defined in Bio.Seq.Seq.CodonTable.ambiguous_generic_by_name
    :return: str: Protein sequence
    """
    table = CodonTable.unambiguous_dna_by_name[translation_table]
    assert cds[:3] in table.start_codons
    assert cds[-3:] in table.stop_codons

    aa_list =[]
    for first in range(0, len(cds)-3, 3):
        codon = cds[first:first+3]
        amino_acid = table.forward_table[codon]
        aa_list.append(amino_acid)
        protein = "".join(aa_list)
    return protein
