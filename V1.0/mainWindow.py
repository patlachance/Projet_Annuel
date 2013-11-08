from PyQt4 import QtGui, QtCore
import sys
import gameZone

class MainWindow(QtGui.QMainWindow):
    """Classe qui représente la fenêtre principale"""

    def __init__(self) :
        """Initialistion de la fenêtre principale"""
        
        super(MainWindow, self).__init__()
        
        self.centralWidget = None
        self.initCentralWidget(10, 50, [0, 1, 2, 3, 4])
        self.initMenuBar()
        self.initStatusBar()
        self.show()
        

    def initCentralWidget(self, bras, nombreCoups, listAlgo):
        """Méthode d'initialisation"""
        
        self.centralWidget = gameZone.GameZone(bras, nombreCoups, listAlgo)

        centralWidget = gameZone.GameZone(10, 50, [0,1,2,3,4])
        
        # Recuperation du centre de l'écran de l'utilisateur
        screenCenter = QtGui.QDesktopWidget().availableGeometry().center()
        
        centralWidgetPosition = self.centralWidget.frameGeometry()
        # centre la centralWidget par rapport à l'écran
        centralWidgetPosition.moveCenter(screenCenter)
     
        self.move(centralWidgetPosition.topLeft())

        self.setCentralWidget(self.centralWidget)

    def initMenuBar(self):
        """Initialisation de la menu bar"""
        
        menuBar = self.menuBar()
        
        self.fileMenu(menuBar)
        self.editionMenu(menuBar)
        

        # Events triggered
        #hasard.changed.connect()
        #glouton.changed.connect()


        
    def initStatusBar(self):
        """Initialisation de la status bar"""

        self.statusBar()


    def fileMenu(self, menuBar):
        """Création de l'onglet Fichier de la menu bar"""
        
        fileMenu = menuBar.addMenu("Fichier")

        exitAction = QtGui.QAction("Quitter", fileMenu)
        exitAction.setShortcut("Ctrl+Q")
        exitAction.setStatusTip("Quitter l'application")
        exitAction.triggered.connect(QtGui.qApp.quit)
        fileMenu.addAction(exitAction)
        
        
    def editionMenu(self, menuBar):
        """Création de l'onglet Edition de la menu bar"""
        
        editMenu = menuBar.addMenu("Edition")
        configurationAction = QtGui.QAction("Configuration", editMenu)
        configurationAction.triggered.connect(self.showDialogConfiguration)
        editMenu.addAction(configurationAction)
        

        
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
        validate = QtGui.QPushButton("Valider")
        cancel = QtGui.QPushButton("Annuler")

        algoJoueur.setChecked(True)
        algoHasard.setChecked(True)
        algoGlouton.setChecked(True)
        algoEpsilonGlouton.setChecked(True)

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
        gridLayout.addWidget(cancel, 5, 0)
        gridLayout.addWidget(validate, 5, 1)

        nombreBras.setText(str(self.centralWidget.bras))
        nombreCoups.setText(str(self.centralWidget.nbCoups))

        
        
        # Events
        nombreCoups.textEdited.connect(lambda : print("yoooooo"))
        cancel.clicked.connect(configurationFrame.close)
        #validate.clicked.connect(lambda : self.validateConfiguration(nombreBras, nombreCoups, configurationFrame))
        configurationFrame.setLayout(gridLayout)
        configurationFrame.setFixedSize(configurationFrame.sizeHint())
        configurationFrame.show()

        
        
    def validateConfiguration(self, nombreBras, nombreCoups, configurationFrame) :
        """Valide la configuration envoyée"""
        
        nbBras, nbCoups = self.centralWidget.bras, self.centralWidget.nbCoups
        validNbBras, validNbCoups = True, True
         
        
        if nombreBras.displayText() != str(nbBras) :
            try :
                nbBras = int(nombreBras.displayText())
            except ValueError :
                validNbBras = False
                nombreBras.setText(str(self.centralWidget.bras))
    
        if nombreBras.displayText() != str(nbCoups) :
            try :
                nbCoups = int(nombreCoups.displayText())
            except ValueError :
                validNbBras = False
                nombreCoups.setText(str(self.centralWidget.nbCoups))
         
        if validNbBras & validNbCoups :
            self.initCentralWidget(nbBras, nbCoups)
            configurationFrame.close()
        else :
            configurationFrame.close()


app = QtGui.QApplication(sys.argv)
main = MainWindow()

sys.exit(app.exec_())
