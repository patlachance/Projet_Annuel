from random import shuffle
import bras
import algorithme


class Moteur:
    """Représente le moteur"""

    nbAlgorithme = 6

    def __init__(self, *args):

        #args[0] = nbBras
        #args[1] = nbCoups
        #args[2] = listAlgorithme
        #args[3] = option
        #args[4] = intervalle ou permutation
        #args[5] = listBras


        self.nbBras = args[0]
        self.nbCoupsMax = args[1]
        self.listAlgorithme = []
        self.option = args[3]
        self.intervalle = 0
        self.permutation = 0
        self.listBras = []


        #Initialistion du choix du type de configuration & des options inhérentes
        if self.option == 1:
            if len(args) >= 5:
                self.permutation = args[4]
            else:
                self.permutation = self.nbCoupsMax / 2 + 1
        elif self.option == 2:
            if len(args) >= 5:
                self.intervalle = args[4]
            else:
                self.intervalle = 4 #valeur par défaut

        if self.option == 0:
            if len(args) == 5:
                self.listBras = args[4]
            else:
                #Initialisation de la liste listBras
                for i in range(0, self.nbBras):
                    self.listBras.append(bras.Bras())

        elif self.option == 1 or self.option == 2:
            if len(args) == 6:
                self.listBras = args[5]
            else:
                #Initialisation de la liste listBras
                for i in range(0, self.nbBras):
                    self.listBras.append(bras.Bras())

        #initialisation des algorithmes.
        for i in args[2]:
            self.listAlgorithme.append(algorithme.Algorithme(self.nbCoupsMax, self.listBras, self.intervalle, i))
        

    # Cette fonction retourne l'espérance du bras demandé pour le joueur.
    def esperanceJoueur(self, num):
        return self.listAlgorithme[0].esperanceCalculee(num)
        
    # Cette fonction retourne le nombre de fois que le joueur a actionné le bras
    def nombreFoisJoueBrasJoueur(self, num):
        """Retourne le nombre de fois que le bras a été actionné"""
        return self.listAlgorithme[0].listBras[num].nbFoisActionne

    # Cette fonction retourne le nombre de fois que le joueur a joué
    def nombreCoupsJoue(self):
        """Cette fonction retourne le nombre de fois que le joueur a joué"""
        return self.listAlgorithme[0].nbCoupsJoue

    # Cette fonction retourne le gain total du joueur
    def gain(self, num):
        return self.listAlgorithme[num].gain
    
    # Cette fonction actionne le bras demandé du joueur.
    def actionnerBrasJoueur(self, numeroBras):
        self.listAlgorithme[0].actionnerBras(numeroBras)

    # Cette fonction lance les algorithmes qui actionneront un bras 
    def lancerAlgo(self, tmp):
        for i in range(tmp, len(self.listAlgorithme)):
              self.listAlgorithme[i].lancerAlgo()

    # Cette fonction retourne le gain esperé.
    def gainEspere(self):        
        algoGainEspere = algorithme.Algorithme(self.nbCoupsMax, self.listBras, self.intervalle, -1)
        
        algoGainEspere.lancerAlgoEntierement()
        return algoGainEspere.gain


    def permutationBras(self):
        """Permute les bras"""

        value_list = []

        for i in self.listBras:
            value_list.append((i.proba, i.gain))

        shuffle(value_list)

        for i in range(0, self.nbBras):
            self.listBras[i].proba = value_list[i][0]
            self.listBras[i].gain = value_list[i][1]

        # Je redéfinis les bras de chaque algorithme.
        for i in self.listAlgorithme:
            i.redefinirBras(self.listBras)


