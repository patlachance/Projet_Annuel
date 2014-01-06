import random

class Bras:
    """Représente une machine à sous avec ses propriétés"""
    def __init__(self, *args):
        #args[0] = proba
        #args[1] = gain

        if len(args) == 2:
            self.proba = args[0]
            self.gain = args[1]
        else:
            # proba et gain definis entre 0 et 1.
            self.proba = random.random()
            self.gain = random.random()

        # variable indiquant la somme gagnée à l'aide de ce bras
        self.gainObtenu = 0

        # variable indiquant le nombre de fois que ce bras a été actionné
        self.nbFoisActionne = 0

    # Fonction retournant la somme gagnée en actionnant le bras 
    def actionner(self):
        self.nbFoisActionne += 1
        tmp = random.random()

        # Si on gagne
        if (tmp <= self.proba):
            self.gainObtenu += self.gain
            return self.gain
        #sinon
        else:
            return 0

    # retourne l'espérance. Nécessaire pour les algorithmes.
    def esperanceCalculee(self):
        if self.nbFoisActionne == 0:
            return 0
        else:
            return self.gainObtenu / self.nbFoisActionne

    # retourne la VERITABLE espérance
    def esperanceVeritable(self):
        return self.proba * self.gain

    # réinitialise le gain et la proba de gain du bras
    def reinitialiser(self):
        # proba et gain definis entre 0 et 1.
        self.proba = random.random()
        self.gain = random.random()

    # Redéfinit le bras.
    def definir(self, g, p):
        self.gain = g
        self.proba = p


