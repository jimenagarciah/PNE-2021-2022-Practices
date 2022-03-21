from Seq0 import *

FOLDER = "../Session-04/"
GENES = ["ADA", "FRAT1", "FXN", "RNU6_269P", "U5"]

print("-----| Exercise 3 |------")

for gene in GENES:
    filename = gene + ".txt"
    sequence = seq_read_fasta(FOLDER + filename)
    print(f"Gene {gene} ---> Length: {seq_len(sequence)}")


