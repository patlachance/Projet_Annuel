from PyQt4 import QtGui, QtCore
import random

class GuiBras(QtGui.QWidget):

    def __init__(self, validateButton):
        super(GuiBras, self).__init__()

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
        self.proba.textEdited.connect(self.chekValidityProba)
        self.gain.textEdited.connect(self.chekValidityGain)
        self.setLayout(hLayout)


    def setLabelBras(self, num):

        self.labelBras.setText("Bras n°" + str(num + 1))


    def chekValidityProba(self):

        proba = 0
        validity = True

        try:
            if self.proba.displayText() != '':
                proba = float(self.proba.displayText())
            else:
                proba = 0

        except ValueError:
            validity = False
        finally:
            if proba < 0 or proba > 1:
                validity = False

        self.emit(QtCore.SIGNAL(self.validateButton.setDisabled(not validity)))


    def chekValidityGain(self):

        gain = 0
        validity = True

        try:
            if self.gain.displayText() != '':
                gain = float(self.gain.displayText())
            else:
                gain = 0

        except ValueError:
            validity = False
        finally:
            if gain < 0 or gain > 1:
                validity = False

        self.emit(QtCore.SIGNAL(self.validateButton.setDisabled(not validity)))


    def randomButton(self):

        if self.proba.displayText() != '':
            self.gain.setText(str(format(random.random(), '.2f')))
        elif self.gain.displayText() != '':
            self.proba.setText(str(format(random.random(), '.2f')))
        else:
            self.proba.setText(str(format(random.random(), '.2f')))
            self.gain.setText(str(format(random.random(), '.2f')))