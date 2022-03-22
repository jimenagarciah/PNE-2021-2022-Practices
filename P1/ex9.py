from Seq1 import Seq
import os

print("-----| Exercise 9 |------")
s = Seq()
s.read_fasta("../session-04/U5.txt")
print(f"Sequence: (Length: {s.len()}) {s}")
print(f"\tBases {s.count()}")
print(f"\tRev {s.reverse()}")
print(f"\tComp {s.complement()}")

