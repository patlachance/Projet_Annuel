from PyQt4 import QtGui, QtCore
import sys
import gameZone
import scenario

class MainWindow(QtGui.QMainWindow):
    """Classe qui représente la fenêtre principale"""

    def __init__(self):
        """Initialistion de la fenêtre principale"""

        super(MainWindow, self).__init__()

        self.centralWidget = None
        self.initUI()
        self.initMenuBar()
        self.initStatusBar()
        self.setWindowTitle('Jeu du manchot')
        self.show()

    def initUI(self):

        self.initCentralWidget(10, 10, [0, 1, 2, 3, 4, 5])

        # Recuperation du centre de l'écran de l'utilisateur
        screenCenter = QtGui.QDesktopWidget().availableGeometry().center()

        centralWidgetPosition = self.centralWidget.frameGeometry()
        # centre la centralWidget par rapport à l'écran
        centralWidgetPosition.moveCenter(screenCenter)

        self.move(centralWidgetPosition.topLeft())

    def initCentralWidget(self, *args):
        """Méthode d'initialisation"""

        #args[0] = nbBras
        #args[1] = nbCoups
        #args[2] = listAlgorithme
        #args[3] = listBras

        if len(args) == 4:
            self.centralWidget = gameZone.GameZone(args[0], args[1], args[2], args[3])
        else:
            self.centralWidget = gameZone.GameZone(args[0], args[1], args[2])
        self.setCentralWidget(self.centralWidget)
        self.setMinimumSize(self.centralWidget.size())
        self.resize(self.centralWidget.size().width(), self.centralWidget.size().height()+50)
        self.setStyleSheet("background-color: #3c3b37;")
        self.connect(self.centralWidget,QtCore.SIGNAL("resize(int)"),self.Resize)

    def Resize(self, size):
        self.resize(self.centralWidget.size().width(), self.centralWidget.size().height() + size +100)

    def initMenuBar(self):
        """Initialisation de la menu bar"""

        menuBar = self.menuBar()

        self.fileMenu(menuBar)
        self.editionMenu(menuBar)


    def initStatusBar(self):
        """Initialisation de la status bar"""

        self.statusBar()


    def fileMenu(self, menuBar):
        """Création de l'onglet Fichier de la menu bar"""

        fileMenu = menuBar.addMenu("Fichier")

        newGame = QtGui.QAction("Nouvelle partie", fileMenu)
        newGame.setShortcut("N")
        newGame.triggered.connect(self.showNewGame)

        loadScenario = QtGui.QAction("Charger un scénario", fileMenu)
        loadScenario.triggered.connect(self.showLoadScenarioDialog)

        exitAction = QtGui.QAction("Quitter", fileMenu)
        exitAction.setShortcut("Ctrl+Q")
        exitAction.setStatusTip("Quitter l'application")
        exitAction.triggered.connect(QtGui.qApp.quit)

        fileMenu.addAction(newGame)
        fileMenu.addAction(loadScenario)
        fileMenu.addAction(exitAction)

    def editionMenu(self, menuBar):
        """Création de l'onglet Edition de la menu bar"""

        editMenu = menuBar.addMenu("Edition")
        configurationAction = QtGui.QAction("Configuration", editMenu)
        configurationAction.triggered.connect(self.showDialogConfiguration)
        editMenu.addAction(configurationAction)

    def showNewGame(self):
        """Création d'une nouvelle partie"""
        listAlgoNumber = []

        for algo in self.centralWidget.moteurJeu.listAlgorithme:
                listAlgoNumber.append(algo.numAlgo)
                
        self.initCentralWidget(self.centralWidget.moteurJeu.nbBras, self.centralWidget.moteurJeu.nbCoupsMax, listAlgoNumber)

    def showLoadScenarioDialog(self):
        """Affiche la fenetre de chargement d'un scenario"""

        pathFilePicked = QtGui.QFileDialog.getOpenFileName(filter="*.sc")
        scenar = scenario.Scenario(pathFilePicked)
        configurationScenario = scenar.loadScenario()
        self.initCentralWidget(scenar.configuration[0], scenar.configuration[1], scenar.configuration[2], scenar.listes_bras)

    def showDialogConfiguration(self):
        """Boite de dialogue demandant le nombre de coups"""

        configurationFrame = QtGui.QDialog(self)
        configurationFrame.setWindowTitle("Fenêtre de configuration")
        gridLayout = QtGui.QGridLayout()
        gridLayout.setSpacing(10)

        font = QtGui.QFont("Times", 14, QtGui.QFont.Bold, True)
        font.setUnderline(True)

        nombreBrasLabel = QtGui.QLabel("Nombre de bras : ")
        nombreCoupsLabel = QtGui.QLabel("Nombre de coups : ")
        nombreBras = QtGui.QLineEdit()
        nombreCoups = QtGui.QLineEdit()
        algorithmeLabel = QtGui.QLabel("Algorithmes")
        algoJoueur = QtGui.QCheckBox("Joueur")
        algoHasard = QtGui.QCheckBox("Hasard")
        algoGlouton = QtGui.QCheckBox("Glouton")
        algoEpsilonGlouton = QtGui.QCheckBox("Epsilon glouton")
        algoMoyenneGain = QtGui.QCheckBox("Moyenne gain")

        algoUCB = QtGui.QCheckBox("UCB1")

        #optStat = 

        validate = QtGui.QPushButton("Valider")
        cancel = QtGui.QPushButton("Annuler")

        listAlgorithme = [algoJoueur, algoHasard, algoGlouton, algoEpsilonGlouton, algoMoyenneGain, algoUCB]

        
        ############################
        #       TEMPORAIRE         #
        ############################

        self.setCheckedAlgoBox(listAlgorithme, self.centralWidget.listAlgo)

        algorithmeLabel.setFont(font)

        gridLayout.addWidget(nombreBrasLabel, 0, 0)
        gridLayout.addWidget(nombreBras, 0, 1)
        gridLayout.addWidget(nombreCoupsLabel, 1, 0)
        gridLayout.addWidget(nombreCoups, 1, 1)
        gridLayout.addWidget(algorithmeLabel, 2, 0, 1, 0, QtCore.Qt.AlignCenter)
        gridLayout.addWidget(algoJoueur, 3, 0)
        gridLayout.addWidget(algoHasard, 3, 1)
        gridLayout.addWidget(algoGlouton, 4, 0)
        gridLayout.addWidget(algoEpsilonGlouton, 4, 1)
        gridLayout.addWidget(algoMoyenneGain, 5, 0)
        gridLayout.addWidget(algoUCB, 5, 1)
        gridLayout.addWidget(cancel, 6, 0)
        gridLayout.addWidget(validate, 6, 1)

        nombreBras.setText(str(self.centralWidget.moteurJeu.nbBras))
        nombreCoups.setText(str(self.centralWidget.moteurJeu.nbCoupsMax))

        # Events
        cancel.clicked.connect(configurationFrame.close)
        validate.clicked.connect(lambda: self.validateConfiguration(nombreBras, nombreCoups, listAlgorithme , configurationFrame))
        cancel.setFocusPolicy(QtCore.Qt.NoFocus)
        nombreBras.textEdited.connect(nombreBras.setText)
        nombreBras.textEdited.connect(lambda: self.checkValidityLineEdit(nombreBras, nombreCoups, validate))
        nombreCoups.textEdited.connect(nombreCoups.setText)
        nombreCoups.textEdited.connect(lambda: self.checkValidityLineEdit(nombreBras, nombreCoups, validate))
        
        configurationFrame.setLayout(gridLayout)
        configurationFrame.setFixedSize(configurationFrame.sizeHint())
        configurationFrame.show()


    def validateConfiguration(self, nombreBras, nombreCoups, listAlgorithme, configurationFrame):
        """Valide la configuration envoyée"""

        listAlgoNumber = []

        for algo, i in zip(listAlgorithme, range(0, 5)):
            if algo.isChecked():
                listAlgoNumber.append(i)

        self.initCentralWidget(int(nombreBras.displayText()), int(nombreCoups.displayText()), listAlgoNumber)
        configurationFrame.close()

    def checkValidityLineEdit(self, nombreBrasLineEdit, nombreCoupsLineEdit, validButton):
        """Verifie la validité de la valeur entrée pour une LineEdit et modifie en conséquent la cliquabilité du bouton valid"""

        numberArm = 0
        numberBlow = 0
        validity = True

        try:
            numberArm = int(nombreBrasLineEdit.displayText())
            numberBlow = int(nombreCoupsLineEdit.displayText())
        except ValueError:
            validity = False
        finally:
            if numberArm < 1 or numberBlow < 1:
                validity = False

            self.emit(QtCore.SIGNAL(validButton.setDisabled(not validity)))



    def setCheckedAlgoBox(self, listAlgorithme, listAlgoNumber):
        """Coche les checkbox selon la présence ou non des algorithmes"""

        for i in listAlgoNumber:
            listAlgorithme[i].setChecked(True)


    def validateConfiguration(self, nombreBras, nombreCoups, listAlgorithme, configurationFrame) :
        """Valide la configuration envoyée"""
        
        listAlgoNumber = []

        #Penser à modifier la range en fonction du nombre d'algo
        for algo, i in zip(listAlgorithme, range(0, 6)):
            if algo.isChecked():
                listAlgoNumber.append(i)
                
        self.initCentralWidget(int(nombreBras.displayText()), int(nombreCoups.displayText()), listAlgoNumber)
        configurationFrame.close()
        if listAlgoNumber[0]!=0:
            self.centralWidget.auto()
        
    def checkValidityLineEdit(self, nombreBrasLineEdit, nombreCoupsLineEdit, validButton):
        """Verifie la validité de la valeur entrée pour une LineEdit et modifie en conséquent la cliquabilité du bouton valid"""
    
        numberArm = 0
        numberBlow = 0
        validity = True
        
        try:
            numberArm = int(nombreBrasLineEdit.displayText())
            numberBlow = int(nombreCoupsLineEdit.displayText())
        except ValueError:
            validity = False
        finally:
            if numberArm < 1 or numberBlow < 1:
                validity = False
                      
            self.emit(QtCore.SIGNAL(validButton.setDisabled(not validity)))
    
                    
    def setCheckedAlgoBox(self, listAlgorithme, listAlgoNumber):
        """Coche les checkbox selon la présence ou non des algorithmes"""
        
        for i in listAlgoNumber:
            listAlgorithme[i].setChecked(True)
            
           
app = QtGui.QApplication(sys.argv)
main = MainWindow()

sys.exit(app.exec_())
