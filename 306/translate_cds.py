"""Use translation table to translate coding sequence to protein."""

from Bio.Seq import Seq # type: ignore
from Bio.Data import CodonTable

def translate_cds(cds: str, translation_table: str) -> str:
    """Translate coding sequence to protein.

    :param cds: str: DNA coding sequence (CDS)
    :param translation_table: str: translation table
        as defined in Bio.Seq.Seq.CodonTable.ambiguous_generic_by_name
    :return: str: Protein sequence
    """
    table = CodonTable.ambiguous_dna_by_name[translation_table]
    cds = "".join(cds.split())  # clean out whitespace
    coding_dna = Seq(cds)
    protein = coding_dna.translate(table, cds=True, to_stop=True)
    return str(protein)
