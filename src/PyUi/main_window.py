# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './UiForm/main_window.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 744)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.imgView_3 = QtWidgets.QLabel(self.centralwidget)
        self.imgView_3.setGeometry(QtCore.QRect(500, 0, 500, 350))
        self.imgView_3.setFrameShape(QtWidgets.QFrame.Box)
        self.imgView_3.setText("")
        self.imgView_3.setAlignment(QtCore.Qt.AlignCenter)
        self.imgView_3.setObjectName("imgView_3")
        self.imgView_1 = QtWidgets.QLabel(self.centralwidget)
        self.imgView_1.setGeometry(QtCore.QRect(0, 350, 500, 350))
        self.imgView_1.setFrameShape(QtWidgets.QFrame.Box)
        self.imgView_1.setLineWidth(1)
        self.imgView_1.setText("")
        self.imgView_1.setAlignment(QtCore.Qt.AlignCenter)
        self.imgView_1.setObjectName("imgView_1")
        self.imgView_2 = QtWidgets.QLabel(self.centralwidget)
        self.imgView_2.setGeometry(QtCore.QRect(500, 350, 500, 350))
        self.imgView_2.setFrameShape(QtWidgets.QFrame.Box)
        self.imgView_2.setText("")
        self.imgView_2.setAlignment(QtCore.Qt.AlignCenter)
        self.imgView_2.setObjectName("imgView_2")
        self.treeWidget = QtWidgets.QTreeWidget(self.centralwidget)
        self.treeWidget.setGeometry(QtCore.QRect(0, 0, 500, 350))
        self.treeWidget.setLineWidth(3)
        self.treeWidget.setTabKeyNavigation(False)
        self.treeWidget.setProperty("showDropIndicator", True)
        self.treeWidget.setHeaderHidden(True)
        self.treeWidget.setObjectName("treeWidget")
        self.treeWidget.headerItem().setText(0, "1")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1000, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionLoad_Image = QtWidgets.QAction(MainWindow)
        self.actionLoad_Image.setObjectName("actionLoad_Image")
        self.actionRemove_Image = QtWidgets.QAction(MainWindow)
        self.actionRemove_Image.setObjectName("actionRemove_Image")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionSave_All_Images = QtWidgets.QAction(MainWindow)
        self.actionSave_All_Images.setObjectName("actionSave_All_Images")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.menuFile.addAction(self.actionLoad_Image)
        self.menuFile.addAction(self.actionRemove_Image)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Malik-Images"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionLoad_Image.setText(_translate("MainWindow", "Load Image"))
        self.actionRemove_Image.setText(_translate("MainWindow", "Remove Image"))
        self.actionSave.setText(_translate("MainWindow", "Save Image"))
        self.actionSave_All_Images.setText(_translate("MainWindow", "Save All Images"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
