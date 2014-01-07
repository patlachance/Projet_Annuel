from PyQt4 import QtGui, QtCore

class GameZone(QtGui.QWidget):
    
    def __init__(self, moteurJeu):

        super(GameZone, self).__init__()
        self.moteurJeu = moteurJeu
        self.initUI()

    def initUI(self):

        ###################
        #Partie Principale#
        ###################
        principal = QtGui.QVBoxLayout()
        principal.addWidget(self.initJoueur())
        principal.addWidget(self.initAlgo())
        principal.addStretch(1)
        
        self.setLayout(principal)
        
        self.setWindowTitle('Jeu du manchot')
        self.show()

    def initJoueur(self):

        ###############
        #Partie Joueur#
        ###############

        if self.moteurJeu.listAlgorithme[0].numAlgo == 0:

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

            cadreJoueur.setRowStretch(0, 1)
            cadreJoueur.setColumnStretch(6, 1)

            self.listBout = []

            for i in range(0, self.moteurJeu.nbBras):
                self.listBout.append(QtGui.QPushButton(str(i+1)))   
                self.listBout[i].setFixedSize(60,60) 
                self.listBout[i].setStyleSheet("background-image:url(button-red.png); color:white;")
                self.listBout[i].clicked.connect(self.buttonClicked)
                cadreJoueur.addWidget(self.listBout[i],3,i)
                   
            labelGainMoyenBras = QtGui.QLabel("Gain moyen par bras : ")
            labelGainMoyenBras.setStyleSheet("border: 0px;")
            cadreJoueur.addWidget(labelGainMoyenBras, 4, 0, 1, self.moteurJeu.nbBras)

            labelNombreCoupsBras = QtGui.QLabel("Nombre de coups par bras ")
            labelNombreCoupsBras.setStyleSheet("border: 0px;")
            cadreJoueur.addWidget(labelNombreCoupsBras, 1, 0, 1, self.moteurJeu.nbBras)
            
            self.moyenneBras = []
            self.nombreFoisJoueBras = []

            for i in range(0, self.moteurJeu.nbBras):
                self.moyenneBras.append(QtGui.QLabel(format(0, '.2f')))
                self.moyenneBras[i].setAlignment(QtCore.Qt.AlignCenter)
                cadreJoueur.addWidget(self.moyenneBras[i], 5, i)
                
                self.nombreFoisJoueBras.append(QtGui.QLabel("0"))
                self.nombreFoisJoueBras[i].setAlignment(QtCore.Qt.AlignCenter)
                cadreJoueur.addWidget(self.nombreFoisJoueBras[i], 2, i)

            joueur = QtGui.QHBoxLayout()
            joueur.addLayout(cadreGain)
            joueur.addStretch(1)
            joueur.addLayout(cadreJoueur)
            joueur.addStretch(1)
            
            groupJoueur = QtGui.QGroupBox("Partie Joueur")
            groupJoueur.setLayout(joueur)

            return groupJoueur
        
        else:
            return QtGui.QLabel("")

    def initAlgo(self):

        #############
        #Partie Algo#
        #############

        if (((self.moteurJeu.listAlgorithme[0].numAlgo == 0) and (len(self.moteurJeu.listAlgorithme)!= 1)) or (self.moteurJeu.listAlgorithme[0].numAlgo != 0)):
            cadreGainAlgo = QtGui.QGridLayout()
            cadreGainAlgo.setColumnStretch(3, 1)

            self.listResAlgo = []
            
            if self.moteurJeu.listAlgorithme[0].numAlgo == 0:
                tmp = 1
            else:
                tmp = 0

            for i in range(tmp, len(self.moteurJeu.listAlgorithme)):

                if self.moteurJeu.listAlgorithme[i].numAlgo == 1:
                    labelAlgo = QtGui.QLabel("Gain Algo hasard")
                    cadreGainAlgo.addWidget(labelAlgo, i-tmp, 0)
                if self.moteurJeu.listAlgorithme[i].numAlgo == 2:
                    labelAlgo = QtGui.QLabel("Gain Algo Glouton")
                    cadreGainAlgo.addWidget(labelAlgo, i-tmp, 0)
                if self.moteurJeu.listAlgorithme[i].numAlgo == 3:
                    labelAlgo = QtGui.QLabel("Gain Algo Espilon")
                    cadreGainAlgo.addWidget(labelAlgo, i-tmp, 0)
                if self.moteurJeu.listAlgorithme[i].numAlgo == 4:
                    labelAlgo = QtGui.QLabel("Gain Algo Moyenne Gain")
                    cadreGainAlgo.addWidget(labelAlgo, i-tmp, 0)
                if self.moteurJeu.listAlgorithme[i].numAlgo == 5:
                    labelAlgo = QtGui.QLabel("Gain Algo UCB")
                    cadreGainAlgo.addWidget(labelAlgo, i-tmp, 0)

                self.listResAlgo.append(QtGui.QLabel(format(0, '.2f')))
                cadreGainAlgo.addWidget(self.listResAlgo[i-tmp], i-tmp, 1)

            algo = QtGui.QHBoxLayout()
            algo.addLayout(cadreGainAlgo)

            groupAlgo = QtGui.QGroupBox("Partie Algo")
            groupAlgo.setLayout(algo)

            return groupAlgo
        else:
            return QtGui.QLabel("")

    def buttonClicked(self):
      
        sender = self.sender()
        num = int(sender.text()) - 1
        self.moteurJeu.actionnerBrasJoueur(num)
        self.moteurJeu.lancerAlgo(1)
        self.moyenneBras[num].setText(str(format(self.moteurJeu.esperanceJoueur(num),'.2f')))
        self.nombreFoisJoueBras[num].setText(str(self.moteurJeu.nombreFoisJoueBrasJoueur(num)))
        self.resultatGain.setText(str(format(self.moteurJeu.gain(0), '.2f')))
        
        self.resultatNbCoupsJoue.setText(str(self.moteurJeu.nombreCoupsJoue()))
        self.affichageAlgo(1)
        if self.moteurJeu.nombreCoupsJoue() == self.moteurJeu.nbCoupsMax:
            self.labelGainEspere.setVisible(True)
            self.resultatGainEspere.setVisible(True)
            for i in self.listBout:
                i.setDisabled(True)

    def auto(self):
        for i in range(0, self.moteurJeu.nbCoupsMax):
            self.moteurJeu.lancerAlgo(0)
        self.affichageAlgo(0)

    def affichageAlgo(self, tmp):
        for i in range(tmp, len(self.moteurJeu.listAlgorithme)):
            self.listResAlgo[i-tmp].setText(str(format(self.moteurJeu.gain(i),'.2f')))
        
