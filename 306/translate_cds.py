"""Use translation table to translate coding sequence to protein."""
# TODO: Add imports


def translate_cds(cds: str, translation_table: str) -> str:
    """Translate coding sequence to protein.

    :param cds: str: DNA coding sequence (CDS)
    :param translation_table: str: translation table
        as defined in Bio.Seq.Seq.CodonTable.ambiguous_generic_by_name
    :return: str: Protein sequence
    """
    # TODO: Put your code here
