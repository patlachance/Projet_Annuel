from PyQt4 import QtGui, QtCore
import guiBras
import random
import moteur
import bras


class ScenarioCreator (QtGui.QDialog):
    """Classe pour la création de scenario"""

    def __init__(self, parent=None, centralWidget=None):

        super(ScenarioCreator, self).__init__(parent)

        self.parent = parent
        self.centralWidget = centralWidget
        self.listGuiBras = []
        self.nombreBrasLabel = QtGui.QLabel("Nombre de bras : ")
        self.nombreCoupsLabel = QtGui.QLabel("Nombre de coups : ")
        self.nombreBras = QtGui.QLineEdit()
        self.nombreCoups = QtGui.QLineEdit()
        self.radioButtonGroup = QtGui.QButtonGroup()
        self.configurationLabel = QtGui.QLabel("Configuration :")
        self.radioButtonClassique = QtGui.QRadioButton("Statique")
        self.radioButtonDynamique = QtGui.QRadioButton("Dynamique")
        self.radioButtonDiminution = QtGui.QRadioButton("Diminution")
        self.nombrePermutationLabel = QtGui.QLabel("Fréquence des permutations : ")
        self.nombreIntervalleLabel = QtGui.QLabel("Intervalle de diminution : ")
        self.permutationLineEdit = QtGui.QLineEdit()
        self.intervalleLineEdit = QtGui.QLineEdit()
        self.algorithmeLabel = QtGui.QLabel("Algorithmes")
        self.algoJoueur = QtGui.QCheckBox("Joueur")
        self.algoHasard = QtGui.QCheckBox("Hasard")
        self.algoGlouton = QtGui.QCheckBox("Glouton")
        self.algoEpsilonGlouton = QtGui.QCheckBox("Epsilon glouton")
        self.algoMoyenneGain = QtGui.QCheckBox("Moyenne gain")
        self.algoUCB = QtGui.QCheckBox("UCB1")

        self.scrollArea = None
        self.vMainLayout = QtGui.QVBoxLayout()
        self.gridLayoutConfigBras = QtGui.QGridLayout()
        self.validate = QtGui.QPushButton("Valider")
        self.cancel = QtGui.QPushButton("Annuler")
        self.save = QtGui.QPushButton("Sauvegarder")

        self.showDialogConfiguration()

    def showDialogConfiguration(self):

        self.setWindowTitle("Fenêtre de configuration")


        gridLayout1 = QtGui.QGridLayout()
        vLayout2 = QtGui.QVBoxLayout()
        gridLayoutAlgo = QtGui.QGridLayout()
        hlayoutup = QtGui.QHBoxLayout()
        hlayoutConfiguration = QtGui.QHBoxLayout()
        hlayoutWindowButton = QtGui.QHBoxLayout()

        font = QtGui.QFont("Times", 14, QtGui.QFont.Bold, True)

        self.radioButtonClassique.setChecked(True)
        self.nombrePermutationLabel.hide()
        self.nombreIntervalleLabel.hide()
        self.permutationLineEdit.hide()
        self.intervalleLineEdit.hide()

        self.radioButtonGroup.addButton(self.radioButtonClassique)
        self.radioButtonGroup.addButton(self.radioButtonDynamique)
        self.radioButtonGroup.addButton(self.radioButtonDiminution)

        self.algorithmeLabel.setFont(font)
        self.configurationLabel.setFont(font)

        gridLayout1.addWidget(self.nombreBrasLabel, 0, 0)
        gridLayout1.addWidget(self.nombreBras, 0, 1)
        gridLayout1.addWidget(self.nombreCoupsLabel, 1, 0)
        gridLayout1.addWidget(self.nombreCoups, 1, 1)
        gridLayout1.setRowStretch(2, 0)

        vLayout2.addWidget(self.radioButtonClassique)
        vLayout2.addWidget(self.radioButtonDynamique)
        vLayout2.addWidget(self.radioButtonDiminution)
        vLayout2.addLayout(hlayoutConfiguration)

        hlayoutConfiguration.addWidget(self.nombrePermutationLabel)
        hlayoutConfiguration.addWidget(self.permutationLineEdit)
        hlayoutConfiguration.addWidget(self.nombreIntervalleLabel)
        hlayoutConfiguration.addWidget(self.intervalleLineEdit)

        gridLayoutAlgo.addWidget(self.algorithmeLabel, 0, 0)
        gridLayoutAlgo.addWidget(self.algoJoueur, 1, 0)
        gridLayoutAlgo.addWidget(self.algoHasard, 1, 1)
        gridLayoutAlgo.addWidget(self.algoGlouton, 2, 0)
        gridLayoutAlgo.addWidget(self.algoEpsilonGlouton, 2, 1,)
        gridLayoutAlgo.addWidget(self.algoMoyenneGain, 3, 0)
        gridLayoutAlgo.addWidget(self.algoUCB, 3, 1)
        gridLayoutAlgo.setColumnStretch(4, 1)

        hlayoutWindowButton.addWidget(self.cancel)
        hlayoutWindowButton.addWidget(self.validate)
        hlayoutWindowButton.addWidget(self.save)

        self.nombreBras.setText("5")
        self.nombreCoups.setText("10")
        self.permutationLineEdit.setText("5")
        self.intervalleLineEdit.setText("4")
        self.algoJoueur.setChecked(True)
        self.algoHasard.setChecked(True)
        self.algoGlouton.setChecked(True)
        self.algoEpsilonGlouton.setChecked(True)
        self.algoMoyenneGain.setChecked(True)
        self.algoUCB.setChecked(True)

        self.nombreBras.setFixedWidth(100)
        self.nombreCoups.setFixedWidth(100)
        self.permutationLineEdit.setFixedWidth(75)
        self.intervalleLineEdit.setFixedWidth(75)
        self.cancel.setFixedWidth(75)
        self.validate.setFixedWidth(75)
        self.save.setFixedWidth(100)

        hlayoutup.addLayout(gridLayout1)
        hlayoutup.addStretch(1)
        hlayoutup.addLayout(vLayout2)
        hlayoutup.addStretch(1)
        hlayoutup.addLayout(gridLayoutAlgo)

        self.vMainLayout.addLayout(hlayoutup)

        self.createWidgetConfigurationBras()
        self.vMainLayout.addLayout(hlayoutWindowButton)

        listAlgorithme = [self.algoJoueur, self.algoHasard, self.algoGlouton, self.algoEpsilonGlouton, self.algoMoyenneGain, self.algoUCB]
        self.setCheckedAlgoBox(listAlgorithme, self.centralWidget.moteurJeu.listAlgorithme)

        # Events
        self.cancel.clicked.connect(self.close)
        self.validate.clicked.connect(lambda: self.validateConfiguration(listAlgorithme))
        self.save.clicked.connect(self.saveScenario)
        self.cancel.setFocusPolicy(QtCore.Qt.NoFocus)
        self.radioButtonClassique.clicked.connect(self.checkValidityLineEdit)
        self.radioButtonDynamique.clicked.connect(self.checkValidityLineEdit)
        self.radioButtonDiminution.clicked.connect(self.checkValidityLineEdit)
        self.nombreBras.textEdited.connect(self.checkValidityLineEdit)
        self.nombreBras.textEdited.connect(self.createDynamicArms)
        self.nombreCoups.textEdited.connect(self.checkValidityLineEdit)

        self.setLayout(self.vMainLayout)
        self.setGeometry(100, 100, 1100, 600)


    def setCheckedAlgoBox(self, listAlgorithme, listAlgoNumber):
        """Coche les checkbox selon la présence ou non des algorithmes"""

        for i in range(0, len(listAlgoNumber)):
            listAlgorithme[i].setChecked(True)

    def validateConfiguration(self, listAlgorithme):
        """Valide la configuration envoyée"""

        listAlgoNumber = []

        #Penser à modifier la range en fonction du nombre d'algo
        for algo, i in zip(listAlgorithme, range(0, 6)):
            if algo.isChecked():
                listAlgoNumber.append(i)

        self.attributeValueForEmptyGuiBras()
        liste_bras = self.createListBras()

        if self.radioButtonClassique.isChecked():
            self.parent.initCentralWidget(moteur.Moteur(int(self.nombreBras.displayText()), int(self.nombreCoups.displayText()), listAlgoNumber, 0, liste_bras))
        elif self.radioButtonDynamique.isChecked():
            self.parent.initCentralWidget(moteur.Moteur(int(self.nombreBras.displayText()), int(self.nombreCoups.displayText()), listAlgoNumber, 1, int(self.permutationLineEdit.displayText()), liste_bras))
        elif self.radioButtonDiminution.isChecked():
            self.parent.initCentralWidget(moteur.Moteur(int(self.nombreBras.displayText()), int(self.nombreCoups.displayText()), listAlgoNumber, 2, int(self.intervalleLineEdit.displayText()), liste_bras))

        self.close()

        if listAlgoNumber[0] != 0:
            self.centralWidget.auto()

    def checkValidityLineEdit(self):

        sender = self.sender()

        if sender == self.radioButtonClassique:
            self.nombrePermutationLabel.hide()
            self.permutationLineEdit.hide()
            self.nombreIntervalleLabel.hide()
            self.intervalleLineEdit.hide()

        if sender == self.radioButtonDynamique:
            self.nombrePermutationLabel.show()
            self.permutationLineEdit.show()
            self.nombreIntervalleLabel.hide()
            self.intervalleLineEdit.hide()

        if sender == self.radioButtonDiminution:
            self.nombrePermutationLabel.hide()
            self.permutationLineEdit.hide()
            self.nombreIntervalleLabel.show()
            self.intervalleLineEdit.show()

        numberArm = 0
        numberBlow = 0
        intervalle = 0
        permutation = 0

        validity = True

        try:
            numberArm = int(self.nombreBras.displayText())
            numberBlow = int(self.nombreCoups.displayText())

            if self.permutationLineEdit.isVisible():
                permutation = int(self.permutationLineEdit.displayText())

            if self.intervalleLineEdit.isVisible():
                intervalle = int(self.intervalleLineEdit.displayText())

        except ValueError:
            validity = False
        finally:
            if numberArm < 1 or numberBlow < 1 or permutation < 0 or intervalle < 0:
                validity = False

            self.emit(QtCore.SIGNAL(self.validate.setDisabled(not validity)))
            self.emit(QtCore.SIGNAL(self.save.setDisabled(not validity)))


    def createDynamicArms(self):

        numberArm = 0
        validity = True

        try:
            numberArm = int(self.nombreBras.displayText())
        except:
            validity = False
        finally:
            if numberArm < 1:
                validity = False

        if validity:
            self.vMainLayout.removeWidget(self.scrollArea)
            self.createWidgetConfigurationBras()

    def configurationBras(self):

        nombreBras = int(self.nombreBras.displayText())
        gridLayout = QtGui.QGridLayout()
        listBras =[]

        for i in range(0, nombreBras):
            b = guiBras.GuiBras(self.validate, self.save)
            b.setLabelBras(i)
            b.setInfoGuiBras(i, '', '')
            listBras.append(b.getInfoGuiBras())
            gridLayout.addWidget(b, int(i / 2), int(i % 2))
        self.gridLayoutConfigBras = gridLayout
        self.listGuiBras = listBras


    def createWidgetConfigurationBras(self):

        self.scrollArea = QtGui.QScrollArea()
        configurationBrasWidget = QtGui.QWidget()
        self.configurationBras()
        configurationBrasWidget.setLayout(self.gridLayoutConfigBras)
        self.scrollArea.setWidget(configurationBrasWidget)
        self.vMainLayout.insertWidget(1, self.scrollArea)

    def getAlgorithmeSelected(self):

        listAlgorithme = ""

        if self.algoJoueur.isChecked():
            listAlgorithme += '0 '

        if self.algoHasard.isChecked():
            listAlgorithme += '1 '

        if self.algoGlouton.isChecked():
            listAlgorithme += '2 '

        if self.algoEpsilonGlouton.isChecked():
            listAlgorithme += '3 '
        if self.algoMoyenneGain.isChecked():
            listAlgorithme += '4 '

        if self.algoUCB.isChecked():
            listAlgorithme += '5'

        return listAlgorithme

    def getOpion(self):

        if self.radioButtonClassique.isChecked():
            return 0
        elif self.radioButtonDynamique.isChecked():
            return 1
        else:
            return 2

    def saveScenario(self):

        saveTmp = QtGui.QFileDialog.getSaveFileName(self, "Save file", "", ".sc")
        with open(saveTmp, 'w') as writeFile:
            writeFile.write(self.nombreBras.displayText() + "\n")
            writeFile.write(self.nombreCoups.displayText() + "\n")
            writeFile.write(self.getAlgorithmeSelected() + "\n")
            writeFile.write(str(self.getOpion()) + "\n")
            if self.getOpion() == 1:
                writeFile.write(self.permutationLineEdit.displayText() + "\n")
            elif self.getOpion() == 2:
                writeFile.write(self.intervalleLineEdit.displayText() + "\n")

            self.attributeValueForEmptyGuiBras()

            for i in self.listGuiBras:
                string = str(i[1]) + " " + str(i[2]) + "\n"
                writeFile.write(string)

        self.close()

    def attributeValueForEmptyGuiBras(self):

        for i in self.listGuiBras:
            if type(i[1]) is str and type(i[2]) is str:
                i[1] = float(format(random.random(), ".2f"))
                i[2] = float(format(random.random(), ".2f"))
            elif type(i[2]) is str:
                i[2] = float(format(random.random(), ".2f"))
            elif type(i[1]) is str:
                i[1] = float(format(random.random(), ".2f"))

    def createListBras(self):

        liste_bras = []

        for i in self.listGuiBras:
            liste_bras.append(bras.Bras(i[1], i[2]))

        return liste_bras

    def showScenarioCreatorFrame(self):

        self.show()
