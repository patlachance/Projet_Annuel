import bras
import algorithme

class Moteur:
    """Représente le moteur"""

    def __init__(self, nbBras, nbCoupsMax, listAlgo):

        self.nbBras = nbBras
        self.nbCoupsMax = nbCoupsMax
        self.listBras = []
        self.listAlgorithme = []
        
        self.nbAlgorithme = 6

        #Initialisation de la liste listBras
        for i in range(0,nbBras):
            self.listBras.append(bras.Bras())	

        #initialisation des algorithmes.

        for i in range(0,len(listAlgo)):
            self.listAlgorithme.append(algorithme.Algorithme(self.nbCoupsMax, self.listBras, listAlgo[i]))
        

    # Cette fonction retourne l'espérance du bras demandé pour le joueur.
    def esperanceJoueur(self, num):
        return self.listAlgorithme[0].esperanceCalculee(num)
        
    # Cette fonction retourne le nombre de fois que le joueur a actionné le bras
    def nombreFoisJoueBrasJoueur(self, num):
        """Retourne le nombre de fois que le bras a été actionné"""
        return self.listAlgorithme[0].listBras[num].nbFoisActionne

    # Cette fonction retourne le nombre de fois que le joueur a joué
    def nombreCoupsJoue(self):
        """Retourne le nombre de fois que le bras a été actionné"""
        return self.listAlgorithme[0].nbCoupsJoue


    # Cette fonction retourne le gain total du joueur
    def gain(self, num):
        return self.listAlgorithme[num].gain
    
    # Cette fonction actionne le bras demandé du joueur.
    def actionnerBrasJoueur(self, numeroBras):
        self.listAlgorithme[0].actionnerBras(numeroBras)
        self.changerBras()

    # Cette fonction lance les algorithmes qui actionneront un bras 
    def lancerAlgo(self):
         for i in range(1,len(self.listAlgorithme)):
              self.listAlgorithme[i].lancerAlgo()

    # Cette fonction retourne le gain esperé.
    def gainEspere(self):        
        algoGainEspere = algorithme.Algorithme(self.nbCoupsMax, self.listBras, -1)
        
        algoGainEspere.lancerAlgoEntierement()
        return algoGainEspere.gain

    # Cette fonction change la proba de gain et le gain de chaque bras. 
    def changerBras(self):
        for i in range(0,self.nbBras):
            self.listBras[i].reinitialiser()

        # Je redéfinis les bras de chaque algorithme.
        for i in range(0,self.nbAlgorithme):
            self.listAlgorithme[i].redefinirBras(self.listBras)
        
