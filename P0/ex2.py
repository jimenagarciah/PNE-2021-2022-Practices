
from Seq0 import *

FOLDER = "../Session-04/"

filename = input("File's name: ")
print(f"DNA file: {filename}")
sequence = seq_read_fasta(FOLDER + filename)
#"../Session-04/U5.txt"
print(f"The first 20 bases are: ")
print(sequence[:20])

