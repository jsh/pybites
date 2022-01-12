"""Bite 262. GC content."""


def calculate_gc_content(sequence: str) -> float:
    """Calculate GC content of DNA string.

    Receives a DNA sequence (A, G, C, or T)
    Returns the percentage of GC content (rounded to the last two digits)
    """
    bases = {"A", "C", "G", "T"}
    sequence = sequence.upper()
    count = {base: sequence.count(base) for base in bases}
    total_count = sum(count.values())
    gc_content = (count["G"] + count["C"]) / total_count
    return round(gc_content * 100, 2)
