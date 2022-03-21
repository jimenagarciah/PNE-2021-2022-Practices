class Seq:
    """A class for representing sequences"""
    def __init__(self, bases):
        self.bases = bases
        print("New sequence created!")
    def __str__(self):
        return self.bases
    def len(self):
        return len(self.bases)

class Gene(Seq): #se heredan todas menos la de __init__
    """This class is derived from the Seq Class
       All the objects of class Gene will inheritate
       the methods from the Seq class
    """
    def __init__(self, bases, name=""):
        super().__init__(bases)
        self.name = name
        print("New gene created!")


# --- Main program
s = Seq("AGTACACTGGT")
g = Gene("CGTAAC", "FRAT1")

# -- Printing the objects
print(f"Sequence 1: {s}")
print(f"Gene: {g}")