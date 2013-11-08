from PyQt4 import QtGui, QtCore
import sys
import gameZone

class MainWindow(QtGui.QMainWindow):
    """Classe qui représente la fenêtre principale"""

    def __init__(self):
        """Initialistion de la fenêtre principale"""
        super(MainWindow, self).__init__()

        self.initCentralWidget()
        self.initMenuBar()
        self.initStatusBar()
        self.show()
        

    def initCentralWidget(self):
        """Méthode d'initialisation"""
        
        centralWidget = gameZone.GameZone(10, 50, [0,1,3,4])
        
        # Recuperation du centre de l'écran de l'utilisateur
        screenCenter = QtGui.QDesktopWidget().availableGeometry().center()
        
        centralWidgetPosition = centralWidget.frameGeometry()
        # centre la centralWidget par rapport à l'écran
        centralWidgetPosition.moveCenter(screenCenter)
     
        self.move(centralWidgetPosition.topLeft())

        self.setCentralWidget(centralWidget)

    def initMenuBar(self):
        """Initialisation de la menu bar"""
        
        menuBar = self.menuBar()
        
        # File menu
        fileMenu = menuBar.addMenu("Fichier")

        exitAction = QtGui.QAction("Quitter", self)
        exitAction.setShortcut("Ctrl+Q")
        exitAction.setStatusTip("Quitter l'application")
        exitAction.triggered.connect(QtGui.qApp.quit)
        fileMenu.addAction(exitAction)
    
        # Configuration menu
        editMenu = menuBar.addMenu("Configuration")

        nombreBras = QtGui.QAction("Nombre de bras", editMenu)
        nombreBras.triggered.connect(self.showDialogArmNumber)
        editMenu.addAction(nombreBras)

        nombreCoups = QtGui.QAction("Nombre de coups", editMenu)
        nombreCoups.triggered.connect(self.showDialogPlayingNumber)
        editMenu.addAction(nombreCoups)

        # Algorithme
        algorithme = editMenu.addMenu("Algorithme")

        hasard = QtGui.QAction("Hasard", algorithme, checkable = True)
        hasard.setChecked(True)
        glouton = QtGui.QAction("Glouton", algorithme, checkable = True)
        glouton.setChecked(True)
        algorithme.addAction(hasard)
        algorithme.addAction(glouton)

        # Events triggered
        #hasard.changed.connect()
        #glouton.changed.connect()


        
    def initStatusBar(self):
        """Initialisation de la status bar"""

        self.statusBar()


    def showDialogArmNumber(self):
        """Boite de dialogue demandant le nombre de bras"""
        text, value = QtGui.QInputDialog.getText(self, 'Nombre de bras', "Choisissez un nombre de bras :")
        
        try :
            text = int(text)
        except ValueError :
            pass

        if value & isinstance(text, int):
            sender = self.sender()
            #sender.triggered.connect(gameZone.GameZone.hey)

    def showDialogPlayingNumber(self):
        """Boite de dialogue demandant le nombre de coups"""
        text, value = QtGui.QInputDialog.getText(self, 'Nombre de bras', "Choisissez un nombre de bras :")
        
        try :
            text = int(text)
        except ValueError :
            pass

        if value & isinstance(text, int):
            sender = self.sender()
            #sender.triggered.connect(gameZone.GameZone.hey)

app = QtGui.QApplication(sys.argv)
main = MainWindow()

sys.exit(app.exec_())
