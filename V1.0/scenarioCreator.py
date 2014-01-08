from PyQt4 import QtGui, QtCore
import moteur
import configurationFrame
import guiBras

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

        self.scrollArea = QtGui.QScrollArea()
        self.vMainLayout = QtGui.QVBoxLayout()
        self.gridLayoutConfigBras = QtGui.QGridLayout()
        self.validate = QtGui.QPushButton("Valider")
        self.cancel = QtGui.QPushButton("Annuler")

        self.showDialogConfiguration()

    def showDialogConfiguration(self):

        self.setWindowTitle("Fenêtre de configuration")


        gridLayout1 = QtGui.QGridLayout()
        gridLayout2 = QtGui.QGridLayout()
        gridLayoutAlgo = QtGui.QGridLayout()
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

        listAlgorithme = [self.algoJoueur, self.algoHasard, self.algoGlouton, self.algoEpsilonGlouton, self.algoMoyenneGain, self.algoUCB]


        self.algorithmeLabel.setFont(font)
        self.configurationLabel.setFont(font)

        gridLayout1.addWidget(self.nombreBrasLabel, 0, 0)
        gridLayout1.addWidget(self.nombreBras, 0, 1)
        gridLayout1.addWidget(self.nombreCoupsLabel, 1, 0)
        gridLayout1.addWidget(self.nombreCoups, 1, 1)
        gridLayout1.setColumnStretch(2, 1)

        gridLayout2.addWidget(self.configurationLabel, 2, 0, 1, 3, QtCore.Qt.AlignCenter)
        gridLayout2.addWidget(self.radioButtonClassique, 3, 0)
        gridLayout2.addWidget(self.radioButtonDynamique, 3, 1)
        gridLayout2.addWidget(self.radioButtonDiminution, 3, 2)

        hlayoutConfiguration.addWidget(self.nombrePermutationLabel)
        hlayoutConfiguration.addWidget(self.permutationLineEdit)
        hlayoutConfiguration.addWidget(self.nombreIntervalleLabel)
        hlayoutConfiguration.addWidget(self.intervalleLineEdit)

        gridLayoutAlgo.addWidget(self.algorithmeLabel, 0, 0, 1, 2, QtCore.Qt.AlignCenter)
        gridLayoutAlgo.addWidget(self.algoJoueur, 1, 0)
        gridLayoutAlgo.addWidget(self.algoHasard, 1, 1)
        gridLayoutAlgo.addWidget(self.algoGlouton, 2, 0)
        gridLayoutAlgo.addWidget(self.algoEpsilonGlouton, 2, 1,)
        gridLayoutAlgo.addWidget(self.algoMoyenneGain, 3, 0)
        gridLayoutAlgo.addWidget(self.algoUCB, 3, 1)

        hlayoutWindowButton.addWidget(self.cancel)
        hlayoutWindowButton.addWidget(self.validate)

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

        self.nombreBras.setFixedWidth(100)
        self.nombreCoups.setFixedWidth(100)
        self.permutationLineEdit.setFixedWidth(75)
        self.intervalleLineEdit.setFixedWidth(75)
        self.cancel.setFixedWidth(75)
        self.validate.setFixedWidth(75)

        self.vMainLayout.addLayout(gridLayout1)
        self.vMainLayout.addLayout(gridLayout2)
        self.vMainLayout.addLayout(hlayoutConfiguration)
        self.vMainLayout.addLayout(gridLayoutAlgo)
        self.createWidgetConfigurationBras()
        self.vMainLayout.addLayout(hlayoutWindowButton)

        # Events
        self.cancel.clicked.connect(self.close)
        self.validate.clicked.connect(lambda: self.validateConfiguration(listAlgorithme))
        self.cancel.setFocusPolicy(QtCore.Qt.NoFocus)
        self.radioButtonClassique.clicked.connect(self.checkValidityLineEdit)
        self.radioButtonDynamique.clicked.connect(self.checkValidityLineEdit)
        self.radioButtonDiminution.clicked.connect(self.checkValidityLineEdit)
        self.nombreBras.textEdited.connect(self.checkValidityLineEdit)
        self.nombreCoups.textEdited.connect(self.checkValidityLineEdit)

        self.setLayout(self.vMainLayout)
        self.setGeometry(100, 100, 1100, 600)
        #self.setFixedSize(self.sizeHint())


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

        if type(numberArm) is int and numberArm > 0:
            self.createWidgetConfigurationBras()

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

        for i in range(0, nombreBras):
            b = guiBras.GuiBras(self.validate)
            b.setLabelBras(i)

            self.gridLayoutConfigBras.addWidget(b, int(i / 2), int(i % 2))


    def createWidgetConfigurationBras(self):

        self.vMainLayout.removeWidget(self.scrollArea)
        self.scrollArea = None
        self.scrollArea = QtGui.QScrollArea()
        configurationBrasWidget = QtGui.QWidget()
        self.configurationBras()
        configurationBrasWidget.setLayout(self.gridLayoutConfigBras)
        self.scrollArea.setWidget(configurationBrasWidget)
        self.vMainLayout.insertWidget(4, self.scrollArea)

    def showScenarioCreatorFrame(self):
        self.show()

