import random
import copy
from math import sqrt, log 

class Algorithme:
    """Classe mère des algorithmes."""

    def __init__(self, nbCoupsMax, listBras, numAlgo):
        self.gain=0
        self.nbCoupsJoue=0
        self.nbCoupsMax = nbCoupsMax
        
        self.listBras = copy.deepcopy(listBras)

        self.numAlgo = numAlgo
                  
    def actionnerBras(self, numeroBras):
        """ Cette fonction actionne le bras demandé. Sauf dans le cas du gain espéré où le gain est ajouté directement."""
        self.nbCoupsJoue += 1
        
        # Le gain est calculé différemment si il s'agit de l'algo utilisé pour connaître le gain espéré. En effet, nous voulons alors connaître la VERITABLE ESPERANCE.
        if (self.numAlgo == -1):
            self.gain += self.esperanceVeritable(numeroBras)
        else:        
            self.gain += self.listBras[numeroBras].actionner()
          

    def esperanceCalculee(self, numeroBras):
        """ Cette fonction retourne l'espérance calculée."""
        return self.listBras[numeroBras].esperanceCalculee()        

    def esperanceVeritable(self, numeroBras):
        """ Cette fonction retourn l'espérance véritable."""
        return self.listBras[numeroBras].esperanceVeritable()        

    def nbFoisActionne(self, numeroBras):
        """ Cette fonction retourn l'espérance véritable."""
        return self.listBras[numeroBras].nbFoisActionne       
        

    def redefinirBras(self, listBras):
        """Cette fonction redéfinit le gain et la proba de chaque bras"""
        for i in range(0, len(listBras) -1):
            self.listBras[i].definir(listBras[i].gain, listBras[i].proba)

    
    def lancerAlgo(self):
        """Cette fonction est appelée pour lancer l'algorithme, et actionner le bras ensuite."""
       

        if self.numAlgo == -1:
            res = self.algoGainEspere()
        if self.numAlgo == 1:
            res = self.algoHasard()
        if self.numAlgo == 2:
            res = self.algoGlouton()
        if self.numAlgo == 3:
            res = self.algoGloutonEpsilon()
        if self.numAlgo == 4:
            res = self.algoMoyenneGain()
        if self.numAlgo == 5:
            res = self.algoUCB()


        self.actionnerBras(res)

    def lancerAlgoEntierement(self):
        """Cette fonction est appelée pour lancer l'algorithme autant de fois que nbCoupsMax."""
        
        for i in range(0,self.nbCoupsMax):
            self.lancerAlgo()

    
    def algoGainEspere(self):
        """ Algorithme utilisé pour calculer le gain espéré"""    
        numeroMeilleurBras=-1
        gainMeilleurBras=-1

        # Pour chaque bras, je vais regarder la VERITABLE espérance et essayer de trouver le meilleur bras.
        for i in range(0,len(self.listBras)):
            if self.esperanceVeritable(i) > gainMeilleurBras:
                numeroMeilleurBras = i
                gainMeilleurBras = self.esperanceVeritable(i)

        return numeroMeilleurBras


    def algoHasard(self):
        """ Algorithme retournant un bras au hasard"""
        return random.randint(0,len(self.listBras)-1)

    def algoGlouton(self):
        """ Algorithme essayant dans un premier temps tous les bras, puis choisit le meilleur"""
        jeuApprentissage = 0.5 # 50% du nombre de coups max sera utilisé pour connaitre le meilleur bras.  
        if self.nbCoupsJoue < jeuApprentissage*self.nbCoupsMax :
            res = self.nbCoupsJoue % len(self.listBras)
        else:
            numeroMeilleurBras=-1
            gainMeilleurBras=-1

            # Pour chaque bras, je vais regarder l'espérance et essayer de trouver le meilleur bras.
            for i in range(0,len(self.listBras)):
                if self.listBras[i].esperanceCalculee() > gainMeilleurBras:
                    numeroMeilleurBras = i
                    gainMeilleurBras = self.listBras[i].esperanceCalculee()

            res = numeroMeilleurBras
        return res

    def algoGloutonEpsilon(self):
        """ Algorithme essayant dans un premier temps tous les bras, puis choisit le meilleur en essayant un autre bras au hasard de temps en temps"""
        jeuApprentissage = 0.5 # 50% du nombre de coups max sera utilisé pour connaitre le meilleur bras.  
        epsilon = 0.1 # une fois sur 10, l'algorithme jouera un coup au hasard.
        if self.nbCoupsJoue < jeuApprentissage*self.nbCoupsMax :
            res = self.nbCoupsJoue % len(self.listBras)
        else:
            numeroMeilleurBras=-1
            gainMeilleurBras=-1
            r = random.random()
            if r<epsilon:
                res = random.randint(0,len(self.listBras)-1)
            else:
                # Pour chaque bras, je vais regarder l'espérance et essayer de trouver le meilleur bras.
                for i in range(0,len(self.listBras)):
                    if self.listBras[i].esperanceCalculee() > gainMeilleurBras:
                        numeroMeilleurBras = i
                        gainMeilleurBras = self.listBras[i].esperanceCalculee()
                res = numeroMeilleurBras

        return res


    def algoMoyenneGain(self):
        """ Algorithme choisissant un bras au prorata de sa moyenne """
 
        jeuApprentissage = 0.5 # 50% du nombre de coups max sera utilisé pour connaitre le meilleur bras.  
        if self.nbCoupsJoue < jeuApprentissage*self.nbCoupsMax :
            res = self.nbCoupsJoue % len(self.listBras)
        else:
            #calcul de la somme des espérances
            sumEsperance = 0
            for i in range(0,len(self.listBras)):
                sumEsperance += self.esperanceCalculee(i)

            # nombre aléatoire calcul
            r = random.uniform(0,sumEsperance)

            somme=0
            i=0

            while somme < r:
                somme += self.esperanceCalculee(i)        
                if somme >= r:
                    res = i
                else:
                    i += 1

        return res


    def algoUCB(self):
        """ Algorithme utilisant l'UCB1. Cet algorithme choisit le bras ayant la meilleure (moyenne + variable) la variable diminuant si le nombre de fois que l'on actionne le bras augmente."""

        meilleurBras=-1
        gain = -1        

        # Au début, on actionne une fois chaque bras.
        if self.nbCoupsJoue < len(self.listBras):
            return self.nbCoupsJoue
        

        for k in range(0,len(self.listBras)):

            gainTmp = self.esperanceCalculee(k) + sqrt( 2 * log(self.nbCoupsJoue) / self.nbFoisActionne(k))

            if gainTmp >= gain:
                gain = gainTmp
                meilleurBras = k

        return meilleurBras
        

