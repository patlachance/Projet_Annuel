import moteur
import bras

class ScenarioLoader:
    """Classe dédiée aux scenarios"""

    def __init__(self, pathFile):

        #Un scenario est decrit :
        #1: nombre de bras
        #2: nombre de coups
        #3: liste algorithme
        #4: configuration (0:classique, 1:dynamique, 2:diminution)
            #si classique liste bras
            #si dynamique palier de permutation + liste bras
            #si diminution intervalle + liste bras
        #5: si # bras generes aléatoirement sinon listes de bras

        self.pathFile = pathFile
        self.nombre_bras = 0
        self.nombre_coups = 0
        self.liste_algorithme = []
        self.option = 0 #peut prendre 0 = Classique, 1 = Dynamique, 2 = Diminution
        self.liste_bras = []
        self.intervalle = 0
        self.permutation = 0

    def loadScenario(self):
        """Creer un nouveau jeu selon un scenario predefini """

        configuration_list = []

        with open(self.pathFile, 'r') as openFile:
            for line in openFile.read().splitlines():
                if line != '':
                    configuration_list.append(line)

        return configuration_list

    def initialiseConfiguration(self, configuration_list):
        """Converti les données recupérés d'un fichier scénario"""

        self.nombre_bras = int(configuration_list[0])
        self.nombre_coups = int(configuration_list[1])

        for i in configuration_list[2]:
            if i not in [' ', ',', '[', ']']:
                self.liste_algorithme.append(int(i))

        self.option = int(configuration_list[3])

        if self.option == 0:

            for i in configuration_list[4:]:
                line = i.split(' ')
                self.liste_bras.append(bras.Bras(float(line[0]), float(line[1])))

            return moteur.Moteur(self.nombre_bras, self.nombre_coups, self.liste_algorithme, self.option, self.liste_bras)

        elif self.option == 1:
            self.permutation = int(configuration_list[4])

            for i in configuration_list[5:]:
                line = i.split(' ')
                self.liste_bras.append(bras.Bras(float(line[0]), float(line[1])))

            return moteur.Moteur(self.nombre_bras, self.nombre_coups, self.liste_algorithme, self.option, self.permutation, self.liste_bras)

        else:
            self.intervalle = int(configuration_list[4])

            for i in configuration_list[5:]:
                line = i.split(' ')
                self.liste_bras.append(bras.Bras(float(line[0]), float(line[1])))

            return moteur.Moteur(self.nombre_bras, self.nombre_coups, self.liste_algorithme, self.option, self.intervalle, self.liste_bras)