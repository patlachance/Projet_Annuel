from PyQt4 import QtGui, QtCore
import random

class GuiBras(QtGui.QWidget):

    def __init__(self, validateButton):
        super(GuiBras, self).__init__()

        self.index = -1
        self.infoGuiBras = []
        self.validateButton = validateButton
        self.labelBras = QtGui.QLabel()
        self.probaLabel = QtGui.QLabel("Probabilité ")
        self.gainLabel = QtGui.QLabel("Gain ")
        self.proba = QtGui.QLineEdit()
        self.gain = QtGui.QLineEdit()
        self.random = QtGui.QPushButton("Random")

        self.createBlocBras()

    def createBlocBras(self):

        hLayout = QtGui.QHBoxLayout()

        hLayout.addWidget(self.labelBras)
        hLayout.addSpacing(5)
        hLayout.addWidget(self.probaLabel)
        hLayout.addWidget(self.proba)
        hLayout.addSpacing(10)
        hLayout.addWidget(self.gainLabel)
        hLayout.addSpacing(5)
        hLayout.addWidget(self.gain)
        hLayout.addSpacing(10)
        hLayout.addWidget(self.random)

        self.proba.setFixedWidth(75)
        self.gain.setFixedWidth(75)
        self.random.setFixedWidth(75)

        self.random.clicked.connect(self.randomButton)
        self.proba.textEdited.connect(self.chekValidityGuiBras)
        self.gain.textEdited.connect(self.chekValidityGuiBras)
        self.setLayout(hLayout)


    def setLabelBras(self, num):

        self.index = num
        self.labelBras.setText("Bras n°" + str(num + 1))


    def chekValidityGuiBras(self):

        proba = 0
        gain = 0
        validityGain = True
        validityProba = True

        try:
            proba = float(self.proba.displayText())
        except ValueError:
            validityProba = False
        finally:
            if proba < 0 or proba > 1:
                validityProba = False
            if self.proba.displayText() == '':
                proba = ''
                validityProba = True

        try:
            gain = float(self.gain.displayText())
        except ValueError:
            validityGain = False
        finally:
            if gain < 0 or gain > 1:
                validityGain = False
            if self.gain.displayText() == '':
                gain = ''
                validityGain = True

        if validityProba and validityGain:
            self.setInfoGuiBras(self.index, proba, gain)
        elif validityProba:
            self.setInfoGuiBras(self.index, proba, '')
        elif validityGain:
            self.setInfoGuiBras(self.index, '', gain)

        self.emit(QtCore.SIGNAL(self.validateButton.setDisabled(not (validityProba and validityGain))))


    def randomButton(self):

        proba = 0
        gain = 0
        validityGain = True
        validityProba = True

        try:
            proba = float(self.proba.displayText())
        except ValueError:
            validityProba = False
        finally:
            if proba < 0 or proba > 1:
                validityProba = False

        try:
            gain = float(self.gain.displayText())
        except ValueError:
            validityGain = False
        finally:
            if gain < 0 or gain > 1:
                validityGain = False

        if validityGain:
            self.proba.setText(str(format(random.random(), '.2f')))
        elif validityProba:
            self.gain.setText(str(format(random.random(), '.2f')))
        else:
            self.proba.setText(str(format(random.random(), '.2f')))
            self.gain.setText(str(format(random.random(), '.2f')))

        self.chekValidityGuiBras()

    def getInfoGuiBras(self):

        return self.infoGuiBras

    def setInfoGuiBras(self, index, proba, gain):

        if len(self.infoGuiBras) == 0:
        
            self.infoGuiBras.append(index)
            self.infoGuiBras.append(proba)
            self.infoGuiBras.append(gain)
        else:
            self.infoGuiBras[1] = proba
            self.infoGuiBras[2] = gain
