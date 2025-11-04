RNA_MAP = {
    "G": "C",
    "C": "G",
    "T": "A",
    "A": "U"
}

def to_rna(dna_strand):
    return "".join(RNA_MAP[base] for base in dna_strand)