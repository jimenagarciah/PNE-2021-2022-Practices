from Seq1 import Seq
print("-----| Practice 1, Exercise 6 |------")

s1 = Seq()
s2 = Seq("ACTGA")
s3 = Seq("Invalid sequence")

print(f"Sequence 1: (length: {s1.len()}) {s1} \n ({s1.count()})")
print(f"Sequence 2: (length: {s2.len()}) {s2} \n ({s2.count()})")
print(f"Sequence 3: (length: {s3.len()}) {s3} \n ({s3.count()})")