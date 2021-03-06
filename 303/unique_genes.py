"""Bite 303. Unique genes."""

import gzip
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
    if filename_in.endswith(".gz"):
        with gzip.open(filename_in, "rt") as f_in:
            all_lines = f_in.readlines()
        filename_in = filename_in[:-3]
        with open(filename_in, "w", encoding="utf-8") as f_out:
            f_out.writelines(all_lines)
    pat = re.compile(r"(\S+)\s\[locus_tag=(.*)]")
    record_list = defaultdict(list)
    gene_list = {}
    for record in SeqIO.parse(filename_in, "fasta"):
        gene = pat.match(record.description)[1].lower()
        locus_tag = pat.match(record.description)[2]
        seq = str(record.seq).upper()
        record_list[seq].append(locus_tag)
        if seq in gene_list and gene_list[seq] != gene:
            msg = f"Gene names differ between entries: '{gene_list[seq]}' vs. '{gene}'"
            raise NameError(msg)
        gene_list[seq] = gene
    record_list = sorted(record_list.items(), key=ntags, reverse=True)
    if filename_out.endswith(".gz"):
        f_out = gzip.open(filename_out, "wt")
    else:
        f_out = open(  # pylint: disable=consider-using-with
            filename_out, "w", encoding="utf-8"
        )

    for record in record_list:
        seq, locus_tags = record
        plural = "s" if len(locus_tags) > 1 else ""
        locus_tags = ",".join(locus_tags)
        gene = gene_list[seq]
        f_out.write(f">{gene} [locus_tag{plural}={locus_tags}]\n")
        f_out.write(f"{seq}\n")
