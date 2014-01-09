from numpy import arange, sin, pi
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

from PyQt4 import QtGui, QtCore

class Graphe(FigureCanvas):
    """Ultimately, this is a QWidget (as well as a FigureCanvasAgg, etc.)."""
    def __init__(self, moteur, parent=None, dpi=100):
        fig = Figure(figsize=(100, moteur.nbCoupsMax), dpi=dpi)

        self.moteur=moteur

        self.axes = fig.add_subplot(111)

        self.compute_initial_figure()

        FigureCanvas.__init__(self, fig)
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)

    def compute_initial_figure(self):
        self.axes.set_xlabel("Nombre de coups",fontsize=9)
        self.axes.set_ylabel("Gain",fontsize=9)
    
        for nom, i in zip(self.moteur.listAlgorithme, range(0,len(self.moteur.listAlgorithme))):
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
            self.axes.plot(nom.histoGain,label=name)
        
        self.axes.legend = self.axes.legend(loc='upper left', shadow=True, fontsize='x-small')
