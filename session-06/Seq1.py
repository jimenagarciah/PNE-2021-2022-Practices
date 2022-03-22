class Seq:
    """A class for representing sequences"""
    BASES_ALLOWED = ['A', 'C', 'G', 'T'] #propiedad o atributo de clas(estático)

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

    def __init__(self, bases):
        if Seq.are_bases_valid(bases):
            self.bases = bases
            print("New sequence created!")
        else:
            self.bases = "ERROR"
            print("INCORRECT Sequence detected")

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

    def __str__(self):
        return self.name + "-" + self.bases

