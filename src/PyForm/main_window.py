from email import message
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

from AnisoDiffusion.images import *

from PyUi.main_window import Ui_MainWindow
from PyForm.parameters import Parameters

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)

        self.name = None
        self.image = None
        self.imageList = []

        self.menuFile.triggered[QAction].connect(self.MenuFile)

    def resizeEvent(self, event):
        width = self.width()/2
        height = (self.height() - 44)/2

        self.listView.setGeometry(0, 0, width, height)
        self.imgView_1.setGeometry(width, 0, width, height)
        self.imgView_2.setGeometry(0, height, width, height)
        self.imgView_3.setGeometry(width, height, width, height)

    def MenuFile(self, triggered):
        if triggered.text() == 'Load Image':
            self.LoadImageAction()

    def LoadImageAction(self):
        path, filter = QFileDialog.getOpenFileName(self, directory='../img', caption='Load Image', filter='Image File (*.jpg  *.png)')
        if not path: return

        param = Parameters()
        param.exec_()

        if not param.value : return
        #param = (param.t, param.updb, param.updf, param.num_seg, param.h, param.sigma, param.edge)
        param = (4, 0.1765, 0.0179, 8, 0.25, 1, param.edge)

        name = proccess_image(param, path)

        self.imgView_1.setPixmap(QPixmap(f'.temp/{name}.jpg'))
        self.imgView_2.setPixmap(QPixmap(f'.temp/{name}_edge.jpg'))
        self.imgView_3.setPixmap(QPixmap(f'.temp/{name}_diff.jpg'))

