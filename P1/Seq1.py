class Seq:
    """A class for representing sequences"""
    def __init__(self, bases):
        self.bases = bases
        print("New sequence created!")
    def __str__(self):
        return self.bases
    def len(self):
        return len(self.bases)


s1 = Seq("AGTACACTGGT")
s2 = Seq("CGTAAC")

print(f"Sequence 1: {s1}")
print(f"  Length: {s1.len()}")
print(f"Sequence 2: {s2}")
print(f"  Length: {s2.len()}")