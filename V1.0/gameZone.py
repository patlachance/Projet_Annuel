from PyQt4 import QtGui, QtCore

import moteur, resultat, graphe

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

        self.RESIZE = QtCore.pyqtSignal()

        self.initUI()
        self.setStyleSheet("background-color: #DFF2FF;")

    def initUI(self):
        """ Fenetre principale de la gamezone """
        self.principal = QtGui.QVBoxLayout()

        if self.moteurJeu.listAlgorithme[0].numAlgo == 0:

            boxGain = QtGui.QVBoxLayout()
            self.TabJoueur = self.initTabJoueur()
            boxGain.addWidget(self.TabJoueur)
            boxGain.addStretch(1)
            self.Algo = self.initAlgo()
            boxGain.addWidget(self.Algo)

            self.boxJeu = QtGui.QHBoxLayout()

            self.boxJeu.addLayout(boxGain)
            self.boxJeu.addStretch(1)
            self.boxJeu.addWidget(self.initBoutJoueur())

            self.principal.addLayout(self.boxJeu)

        else:

            pouet = QtGui.QHBoxLayout()
            pouet.addWidget(self.initAlgo())
            self.auto()     
            pouet.addStretch(1)
            pouet.addWidget(resultat.Resultat(self.moteurJeu))

            self.principal.addLayout(pouet)

            self.principal.addWidget(graphe.Graphe(self.moteurJeu))
            
        
        self.setLayout(self.principal)
        self.show()

    def initTabJoueur(self):
        """ Tableau récapitulatif du joueur """

        cadreGain = QtGui.QGridLayout()

        font=QtGui.QFont()
        font.setBold(True)

        labelGain = QtGui.QLabel("Gain")
        labelGain.setFont(font)
        cadreGain.addWidget(labelGain,1,0)

        self.resultatGain = QtGui.QLabel(format(0,'.2f'))
        self.resultatGain.setFont(font)
        cadreGain.addWidget(self.resultatGain,1,1)

        self.labelGainEspere = QtGui.QLabel("Gain espéré")
        cadreGain.addWidget(self.labelGainEspere,2,0)
        self.labelGainEspere.setVisible(False)

        self.resultatGainEspere = QtGui.QLabel(format(float(self.moteurJeu.gainEspere()),'.2f'))
        cadreGain.addWidget(self.resultatGainEspere,2,1)
        self.resultatGainEspere.setVisible(False)
        
        labelNbCoupsJoue = QtGui.QLabel("Nombre de coups")
        cadreGain.addWidget(labelNbCoupsJoue,3,0)


        self.resultatNbCoupsJoue = QtGui.QLabel("0")
        cadreGain.addWidget(self.resultatNbCoupsJoue,3,1)

        groupAlgo = QtGui.QGroupBox("Partie Joueur")
        groupAlgo.setLayout(cadreGain)
        #groupAlgo.setStyleSheet("background-color: #DFF2FF;")
        return groupAlgo

    def initBoutJoueur(self):

        cadreJoueur = QtGui.QGridLayout()
        icon = QtGui.QIcon("bras.gif")

        self.listBout = []

        for i in range(0,self.moteurJeu.nbBras):
            self.listBout.append(QtGui.QPushButton(str(i+1)))   
            self.listBout[i].setFixedSize(60,60) 
            self.listBout[i].setStyleSheet("background-image:url(button-red.png); color:white;")
            self.listBout[i].clicked.connect(self.buttonClicked)
            cadreJoueur.addWidget(self.listBout[i],3,i)
               
        labelGainMoyenBras = QtGui.QLabel("Gain moyen par bras : ")
        labelGainMoyenBras.setStyleSheet("border: 0px;")
        cadreJoueur.addWidget(labelGainMoyenBras,4,0,1,self.moteurJeu.nbBras)

        labelNombreCoupsBras = QtGui.QLabel("Nombre de coups par bras ")
        labelNombreCoupsBras.setStyleSheet("border: 0px;")
        cadreJoueur.addWidget(labelNombreCoupsBras,1,0,1,self.moteurJeu.nbBras)
        
        self.moyenneBras = []
        self.nombreFoisJoueBras = []

        for i in range(0,self.moteurJeu.nbBras):
            self.moyenneBras.append(QtGui.QLabel(format(0, '.2f')))
            self.moyenneBras[i].setAlignment(QtCore.Qt.AlignCenter)
            cadreJoueur.addWidget(self.moyenneBras[i],5,i)
            
            self.nombreFoisJoueBras.append(QtGui.QLabel("0"))
            self.nombreFoisJoueBras[i].setAlignment(QtCore.Qt.AlignCenter)
            cadreJoueur.addWidget(self.nombreFoisJoueBras[i],2,i)

        self.groupBout = QtGui.QGroupBox("Liste des bras")
        self.groupBout.setLayout(cadreJoueur)

        return self.groupBout

    def initAlgo(self):
        """ Partie Algo """

        if (((self.listAlgo[0]==0) and (len(self.listAlgo)!=1))or(self.listAlgo[0]!=0)):
            cadreGainAlgo = QtGui.QGridLayout()
            cadreGainAlgo.setColumnStretch(3,1)

            self.listResAlgo = []
            
            if self.listAlgo[0]==0:
                tmp=1
            else:
                tmp=0

            for i in  range(tmp,len(self.listAlgo)):

                if self.listAlgo[i] == 1:
                    labelAlgo = QtGui.QLabel("Gain Algo hasard")
                    cadreGainAlgo.addWidget(labelAlgo,i-tmp,0)
                if self.listAlgo[i] == 2:
                    labelAlgo = QtGui.QLabel("Gain Algo Glouton")
                    cadreGainAlgo.addWidget(labelAlgo,i-tmp,0)
                if self.listAlgo[i] == 3:
                    labelAlgo = QtGui.QLabel("Gain Algo Espilon")
                    cadreGainAlgo.addWidget(labelAlgo,i-tmp,0)
                if self.listAlgo[i] == 4:
                    labelAlgo = QtGui.QLabel("Gain Algo Moyenne Gain")
                    cadreGainAlgo.addWidget(labelAlgo,i-tmp,0)
                if self.listAlgo[i] == 5:
                    labelAlgo = QtGui.QLabel("Gain Algo UCB")
                    cadreGainAlgo.addWidget(labelAlgo,i-tmp,0)

                self.listResAlgo.append(QtGui.QLabel(format(0,'.2f')))
                cadreGainAlgo.addWidget(self.listResAlgo[i-tmp],i-tmp,1)

            algo = QtGui.QHBoxLayout()
            algo.addLayout(cadreGainAlgo)

            groupAlgo = QtGui.QGroupBox("Partie Algo")
            groupAlgo.setLayout(algo)
            #groupAlgo.setStyleSheet("background-color: #DFF2FF;")
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
            self.groupBout.setVisible(False)
            self.boxJeu.addWidget(resultat.Resultat(self.moteurJeu))

            self.principal.addWidget(graphe.Graphe(self.moteurJeu))
        
            self.emit(QtCore.SIGNAL("resize(int)"), self.size().height())

    def auto(self):
        for i in range(0,self.moteurJeu.nbCoupsMax):
            self.moteurJeu.lancerAlgo(0)
        self.affichageAlgo(0)

    def affichageAlgo(self,tmp):
        for i in range(tmp,len(self.listAlgo)):
            self.listResAlgo[i-tmp].setText(str(format(self.moteurJeu.gain(i),'.2f')))
        
