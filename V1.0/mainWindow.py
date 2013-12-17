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
        self.showMaximized()
        

    def initCentralWidget(self, bras, nombreCoups, listAlgo):
        """Méthode d'initialisation"""
        
        self.centralWidget = gameZone.GameZone(bras, nombreCoups, listAlgo)

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
        algoMoyenneGain = QtGui.QCheckBox("Moyenne gain")
        validate = QtGui.QPushButton("Valider")
        cancel = QtGui.QPushButton("Annuler")

        listAlgorithme = [algoJoueur, algoHasard, algoGlouton, algoEpsilonGlouton, algoMoyenneGain]
        
        ############################
        #       TEMPORAIRE         #
        ############################
        algoJoueur.setDisabled(True)
        
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
        gridLayout.addWidget(cancel, 6, 0)
        gridLayout.addWidget(validate, 6, 1)

        nombreBras.setText(str(self.centralWidget.bras))
        nombreCoups.setText(str(self.centralWidget.nbCoups))

        # Events
        cancel.clicked.connect(configurationFrame.close)
        validate.clicked.connect(lambda : self.validateConfiguration(nombreBras, nombreCoups, listAlgorithme , configurationFrame))
        cancel.setFocusPolicy(QtCore.Qt.NoFocus)
        nombreBras.textEdited.connect(nombreBras.setText)
        nombreBras.textEdited.connect(lambda : self.checkValidityLineEdit(nombreBras, nombreCoups, validate))
        nombreCoups.textEdited.connect(nombreCoups.setText)
        nombreCoups.textEdited.connect(lambda : self.checkValidityLineEdit(nombreBras, nombreCoups, validate))
        
        configurationFrame.setLayout(gridLayout)
        configurationFrame.setFixedSize(configurationFrame.sizeHint())
        configurationFrame.show()

        
        
    def validateConfiguration(self, nombreBras, nombreCoups, listAlgorithme, configurationFrame) :
        """Valide la configuration envoyée"""
        
        listAlgoNumber = []
        
        for algo, i in zip(listAlgorithme, range(0, 5)):
            if algo.isChecked() :
                listAlgoNumber.append(i)
                
        self.initCentralWidget(int(nombreBras.displayText()), int(nombreCoups.displayText()), listAlgoNumber)
        configurationFrame.close()
        
    def checkValidityLineEdit(self, nombreBrasLineEdit, nombreCoupsLineEdit, validButton):
        """Verifie la validité de la valeur entrée pour une LineEdit et modifie en conséquent la cliquabilité du bouton valid"""
    
        numberArm = 0
        numberBlow = 0
        validity = True
        
        try :
            numberArm = int(nombreBrasLineEdit.displayText())
            numberBlow = int(nombreCoupsLineEdit.displayText())
        except ValueError :
            validity = False
        finally :
            if numberArm < 1 or numberBlow < 1 :
                validity = False
                      
            self.emit(QtCore.SIGNAL(validButton.setDisabled(not validity)))
    
                    
    def setCheckedAlgoBox(self, listAlgorithme, listAlgoNumber):
        """Coche les checkbox selon la présence ou non des algorithmes"""
        
        for i in  listAlgoNumber:
            listAlgorithme[i].setChecked(True)
            
            
app = QtGui.QApplication(sys.argv)
main = MainWindow()

sys.exit(app.exec_())
