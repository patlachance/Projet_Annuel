from PyQt4 import QtGui, QtCore
import sys
import gameZone

class MainWindow(QtGui.QMainWindow):
    """Classe qui représente la fenêtre principale"""

    def __init__(self) :
        """Initialistion de la fenêtre principale"""
        
        super(MainWindow, self).__init__()
        
        self.centralWidget = gameZone.GameZone(10, 50)
        self.initCentralWidget()
        self.initMenuBar()
        self.initStatusBar()
        self.show()
        

    def initCentralWidget(self):
        """Méthode d'initialisation"""
        
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
        exitAction.triggered.connect(showDialogConfiguration)
        editMenu.addAction(configurationAction)
        

        
    def showDialogConfiguration(self):
        """Boite de dialogue demandant le nombre de coups"""
        
        gridLayout = QtGui.QGridLayout(self)
      
        nombreBras = QtGui.QInputDialog()
        text, value = nombreBras.getText(self, 'Nombre de bras', "Choisissez un nombre de bras :")
        
        try :
            text = int(text)
        except ValueError :
            pass

        if value & isinstance(text, int):
            sender = self.sender()
            #sender.triggered.connect(gameZone.GameZone.hey)
            
        gridLayout.addWidget(nombreBras)

app = QtGui.QApplication(sys.argv)
main = MainWindow()

sys.exit(app.exec_())
