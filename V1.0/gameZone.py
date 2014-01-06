from PyQt4 import QtGui, QtCore
import moteur

class GameZone(QtGui.QWidget):
    
    def __init__(self, *args):

        super(GameZone, self).__init__()

        #args[0] = nbBras
        #args[1] = nbCoups
        #args[2] = listAlgorithme
        #args[3] = listBras

        self.listAlgo = args[2]

        if len(args) == 4:
            self.moteurJeu = moteur.Moteur(args[0], args[1], args[2], args[3])
        else:
            self.moteurJeu = moteur.Moteur(args[0], args[1], args[2])

        self.initUI()
       

    def initUI(self):

        ###############
        #Partie Joueur#
        ###############

        cadreGain = QtGui.QGridLayout()
        cadreGain.setRowStretch(0, 1)
        cadreGain.setRowStretch(4, 1)

        font = QtGui.QFont()
        font.setBold(True)

        labelGain = QtGui.QLabel("Gain")
        labelGain.setFont(font)
        cadreGain.addWidget(labelGain, 1, 0)

        self.resultatGain = QtGui.QLabel(format(0, '.2f'))
        self.resultatGain.setFont(font)

        cadreGain.addWidget(self.resultatGain, 1, 1)

        self.labelGainEspere = QtGui.QLabel("Gain espéré")
        cadreGain.addWidget(self.labelGainEspere, 2, 0)
        self.labelGainEspere.setVisible(False)

        self.resultatGainEspere = QtGui.QLabel(format(float(self.moteurJeu.gainEspere()), '.2f'))
        cadreGain.addWidget(self.resultatGainEspere, 2, 1)
        self.resultatGainEspere.setVisible(False)
        
        labelNbCoupsJoue = QtGui.QLabel("Nombre de coups")
        cadreGain.addWidget(labelNbCoupsJoue, 3, 0)

        self.resultatNbCoupsJoue = QtGui.QLabel("0")
        cadreGain.addWidget(self.resultatNbCoupsJoue, 3, 1)



        cadreJoueur = QtGui.QGridLayout()
        icon = QtGui.QIcon("bras.gif")
        
        cadreJoueur.setRowStretch(0, 1)
        cadreJoueur.setColumnStretch(6, 1)

        self.listBout = []

        for i in range(0, self.moteurJeu.nbBras):
            self.listBout.append(QtGui.QPushButton(str(i+1)))
            self.listBout[i].setIcon(icon)
            self.listBout[i].setIconSize(QtCore.QSize(50, 50))
            self.listBout[i].clicked.connect(self.buttonClicked)
            cadreJoueur.addWidget(self.listBout[i], 1, i)
               
        labelGainMoyenBras = QtGui.QLabel("Gain moyen par bras : ")
        labelGainMoyenBras.setStyleSheet("border: 0px;")
        cadreJoueur.addWidget(labelGainMoyenBras, 2, 0, 1, self.moteurJeu.nbBras)

        labelNombreCoupsBras = QtGui.QLabel("Nombre de coups par bras ")
        labelNombreCoupsBras.setStyleSheet("border: 0px;")
        cadreJoueur.addWidget(labelNombreCoupsBras, 5, 0, 1, self.moteurJeu.nbBras)

        cadreJoueur.setRowStretch(0,1)
        cadreJoueur.setColumnStretch(6,1)

        self.listBout = []

        for i in range(0, self.moteurJeu.nbBras):
            self.listBout.append(QtGui.QPushButton(str(i+1)))
            self.listBout[i].setIcon(icon)
            self.listBout[i].setIconSize(QtCore.QSize(50,50))
            self.listBout[i].clicked.connect(self.buttonClicked)
            cadreJoueur.addWidget(self.listBout[i], 1, i)
               
        labelGainMoyenBras = QtGui.QLabel("Gain moyen par bras : ")
        labelGainMoyenBras.setStyleSheet("border: 0px;")
        cadreJoueur.addWidget(labelGainMoyenBras, 2, 0, 1, self.moteurJeu.nbBras)

        labelNombreCoupsBras = QtGui.QLabel("Nombre de coups par bras ")
        labelNombreCoupsBras.setStyleSheet("border: 0px;")
        cadreJoueur.addWidget(labelNombreCoupsBras, 5, 0, 1, self.moteurJeu.nbBras)
        
        self.moyenneBras = []
        self.nombreFoisJoueBras = []

        for i in range(0, self.moteurJeu.nbBras):
            self.moyenneBras.append(QtGui.QLabel(format(0, '.2f')))
            self.moyenneBras[i].setAlignment(QtCore.Qt.AlignCenter)

            cadreJoueur.addWidget(self.moyenneBras[i], 3, i)
            
            self.nombreFoisJoueBras.append(QtGui.QLabel("0"))
            self.nombreFoisJoueBras[i].setAlignment(QtCore.Qt.AlignCenter)
            cadreJoueur.addWidget(self.nombreFoisJoueBras[i], 4, i)

        joueur = QtGui.QHBoxLayout()
        joueur.addLayout(cadreGain)
        joueur.addStretch(1)
        joueur.addLayout(cadreJoueur)
        joueur.addStretch(1)
        
        groupJoueur = QtGui.QGroupBox("Partie Joueur")
        groupJoueur.setLayout(joueur)
        

        #############
        #Partie Algo#
        #############


        cadreGainAlgo = QtGui.QGridLayout()
        cadreGainAlgo.setColumnStretch(3,1)

        self.listResAlgo = []
        
        for i in range(1, len(self.listAlgo)):

            if self.listAlgo[i] == 1:
                labelAlgo = QtGui.QLabel("Gain Algo hasard")
                cadreGainAlgo.addWidget(labelAlgo, i-1, 0)
            if self.listAlgo[i] == 2:
                labelAlgo = QtGui.QLabel("Gain Algo Glouton")
                cadreGainAlgo.addWidget(labelAlgo, i-1, 0)
            if self.listAlgo[i] == 3:
                labelAlgo = QtGui.QLabel("Gain Algo Espilon")
                cadreGainAlgo.addWidget(labelAlgo, i-1, 0)
            if self.listAlgo[i] == 4:
                labelAlgo = QtGui.QLabel("Gain Algo Moyenne Gain")
                cadreGainAlgo.addWidget(labelAlgo, i-1, 0)
            if self.listAlgo[i] == 5:
                labelAlgo = QtGui.QLabel("Gain Algo UCB")
                cadreGainAlgo.addWidget(labelAlgo, i-1, 0)     

            self.listResAlgo.append(QtGui.QLabel(format(0,'.2f')))
            cadreGainAlgo.addWidget(self.listResAlgo[i-1], i-1, 1)

        algo = QtGui.QHBoxLayout()
        algo.addLayout(cadreGainAlgo)

        groupAlgo = QtGui.QGroupBox("Partie Algo")
        groupAlgo.setLayout(algo)

        ###################
        #Partie Principale#
        ###################

        principal = QtGui.QVBoxLayout()
        principal.addWidget(groupJoueur)
        principal.addWidget(groupAlgo)
        principal.addStretch(1)
        
        self.setLayout(principal)
        

    def buttonClicked(self):
      
        sender = self.sender()
        num = int(sender.text()) - 1
        self.moteurJeu.actionnerBrasJoueur(num)
        self.moteurJeu.lancerAlgo()
        self.moyenneBras[num].setText(str(format(self.moteurJeu.esperanceJoueur(num),'.2f')))
        self.nombreFoisJoueBras[num].setText(str(self.moteurJeu.nombreFoisJoueBrasJoueur(num)))
        self.resultatGain.setText(str(format(self.moteurJeu.gain(0), '.2f')))
        
        self.resultatNbCoupsJoue.setText(str(self.moteurJeu.nombreCoupsJoue()))

        for i in range(1, len(self.moteurJeu.listAlgorithme)):
            self.listResAlgo[i-1].setText(str(format(self.moteurJeu.gain(i), '.2f')))

        if self.moteurJeu.nombreCoupsJoue() == self.moteurJeu.nbCoupsMax:
            self.labelGainEspere.setVisible(True)
            self.resultatGainEspere.setVisible(True)
            for i in range(0, len(self.listBout)):
                self.listBout[i].setDisabled(True)
