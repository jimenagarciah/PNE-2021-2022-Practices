class Seq:
    """A class for representing sequences"""
    BASES_ALLOWED = ['A', 'C', 'G', 'T'] #propiedad o atributo de clas(estático)
    BASES_COMPLEMENTS = {"A": "T", "C": "G", "T": "A", "G": "C"}

    @staticmethod #funcion o metodo de clase (estático)
    def are_bases_valid(bases):
        valid = len(bases) != 0
        i = 0
        while valid and i < len(bases):
            if bases[i] in Seq.BASES_ALLOWED: #tienes que poner por delante el nombre de la clas
                i += 1
            else:
                valid = False
        return valid

    def __init__(self, bases="NULL"):
        if bases == "NULL":
            self.bases = bases
            print("NULL sequence created!")
        elif Seq.are_bases_valid(bases):
            self.bases = bases
            print("New sequence created!")
        else:
            self.bases = "ERROR"
            print("INVALID seq!")

    def __str__(self):
        return self.bases

    def len(self):
        if self.bases == "NULL" or self.bases == "ERROR":
            return 0
        return len(self.bases)

    def count_base(self, base):
        if self.bases == "NULL" or self.bases == "ERROR":
            return 0
        return self.bases.count(base)

    def count(self):
        result ={}
        for base in Seq.BASES_ALLOWED:
            result[base] = self.count_base(base)
        return result

    def reverse(self):
        if self.bases == "NULL" or self.bases == "ERROR":
            return self.bases
        return self.bases[::-1]

    def complement(self):
        if self.bases == "NULL" or self.bases == "ERROR":
            return self.bases

        result = ""
        for base in self.bases:
            result += Seq.BASES_COMPLEMENTS[base]
        return result

    def read_fasta(self, file_name):
        from pathlib import Path
        file_contents = Path(file_name).read_text()
        lines = file_contents.splitlines()
        body = lines[1:]
        self.bases = ""
        for line in body:
            self.bases += line



