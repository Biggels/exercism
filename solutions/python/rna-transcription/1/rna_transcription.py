def to_rna(dna_strand):
    rna_map = {
        "G": "C",
        "C": "G",
        "T": "A",
        "A": "U"
    }

    return "".join([rna_map[base] for base in dna_strand])