from PyQt4 import QtGui,QtCore

import moteur

class Resultat(QtGui.QWidget):
    
    def __init__(self, moteurJeu):
        super(Resultat, self).__init__()
        self.moteurJeu = moteurJeu
        self.initUI()

    def initUI(self):

        #############################
        #Liste Bras Probabilité/Gain#
        #############################
        principal = QtGui.QGridLayout()
        self.setStyleSheet(" border:1px solid #000000; ")

        for i in range(0,len(self.moteurJeu.listBras)):
            principal.addWidget(QtGui.QLabel(str(i + 1)),0,i+1)
        principal.addWidget(QtGui.QLabel("Bras"),0,0)
        principal.addWidget(QtGui.QLabel("Gain"),1,0)
        principal.addWidget(QtGui.QLabel("Probabilité"),2,0)

        for bras, i in zip(self.moteurJeu.listBras, range(0,len(self.moteurJeu.listBras))):
            principal.addWidget(QtGui.QLabel(str(format(bras.gain,'.2f'))),1,i+1)
            principal.addWidget(QtGui.QLabel(str(format(bras.proba,'.2f'))),2,i+1)
        
        for nom, i in zip(self.moteurJeu.listAlgorithme, range(0,len(self.moteurJeu.listAlgorithme))):
            if nom.numAlgo == 0:
                name="Joueur"
            elif nom.numAlgo == 1:
                name="Algo hasard"
            elif nom.numAlgo == 2:
                name="Algo Glouton"
            elif nom.numAlgo == 3:
                name="Algo Espilon"
            elif nom.numAlgo == 4:
                name="Algo Moyenne Gain"
            elif nom.numAlgo == 5:
                name="Algo UCB"
            principal.addWidget(QtGui.QLabel(name),3+i,0)
        

        for algo, i in zip(self.moteurJeu.listAlgorithme, range(0,len(self.moteurJeu.listAlgorithme))):
            for res, j in zip(algo.listBras, range(0,len(self.moteurJeu.listBras))):
                nbAction = res.nbFoisActionne
                if nbAction < self.moteurJeu.nbCoupsMax/4:
                    couleur = "#00FFFF"
                elif nbAction < self.moteurJeu.nbCoupsMax/2:
                    couleur = "#00FF00"
                elif nbAction < self.moteurJeu.nbCoupsMax - self.moteurJeu.nbCoupsMax/4:
                    couleur = "#FFFF00"
                else:
                    couleur = "#FF0000"
                labelTmp = QtGui.QLabel(str(res.nbFoisActionne))
                labelTmp.setStyleSheet("QLabel { background-color: "+ couleur +";}")
                principal.addWidget(labelTmp,3+i,j+1)
        
        self.setLayout(principal)
        self.show()
