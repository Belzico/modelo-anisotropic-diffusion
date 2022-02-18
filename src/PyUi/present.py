# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './UiForm/present.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Present(object):
    def setupUi(self, Present):
        Present.setObjectName("Present")
        Present.resize(500, 461)
        Present.setFocusPolicy(QtCore.Qt.ClickFocus)
        Present.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./UiForm/../../icons/python.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Present.setWindowIcon(icon)
        self.label = QtWidgets.QLabel(Present)
        self.label.setGeometry(QtCore.QRect(0, 0, 500, 461))
        self.label.setMinimumSize(QtCore.QSize(500, 461))
        self.label.setMaximumSize(QtCore.QSize(500, 461))
        self.label.setStyleSheet("backgraound-color: {rgb(37, 36, 36)};")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("./UiForm/../../icons/logo_small.png"))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.progressBar = QtWidgets.QProgressBar(Present)
        self.progressBar.setGeometry(QtCore.QRect(5, 440, 490, 15))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setFormat("")
        self.progressBar.setObjectName("progressBar")

        self.retranslateUi(Present)
        QtCore.QMetaObject.connectSlotsByName(Present)

    def retranslateUi(self, Present):
        _translate = QtCore.QCoreApplication.translate
        Present.setWindowTitle(_translate("Present", "Anisotropic Diffusion"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Present = QtWidgets.QWidget()
    ui = Ui_Present()
    ui.setupUi(Present)
    Present.show()
    sys.exit(app.exec_())
