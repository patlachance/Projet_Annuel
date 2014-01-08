from PyQt4 import QtGui, QtCore
import moteur

class ConfigurationFrame(QtGui.QWidget):
    """Fenetre de configuration"""

    def __init__(self, parent=None, centralWidget=None):

        super(ConfigurationFrame, self).__init__()

        self.parent = parent
        self.centralWidget = centralWidget
        self.nombreBrasLabel = QtGui.QLabel("Nombre de bras : ")
        self.nombreCoupsLabel = QtGui.QLabel("Nombre de coups : ")
        self.nombreBras = QtGui.QLineEdit()
        self.nombreCoups = QtGui.QLineEdit()
        self.radioButtonGroup = QtGui.QButtonGroup()
        self.configurationLabel = QtGui.QLabel("Configuration :")
        self.radioButtonClassique = QtGui.QRadioButton("Classique")
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

        self.validate = QtGui.QPushButton("Valider")
        self.cancel = QtGui.QPushButton("Annuler")

        self.showDialogConfiguration()

    def showDialogConfiguration(self):

        self.setWindowTitle("Fenêtre de configuration")
        gridLayout = QtGui.QGridLayout()
        gridLayout.setSpacing(10)

        font = QtGui.QFont("Times", 14, QtGui.QFont.Bold, True)
        font.setUnderline(True)

        self.radioButtonClassique.setChecked(True)
        self.nombrePermutationLabel.hide()
        self.nombreIntervalleLabel.hide()
        self.permutationLineEdit.hide()
        self.intervalleLineEdit.hide()

        self.radioButtonGroup.addButton(self.radioButtonClassique)
        self.radioButtonGroup.addButton(self.radioButtonDynamique)
        self.radioButtonGroup.addButton(self.radioButtonDiminution)

        listAlgorithme = [self.algoJoueur, self.algoHasard, self.algoGlouton, self.algoEpsilonGlouton, self.algoMoyenneGain, self.algoUCB]

        self.setCheckedAlgoBox(listAlgorithme, self.centralWidget.moteurJeu.listAlgorithme)

        self.algorithmeLabel.setFont(font)

        gridLayout.addWidget(self.nombreBrasLabel, 0, 0)
        gridLayout.addWidget(self.nombreBras, 0, 1)
        gridLayout.addWidget(self.nombreCoupsLabel, 1, 0)
        gridLayout.addWidget(self.nombreCoups, 1, 1)
        gridLayout.addWidget(self.configurationLabel, 2, 0, 1, 0)
        gridLayout.addWidget(self.radioButtonClassique, 3, 0)
        gridLayout.addWidget(self.radioButtonDynamique, 3, 1)
        gridLayout.addWidget(self.radioButtonDiminution, 3, 2)
        gridLayout.addWidget(self.nombrePermutationLabel, 4, 0, 1, 0)
        gridLayout.addWidget(self.permutationLineEdit, 4, 2)
        gridLayout.addWidget(self.nombreIntervalleLabel, 4, 0, 1, 0)
        gridLayout.addWidget(self.intervalleLineEdit, 4, 2)
        gridLayout.addWidget(self.algorithmeLabel, 5, 0, 1, 0, QtCore.Qt.AlignCenter)
        gridLayout.addWidget(self.algoJoueur, 6, 0)
        gridLayout.addWidget(self.algoHasard, 6, 1)
        gridLayout.addWidget(self.algoGlouton, 7, 0)
        gridLayout.addWidget(self.algoEpsilonGlouton, 7, 1)
        gridLayout.addWidget(self.algoMoyenneGain, 8, 0)
        gridLayout.addWidget(self.algoUCB, 8, 1)
        gridLayout.addWidget(self.cancel, 9, 0)
        gridLayout.addWidget(self.validate, 9, 1)

        self.nombreBras.setText(str(self.centralWidget.moteurJeu.nbBras))
        self.nombreCoups.setText(str(self.centralWidget.moteurJeu.nbCoupsMax))
        self.permutationLineEdit.setText(str(self.centralWidget.moteurJeu.permutation))
        self.intervalleLineEdit.setText(str(self.centralWidget.moteurJeu.intervalle))

        # Events
        self.cancel.clicked.connect(self.close)
        self.validate.clicked.connect(lambda: self.validateConfiguration(listAlgorithme))
        self.cancel.setFocusPolicy(QtCore.Qt.NoFocus)
        self.radioButtonClassique.clicked.connect(self.checkValidityLineEdit)
        self.radioButtonDynamique.clicked.connect(self.checkValidityLineEdit)
        self.radioButtonDiminution.clicked.connect(self.checkValidityLineEdit)
        self.nombreBras.textEdited.connect(self.checkValidityLineEdit)
        self.nombreCoups.textEdited.connect(self.checkValidityLineEdit)

        self.setLayout(gridLayout)
        self.setFixedSize(self.sizeHint())

    def setCheckedAlgoBox(self, listAlgorithme, listAlgoNumber):
        """Coche les checkbox selon la présence ou non des algorithmes"""

        for i in range(0, len(listAlgoNumber)):
            listAlgorithme[i].setChecked(True)

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

            self.permutationLineEdit.textEdited.connect(self.checkValidityLineEdit)

        if sender == self.radioButtonDiminution:
            self.nombrePermutationLabel.hide()
            self.permutationLineEdit.hide()
            self.nombreIntervalleLabel.show()
            self.intervalleLineEdit.show()

            self.intervalleLineEdit.textEdited.connect(self.checkValidityLineEdit)

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


    def validateConfiguration(self, listAlgorithme):
        """Valide la configuration envoyée"""

        listAlgoNumber = []

        #Penser à modifier la range en fonction du nombre d'algo
        for algo, i in zip(listAlgorithme, range(0, 6)):
            if algo.isChecked():
                listAlgoNumber.append(i)

        if self.radioButtonClassique.isChecked():
            self.parent.initCentralWidget(moteur.Moteur(int(self.nombreBras.displayText()), int(self.nombreCoups.displayText()), listAlgoNumber, 0))
        elif self.radioButtonDynamique.isChecked():
            self.parent.initCentralWidget(moteur.Moteur(int(self.nombreBras.displayText()), int(self.nombreCoups.displayText()), listAlgoNumber, 1, int(self.permutationLineEdit.displayText())))
        elif self.radioButtonDiminution.isChecked():
            self.parent.initCentralWidget(moteur.Moteur(int(self.nombreBras.displayText()), int(self.nombreCoups.displayText()), listAlgoNumber, 2, int(self.intervalleLineEdit.displayText())))

        self.close()

        if listAlgoNumber[0] != 0:
            self.centralWidget.auto()


    def showConfigurationFrame(self):
        self.show()