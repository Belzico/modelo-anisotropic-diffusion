import imageio
import webbrowser

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

from threading import Thread
from os import remove, scandir, mkdir

from Diffusion.proccess import *
from Diffusion.measure import quality_measures
from Diffusion.images import read_image, save_image, get_name

from PyUi.help import Ui_Help
from PyUi.about_app import Ui_AboutApp
from PyForm.parameters import Parameters
from PyUi.main_window import Ui_MainWindow
from PyUi.about_authors import Ui_AboutAuthors



class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        
        #mine JJ
        self.picturesList=None
        
        try:
            mkdir('.temp')
        except:
            pass
        
        self.name = None
        self.parent = None
        self.iterations = None
        
        self.img_1_width = 0
        self.img_1_height = 0

        self.img_2_width = 0
        self.img_2_height = 0

        self.img_3_width = 0
        self.img_3_height = 0

        self.img_4_width = 0
        self.img_4_height = 0

        self.imageList = {}
        self.imageSize = {}
        self.imageParent = {}

        self.showImage = 0
        self.countProcc = 0

        self.menuFile.triggered[QAction].connect(self.MenuFile)
        self.menuFilter.triggered[QAction].connect(self.MenuFilter)
        self.menuView.triggered[QAction].connect(self.MenuView)
        self.treeWidget.clicked.connect(self.SelectItemAction)
        self.menuOptions.triggered[QAction].connect(self.MenuOptions)

        self.scrollArea_1.setWidget(self.imgView_1)
        self.scrollArea_2.setWidget(self.imgView_2)
        self.scrollArea_3.setWidget(self.imgView_3)
        self.scrollArea_4.setWidget(self.imgView_4)

        self.minusImage_1.clicked.connect(self.MinusImage_1)
        self.minusImage_2.clicked.connect(self.MinusImage_2)
        self.minusImage_3.clicked.connect(self.MinusImage_3)
        self.minusImage_4.clicked.connect(self.MinusImage_4)

        self.plusImage_1.clicked.connect(self.PlusImage_1)
        self.plusImage_2.clicked.connect(self.PlusImage_2)
        self.plusImage_3.clicked.connect(self.PlusImage_3)
        self.plusImage_4.clicked.connect(self.PlusImage_4)

        self.showImage_1.clicked.connect(self.ShowImage_1)
        self.showImage_2.clicked.connect(self.ShowImage_2)
        self.showImage_3.clicked.connect(self.ShowImage_3)
        self.showImage_4.clicked.connect(self.ShowImage_4)

        self.statBar = QStatusBar()
        self.setStatusBar(self.statBar)
        self.imgView_2.setFrameShape(QFrame.WinPanel)
        self.SetEnable(False)

    def resizeEvent(self, event):
        rest = 310 if self.actionImages_Tree.isChecked() else 0

        self.treeWidget.setGeometry(10, 10, int(rest - 10), int(self.height() - 74))
        
        if self.showImage == 0:
            width = (self.width() - rest - 30) / 2
            height = (self.height() - 74) / 2
            width1 = (self.width() - rest - 30) / 2
            height1 = (self.height() - 74) / 2
        else:
            width = (self.width() - rest - 30)
            height = (self.height() - 74)
            width1 = 0
            height1 = 0
            
        #jj fix    
        width=int(width)
        height=int(height)
        width1=int(width1)
        height1=int(height1)
        #.....
        
        self.groupBox_1.setGeometry(int(rest + 10), 10, int(width), int(height))
        self.groupBox_2.setGeometry(int(rest + width1 + 20), 10, int(width), int(height))
        self.groupBox_3.setGeometry(int(rest + 10), int(height1 + 10), int(width), int(height))
        self.groupBox_4.setGeometry(int(rest + width1 + 20), int(height1 + 10), int(width), int(height))

        self.imgView_1.setGeometry(0, 16, int(width), int(height))
        self.scrollArea_1.setGeometry(0, 16, int(width), int(height-20))
        self.showImage_1.setGeometry(10, int(height - 55), 30, 30)
        self.plusImage_1.setGeometry(int(width) - 50, 20, 30, 30)
        self.minusImage_1.setGeometry(int(width - 85), 20, 30, 30)
        
        self.imgView_2.setGeometry(0, 16, width, height)
        self.scrollArea_2.setGeometry(0, 16, width, height-20)
        self.showImage_2.setGeometry(10, height - 55, 30, 30)
        self.plusImage_2.setGeometry(width - 50, 20, 30, 30)
        self.minusImage_2.setGeometry(width - 85, 20, 30, 30)

        self.imgView_3.setGeometry(0, 16, width, height)
        self.scrollArea_3.setGeometry(0, 16, width, height-20)
        self.showImage_3.setGeometry(10, height - 55, 30, 30)
        self.plusImage_3.setGeometry(width - 50, 20, 30, 30)
        self.minusImage_3.setGeometry(width - 85, 20, 30, 30)

        self.imgView_4.setGeometry(0, 16, width, height)
        self.scrollArea_4.setGeometry(0, 16, width, height-20)
        self.showImage_4.setGeometry(10, height - 55, 30, 30)
        self.plusImage_4.setGeometry(width - 50, 20, 30, 30)
        self.minusImage_4.setGeometry(width - 85, 20, 30, 30)

    def MenuOptions(self, triggered):
        if triggered.text() == 'Help':
            self.HelpAction()
        if triggered.text() == 'Orientation':
            self.OrientationAction()
        if triggered.text() == 'Report':
            self.ReportAction()
        if triggered.text() == 'About the Authors':
            self.AboutAuthorsAction()
        if triggered.text() == 'About the App':
            self.AboutAppAction()

    def HelpAction(self):
        dialog = QDialog()
        ui_dialog = Ui_Help()
        ui_dialog.setupUi(dialog)
        dialog.exec()

    def OrientationAction(self):
        path = '../doc/Bordes Imagenes Medicas.pdf'
        webbrowser.open_new(path)

    def ReportAction(self):
        path = '../doc/Barrera-Plasencia-Leon Influencia del Suavizado por Difusion Anisotropica en Imagenes de Ultrasonido.pdf'
        webbrowser.open_new(path)

    def AboutAuthorsAction(self):
        dialog = QDialog()
        ui_dialog = Ui_AboutAuthors()
        ui_dialog.setupUi(dialog)
        dialog.exec()

    def AboutAppAction(self):
        dialog = QDialog()
        ui_dialog = Ui_AboutApp()
        ui_dialog.setupUi(dialog)
        dialog.exec()

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

    def MenuFilter(self, triggered):
        if triggered.text() == 'Anisotropic Diffusion':
            self.AnisotropicDiffusion()
        if triggered.text() == 'View GIF':
            self.CreateGif()

    def CreateGif(self):
        frames = []

        for i in range(1, self.iterations + 1):
            image_path = f'.temp/{self.name}_{i}_edge_diff.jpg'
            frames.append(imageio.imread(image_path))
        
        imageio.mimsave(f'.temp/{self.name}.gif', frames, 'GIF', duration=0.5)

    def MenuView(self, triggered):
        if triggered.text() == 'Image Tree':
            self.treeWidget.setHidden(not self.actionImages_Tree.isChecked())
        self.resizeEvent(None)

    def LoadImageAction(self):
        path,_ = QFileDialog.getOpenFileName(self, directory='../img', caption='Load Image', filter='Image File (*.jpg  *.png)')
        if not path:
            return

        self.name = self.parent = get_name(path)
        
        if self.name in self.imageList:
            return
        
        self.imageParent[self.name] = self.name
        self.imageList[self.name] = QTreeWidgetItem(self.treeWidget, [self.name])

        image = read_image(path)
        save_image(image, self.name)

        self.img_1_height = self.img_2_height = self.img_3_height = self.img_4_height = self.imgView_1.height()
        self.img_1_width = self.img_2_width = self.img_3_width = self.img_4_width = self.imgView_1.width()

        self.imageSize[self.name] = (self.img_1_width, self.img_1_height)
        
        self.ClearImage()
        self.imgView_1.setPixmap(QPixmap(f'.temp/{self.parent}').scaled(self.img_1_width, self.img_1_height, Qt.KeepAspectRatio))
        self.SetEnable(True)

    #ffffffffffffffffffffffffffffffffffffff
    def AnisotropicDiffusion(self):
        param = Parameters()
        param.defaultParams()

        if not param.value:
            return
        
        param = (param.t, param.updb, param.updf, param.num_seg, param.sigma, param.coeff, param.edge)
        self.iterations = param[0]

        for image in self.picturesList:
            thread = Thread(target=proccess_image, args=(image, param, self))
            thread.setDaemon(True)
            thread.start()

    def ClearImage(self):
        self.imgView_1.setPixmap(QPixmap(f''))
        self.imgView_2.setPixmap(QPixmap(f''))
        self.imgView_3.setPixmap(QPixmap(f''))
        self.imgView_4.setPixmap(QPixmap(f''))

    def SelectItemAction(self):
        self.name = self.treeWidget.currentItem().text(0)
        self.parent = self.imageParent[self.name]

        self.ClearImage()
        temp = self.imageSize[self.parent]
        self.img_1_width = temp[0]
        self.img_1_height = temp[1]
        
        self.imgView_1.setPixmap(QPixmap(f'.temp/{self.parent}').scaled(self.img_1_width, self.img_1_height, Qt.KeepAspectRatio))
        
        if self.name != self.parent:     
            self.img_4_width = self.img_2_width = self.img_3_width = temp[0]
            self.img_4_height = self.img_2_height =  self.img_3_height = temp[1]
            self.imgView_2.setPixmap(QPixmap(f'.temp/{self.name}_diff').scaled(self.img_2_width, self.img_2_height, Qt.KeepAspectRatio))
            self.imgView_3.setPixmap(QPixmap(f'.temp/{self.parent}_edge').scaled(self.img_3_width, self.img_3_height, Qt.KeepAspectRatio))
            self.imgView_4.setPixmap(QPixmap(f'.temp/{self.name}_edge_diff').scaled(self.img_4_width, self.img_4_height, Qt.KeepAspectRatio))
            
            edge = read_image(f'.temp/{self.parent}_edge.jpg')
            diff_edge = read_image(f'.temp/{self.name}_edge_diff.jpg')
            measure = quality_measures(edge, diff_edge)
            self.groupBox_4.setStatusTip(f'AD-Edge Image --> (RMSE={str(measure[0])[:7]}, PSNR={str(measure[1])[:7]}, SNR={str(measure[2])[:7]})')
        else:
            self.groupBox_4.setStatusTip(f'AD-Edge Image')
        
    def SaveAction(self):
        if self.name is None:
            return
        path = QFileDialog.getExistingDirectory(self, directory='../img/', caption='Save Image')
        
        if not path:
            return
        tup = self.GetSaveName()
        
        image = read_image(f'.temp/{tup[0]}.jpg')
        try:
            #image_edge = read_image(f'.temp/{tup[1]}.jpg')
            image_diff = read_image(f'.temp/{tup[2]}.jpg')
        except:
            pass

        #save_image(image, tup[0], path)
        try:
            #save_image(image_edge, tup[1], path)
            
            #fffffffffffffffffffffffffffff
            #primer parametro no se toca, segundo nombre de la imagen, tercer parametro path
            save_image(image_diff, tup[2], path)
        except:
            pass

    def RemoveAction(self):
        if self.name is None or self.countProcc > 0:
            return

        if self.name == self.parent:
            self.treeWidget.invisibleRootItem().removeChild(self.imageList[self.name])
            self.ClearImage()
            self.SetEnable(False)
        else:
            self.imageList[self.parent].removeChild(self.imageList[self.name])
            # self.imgView_3.setPixmap(QPixmap(f''))
            # self.imgView_4.setPixmap(QPixmap(f''))
        
        self.imageList.pop(self.name)
        self.imageParent.pop(self.name)
        
        self.name = None
        self.parent = None

    def GetSaveName(self):
        parent = self.imageParent[self.name]
        if self.name == parent:
            return (parent, f'{parent}_edge', '')
        else:
            return (parent, f'{parent}_edge', f'{self.name}_diff')

    def closeEvent(self, even):
        self.clearTemp()
        return super().closeEvent(even)

    def clearTemp(self):
        for x in [arch.name for arch in scandir('.temp') if arch.is_file()]:
            remove(f'.temp/{x}')

    def MinusImage_1(self):
        if self.img_1_height == 0 or self.img_1_width == 0 or self.img_1_width - 100 <= 0 or self.name is None:
            return

        bixmap = QPixmap(f'.temp/{self.parent}')
        
        self.img_1_width -= 100
        self.img_1_height -= 100

        self.imgView_1.setPixmap(bixmap.scaled(self.img_1_width, self.img_1_height, Qt.KeepAspectRatio)) 
    
    def MinusImage_2(self):
        if self.img_2_height == 0 or self.img_2_width == 0 or self.img_2_width - 100 <= 0 or self.name is None:
            return

        bixmap = QPixmap(f'.temp/{self.parent}')
        
        self.img_2_width -= 100
        self.img_2_height -= 100

        self.imgView_2.setPixmap(bixmap.scaled(self.img_2_width, self.img_2_height, Qt.KeepAspectRatio))
    
    def MinusImage_3(self):
        if self.img_3_height == 0 or self.img_3_width == 0 or self.img_3_width - 100 <= 0 or self.name is None:
            return

        bixmap = QPixmap(f'.temp/{self.parent}_edge')
        
        self.img_3_width -= 100
        self.img_3_height -= 100

        self.imgView_3.setPixmap(bixmap.scaled(self.img_3_width, self.img_3_height, Qt.KeepAspectRatio))

    def MinusImage_4(self):
        if self.img_4_height == 0 or self.img_4_width == 0 or self.img_4_width - 100 <= 0 or self.name is None:
            return

        bixmap = QPixmap(f'.temp/{self.name}_diff')
        
        self.img_4_width -= 100
        self.img_4_height -= 100

        self.imgView_4.setPixmap(bixmap.scaled(self.img_4_width, self.img_4_height, Qt.KeepAspectRatio)) 

    def PlusImage_1(self):
        if self.img_1_height == 0 or self.img_1_width == 0 or self.img_1_width + 100 >= 10000 or self.name is None:
            return

        bixmap = QPixmap(f'.temp/{self.parent}')
        
        self.img_1_width += 100
        self.img_1_height += 100

        self.imgView_1.setPixmap(bixmap.scaled(self.img_1_width, self.img_1_height, Qt.KeepAspectRatio))

    def PlusImage_2(self):
        if self.img_2_height == 0 or self.img_2_width == 0 or self.img_2_width + 100 >= 10000 or self.name is None:
            return

        bixmap = QPixmap(f'.temp/{self.parent}')
        
        self.img_2_width += 100
        self.img_2_height += 100

        self.imgView_2.setPixmap(bixmap.scaled(self.img_2_width, self.img_2_height, Qt.KeepAspectRatio))

    def PlusImage_3(self):
        if self.img_3_height == 0 or self.img_3_width == 0 or self.img_3_width + 100 >= 10000 or self.name is None:
            return

        bixmap = QPixmap(f'.temp/{self.parent}_edge')
        
        self.img_3_width += 100
        self.img_3_height += 100

        self.imgView_3.setPixmap(bixmap.scaled(self.img_3_width, self.img_3_height, Qt.KeepAspectRatio))

    def PlusImage_4(self):
        if self.img_4_height == 0 or self.img_4_width == 0 or self.img_4_width + 100 >= 10000 or self.name is None:
            return

        bixmap = QPixmap(f'.temp/{self.name}_diff')
        
        self.img_4_width += 100
        self.img_4_height += 100

        self.imgView_4.setPixmap(bixmap.scaled(self.img_4_width, self.img_4_height, Qt.KeepAspectRatio))  

    def ShowImage_1(self):
        if self.showImage == 0:
            self.showImage = 1
            self.Hidden(1, True)
            self.showImage_1.setIcon(QIcon('../icons/hide.png'))
        elif self.showImage == 1:
            self.showImage = 0
            self.Hidden(1, False)
            self.showImage_1.setIcon(QIcon('../icons/no-hide.png'))
        self.resizeEvent(None)
    
    def ShowImage_2(self):
        if self.showImage == 0:
            self.showImage = 2
            self.Hidden(2, True)
            self.showImage_2.setIcon(QIcon('../icons/hide.png'))
        elif self.showImage == 2:
            self.showImage = 0
            self.Hidden(2, False)
            self.showImage_2.setIcon(QIcon('../icons/no-hide.png'))
        self.resizeEvent(None)
    
    def ShowImage_3(self):
        if self.showImage == 0:
            self.showImage = 3
            self.Hidden(3, True)
            self.showImage_3.setIcon(QIcon('../icons/hide.png'))
        elif self.showImage == 3:
            self.showImage = 0
            self.Hidden(3, False)
            self.showImage_3.setIcon(QIcon('../icons/no-hide.png'))
        self.resizeEvent(None)
    
    def ShowImage_4(self):
        if self.showImage == 0:
            self.showImage = 4
            self.Hidden(4, True)
            self.showImage_4.setIcon(QIcon('../icons/hide.png'))
        elif self.showImage == 4:
            self.showImage = 0
            self.Hidden(4, False)
            self.showImage_4.setIcon(QIcon('../icons/no-hide.png'))
        self.resizeEvent(None)

    def Hidden(self, num, val):
        if num != 1:
            self.groupBox_1.setHidden(val)
            self.imgView_1.setHidden(val)
            self.plusImage_1.setHidden(val)
            self.showImage_1.setHidden(val)
            self.minusImage_1.setHidden(val)
        if num != 2:
            self.groupBox_2.setHidden(val)
            self.imgView_2.setHidden(val)
            self.plusImage_2.setHidden(val)
            self.showImage_2.setHidden(val)
            self.minusImage_2.setHidden(val)
        if num != 3:
            self.groupBox_3.setHidden(val)
            self.imgView_3.setHidden(val)
            self.plusImage_3.setHidden(val)
            self.showImage_3.setHidden(val)
            self.minusImage_3.setHidden(val)
        if num != 4:
            self.groupBox_4.setHidden(val)
            self.imgView_4.setHidden(val)
            self.plusImage_4.setHidden(val)
            self.showImage_4.setHidden(val)
            self.minusImage_4.setHidden(val)

    def SetEnable(self, boolean):
        self.actionSave.setEnabled(boolean)
        self.actionRemove_Image.setEnabled(boolean)
        self.actionAnisotropic_Diffusion.setEnabled(boolean)
        self.actionView_GIF.setEnabled(boolean)
