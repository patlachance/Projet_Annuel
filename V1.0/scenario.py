import gameZone
import bras

class Scenario:
    """Classe dédiée aux scenarios"""

    def __init__(self, pathFile):

        self.pathFile = pathFile
        self.configuration = []
        self.listes_bras = []

    def loadScenario(self):
        """Creer un nouveau jeu selon un scenario predefini """

        configuration_list = []

        with open(self.pathFile, 'r') as openFile:
            for line in openFile.read().splitlines():
                if line != '':
                   configuration_list.append(line)

        self.convertConfiguration(configuration_list)

    def convertConfiguration(self, configuration_list):
        """Converti les données recupérés d'un fichier scénario"""

        self.configuration.append(int(configuration_list[0]))
        self.configuration.append(int(configuration_list[1]))

        list_algorithme = []

        for i in configuration_list[2]:
            if i not in [' ', ',', '[', ']']:
                list_algorithme.append(int(i))

        self.configuration.append(list_algorithme)

        config_bras = configuration_list[3:]

        list_changement = []
        index_changement = 0

        if len(config_bras) != 0:
            for i in config_bras:
                if i[0] == "#":
                    list_changement.append((index_changement, int(i[1:])))

                index_changement += 1

        self.createListBras(config_bras, list_changement)



    def createListBras(self, config_bras, list_changement):
        """Crée une liste de bras"""

        for i in range(0, len(list_changement)):
            liste_bras = []


            if i != len(list_changement) - 1:
                for j in range(list_changement[i][0] + 1, list_changement[i + 1][0]):
                    parametre_bras = config_bras[j].split(" ")
                    liste_bras.append(bras.Bras(float(parametre_bras[0]), float(parametre_bras[1])))

                if j != self.configuration[0]:
                    for k in range(j, self.configuration[0]):
                        liste_bras.append(bras.Bras())
            else:
                l = 0
                for j in config_bras[list_changement[i][0] + 1:]:
                    parametre_bras = j.split(" ")
                    liste_bras.append(bras.Bras(float(parametre_bras[0]), float(parametre_bras[1])))
                    l += 1

                if l != self.configuration[0]:
                    for k in range(l, self.configuration[0]):
                        liste_bras.append(bras.Bras())

            self.listes_bras.append(liste_bras)

