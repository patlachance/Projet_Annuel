from PyQt4 import QtGui, QtCore
import sys
import gameZone
import moteur
import scenarioLoader
import scenarioCreator

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

        self.initCentralWidget(moteur.Moteur(10, 50, [0, 1, 2, 3, 4, 5], 0))

        # Recuperation du centre de l'écran de l'utilisateur
        screenCenter = QtGui.QDesktopWidget().availableGeometry().center()

        centralWidgetPosition = self.centralWidget.frameGeometry()

        # centre la centralWidget par rapport à l'écran
        centralWidgetPosition.moveCenter(screenCenter)

        self.move(centralWidgetPosition.topLeft())


    def initCentralWidget(self, moteurJeu):
        """Méthode d'initialisation"""

        self.centralWidget = gameZone.GameZone(moteurJeu)

        self.setCentralWidget(self.centralWidget)
        self.setMinimumSize(self.centralWidget.size())
        self.resize(self.centralWidget.size().width(), self.centralWidget.size().height()+100)
        self.connect(self.centralWidget, QtCore.SIGNAL("resize(int)"), self.Resize)


    def Resize(self, size):
        self.resize(self.centralWidget.size().width(), self.centralWidget.size().height() + size + 100)

    def initMenuBar(self):
        """Initialisation de la menu bar"""

        menuBar = self.menuBar()

        self.fileMenu(menuBar)
        self.editionMenu(menuBar)
        self.scenarioMenu(menuBar)

    def initStatusBar(self):
        """Initialisation de la status bar"""

        self.statusBar()


    def fileMenu(self, menuBar):
        """Création de l'onglet Fichier de la menu bar"""

        fileMenu = menuBar.addMenu("Fichier")

        newGame = QtGui.QAction("Nouvelle partie", fileMenu)
        newGame.setShortcut("N")
        newGame.triggered.connect(self.showNewGame)

        exitAction = QtGui.QAction("Quitter", fileMenu)
        exitAction.setShortcut("Ctrl+Q")
        exitAction.setStatusTip("Quitter l'application")
        exitAction.triggered.connect(QtGui.qApp.quit)

        fileMenu.addAction(newGame)
        fileMenu.addAction(exitAction)

    def editionMenu(self, menuBar):
        """Création de l'onglet Edition de la menu bar"""

        editMenu = menuBar.addMenu("Edition")
        configurationAction = QtGui.QAction("Configuration", editMenu)

        configurationAction.triggered.connect(self.showScenarioCreator)

        editMenu.addAction(configurationAction)


    def scenarioMenu(self, menuBar):
        """Création de l'onglet ScenarioLoader de la menu bar"""

        scenarioMenu = menuBar.addMenu("Scénario")

        chargerAction = QtGui.QAction("Charger", scenarioMenu)

        chargerAction.triggered.connect(self.showLoadScenarioDialog)

        scenarioMenu.addAction(chargerAction)

    def showNewGame(self):
        """Création d'une nouvelle partie"""
        listAlgoNumber = []

        for algo in self.centralWidget.moteurJeu.listAlgorithme:
                listAlgoNumber.append(algo.numAlgo)
                
        self.initCentralWidget(moteur.Moteur(self.centralWidget.moteurJeu.nbBras, self.centralWidget.moteurJeu.nbCoupsMax, listAlgoNumber, self.centralWidget.moteurJeu.option))

        if listAlgoNumber[0] != 0:
            self.centralWidget.auto()

    def showScenarioCreator(self):

        scenarCreator = scenarioCreator.ScenarioCreator(self, centralWidget=self.centralWidget)
        scenarCreator.showScenarioCreatorFrame()

    def showLoadScenarioDialog(self):
        """Affiche la fenetre de chargement d'un scenario"""

        pathFilePicked = QtGui.QFileDialog.getOpenFileName(filter="*.sc")
        if pathFilePicked != '':
            scenar = scenarioLoader.ScenarioLoader(pathFilePicked)
            moteurJeu = scenar.initialiseConfiguration(scenar.loadScenario())
            self.initCentralWidget(moteurJeu)

    
app = QtGui.QApplication(sys.argv)
main = MainWindow()

sys.exit(app.exec_())
