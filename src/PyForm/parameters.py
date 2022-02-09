from PyUi.parameters import *
from PyQt5.QtWidgets import *

class Parameters(QDialog, Ui_Dialog):
    def __init__(self):
        QDialog.__init__(self)
        self.setupUi(self)

        self.t = 0
        self.h = 0
        self.updb = 0
        self.updf = 0
        self.sigma = 0
        self.num_seg = 0

        self.edge = ''
        self.value = False

        self.buttonBox.accepted.connect(self.AcceptedAction)

    def AcceptedAction(self):
        self.value = True
        self.h = int(self.constSpin.text())
        self.edge = self.edgeBox.currentText()
        self.t = int(self.iterationSpin.text())
        self.updb = float(self.updbSpin.text())
        self.updf = float(self.updfSpin.text())
        self.sigma = int(self.sigmaSpin.text())
        self.num_seg = int(self.clusterSpin.text())