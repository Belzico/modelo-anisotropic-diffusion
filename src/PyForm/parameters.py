from PyUi.parameters import *
from PyQt5.QtWidgets import *
import docReader

class Parameters(QDialog, Ui_Dialog):
    def __init__(self):
        QDialog.__init__(self)
        self.setupUi(self)

        self.t = 0
        self.updb = 0
        self.updf = 0
        self.sigma = 0
        self.num_seg = 0

        self.edge = ''
        self.coeff = ''
        self.value = False

        self.buttonBox.accepted.connect(self.AcceptedAction)

    def AcceptedAction(self):
        self.value = True
        self.edge = self.edgeBox.currentText()
        self.coeff = self.coeffBox.currentText()
        self.t = int(self.iterationSpin.text())
        self.updb = float(self.updbSpin.text())
        self.updf = float(self.updfSpin.text())
        self.sigma = int(self.sigmaSpin.text())
        self.num_seg = int(self.clusterSpin.text())
        print('a')
        
    def defaultParams(self):
        self.t = 10
        self.updb = 0.17650
        self.updf = 0.01790
        self.sigma = 1
        self.num_seg = 8

        self.edge = 'Scharr'
        self.coeff = "Perona and Malik II"
        self.value = True