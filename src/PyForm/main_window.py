from ast import arg
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

from os import remove, scandir

from AnisoDiffusion.proccess import *
from AnisoDiffusion.images import read_image, save_image

from PyUi.main_window import Ui_MainWindow
from PyForm.parameters import Parameters

from _thread import start_new_thread

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)

        self.first = True
        self.imageList = {}
        self.imageParent = {}

        self.menuFile.triggered[QAction].connect(self.MenuFile)
        self.treeWidget.clicked.connect(self.SelectItemAction)

        self.statBar = QStatusBar()
        self.setStatusBar(self.statBar)

    def resizeEvent(self, event):
        width = self.width()/2
        height = (self.height() - 44)/2

        self.treeWidget.setGeometry(0, 0, width, height)
        self.imgView_1.setGeometry(width, 0, width, height)
        self.imgView_2.setGeometry(0, height, width, height)
        self.imgView_3.setGeometry(width, height, width, height)

    def MenuFile(self, triggered):
        if triggered.text() == 'Load Image':
            self.LoadImageAction()
        if triggered.text() == 'Save Image':
            self.SaveAction()
        if triggered.text() == 'Remove Image':
            self.RemoveAction()
        if triggered.text() == 'Exit':
            self.clearTemp()
            self.close()

    def LoadImageAction(self):
        path, filter = QFileDialog.getOpenFileName(self, directory='../img', caption='Load Image', filter='Image File (*.jpg  *.png)')
        if not path: return

        param = Parameters()
        param.exec_()

        if not param.value : return
        param = (param.t, param.updb, param.updf, param.num_seg, param.sigma, param.coeff, param.edge)

        start_new_thread(proccess_image, (param, path, self))

    def LoadImage(self, name):
        self.imgView_1.setPixmap(QPixmap(f'.temp/{name}.jpg'))
        self.imgView_2.setPixmap(QPixmap(f'.temp/{name}_edge.jpg'))
        self.imgView_3.setPixmap(QPixmap(''))

    def SelectItemAction(self):
        name = self.treeWidget.currentItem().text(0)
        parent = self.imageParent[name]
        self.LoadImage(parent)
        if name != parent:
            self.imgView_3.setPixmap(QPixmap(f'.temp/{name}_diff.jpg'))

    def SaveAction(self):
        path = QFileDialog.getExistingDirectory(self, directory='../img/', caption='Save Image')
        
        if not path:return
        tup = self.GetSaveName()
        
        image = read_image(f'.temp/{tup[0]}.jpg')
        image_edge = read_image(f'.temp/{tup[1]}.jpg')
        image_diff = read_image(f'.temp/{tup[2]}.jpg')

        save_image(image, tup[0], path)
        save_image(image_edge, tup[1], path)
        save_image(image_diff, tup[2], path)
    
    def RemoveAction(self):
        name = self.treeWidget.currentItem().text(0)
        parent = self.imageParent[name]

        if name == parent:
            self.treeWidget.invisibleRootItem().removeChild(self.imageList[name])
        else:
            self.imageList[parent].removeChild(self.imageList[name])
        
    def GetSaveName(self):
        name = self.treeWidget.currentItem().text(0)
        parent = self.imageParent[name]
        if name == parent: return (parent, f'{parent}_edge', '')
        else: return (parent, f'{parent}_edge', f'{name}_diff')

    def closeEvent(self, even):
        self.clearTemp()
        return super().closeEvent(even)

    def clearTemp(self):
        for x in [arch.name for arch in scandir('.temp') if arch.is_file()]:
            remove(f'.temp/{x}')