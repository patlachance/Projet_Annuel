import gameZone

class Scenario:
    """Classe dédiée aux scenarios"""

    def __init__(self, pathFile):

        self.pathFile = pathFile
        self.configuration = []

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



