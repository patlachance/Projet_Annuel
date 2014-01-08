from PyQt4 import QtGui, QtCore
import moteur
import configurationFrame

class ScenarioCreator (QtGui.QWidget):
    """Classe pour la création de scenario"""

    def __init__(self, parent=None):

        super(ScenarioCreator, self).__init__()

        self.parent = parent
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

        vMainLayout = QtGui.QVBoxLayout()
        hlayoutBras = QtGui.QHBoxLayout()
        hLayoutCoups = QtGui.QHBoxLayout()
        hlayout = QtGui.QHBoxLayout()
        hlayoutConfiguration = QtGui.QHBoxLayout()

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


        self.algorithmeLabel.setFont(font)

        hlayoutBras.addWidget(self.nombreBrasLabel)
        hlayoutBras.addWidget(self.nombreBras)
        hlayoutBras.addStretch(1)

        hLayoutCoups.addWidget(self.nombreCoupsLabel)
        hLayoutCoups.addWidget(self.nombreCoups)
        hLayoutCoups.addStretch(1)

        vMainLayout.addLayout(hlayoutBras)
        vMainLayout.addLayout(hLayoutCoups)


        self.nombreBras.setText("10")
        self.nombreCoups.setText("50")
        self.permutationLineEdit.setText("5")
        self.intervalleLineEdit.setText("4")
        self.algoJoueur.setChecked(True)
        self.algoHasard.setChecked(True)
        self.algoGlouton.setChecked(True)
        self.algoEpsilonGlouton.setChecked(True)
        self.algoMoyenneGain.setChecked(True)
        self.algoUCB.setChecked(True)

        # Events
        self.cancel.clicked.connect(self.close)
        self.validate.clicked.connect(lambda: self.validateConfiguration(listAlgorithme))
        self.cancel.setFocusPolicy(QtCore.Qt.NoFocus)
        self.radioButtonClassique.clicked.connect(self.checkValidityLineEdit)
        self.radioButtonDynamique.clicked.connect(self.checkValidityLineEdit)
        self.radioButtonDiminution.clicked.connect(self.checkValidityLineEdit)
        self.nombreBras.textEdited.connect(self.checkValidityLineEdit)
        self.nombreCoups.textEdited.connect(self.checkValidityLineEdit)

        self.setLayout(vMainLayout)

        self.setFixedSize(self.sizeHint())


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

        self.close()

    def configurationBras(self):

        nombreBras = int(self.nombreBras.displayText())
        gLayout = QtGui.QGridLayout()

        for i in range(0, nombreBras):
            hlayout = QtGui.QHBoxLayout()
            stringLabel = "Bras n°" + str(i + 1) + "  "
            labelBras = QtGui.QLabel(stringLabel)
            probaLabel = QtGui.QLabel("Probabilité ")
            gainLabel = QtGui.QLabel("Gain ")
            proba = QtGui.QLineEdit()
            gain = QtGui.QLineEdit()
            random = QtGui.QPushButton("Random")
            hlayout.addWidget(labelBras)
            hlayout.addWidget(probaLabel)
            hlayout.addWidget(proba)
            hlayout.addWidget(gainLabel)
            hlayout.addWidget(gain)
            hlayout.addWidget(random)
            if i % 2 == 0:
                hlayout.addSpacing(50)
            gLayout.addLayout(hlayout, i / 2, i % 2)

        return gLayout


    def showScenarioCreatorFrame(self):
        self.show()

