from Seq0 import *

FOLDER = "../Session-04/"
GENES = ["ADA", "FRAT1", "FXN", "RNU6_269P", "U5"]
BASES = ["A", "C", "T", "G"]

print("-----| Exercise 4 |------")

for gene in GENES:
    filename = gene + ".txt"
    sequence = seq_read_fasta(FOLDER + filename)
    print(f"Gene {gene}:")
    for base in BASES:
        print(f" {base}: {seq_count_base(sequence, base)}")
    print()
