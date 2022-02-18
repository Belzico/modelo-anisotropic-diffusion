# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './UiForm/about_app.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AboutApp(object):
    def setupUi(self, AboutApp):
        AboutApp.setObjectName("AboutApp")
        AboutApp.resize(734, 435)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./UiForm/../../icons/python.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        AboutApp.setWindowIcon(icon)
        self.gridLayout = QtWidgets.QGridLayout(AboutApp)
        self.gridLayout.setObjectName("gridLayout")
        self.buttonBox = QtWidgets.QDialogButtonBox(AboutApp)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 2, 0, 1, 1)
        self.textBrowser = QtWidgets.QTextBrowser(AboutApp)
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout.addWidget(self.textBrowser, 1, 0, 1, 1)
        self.label = QtWidgets.QLabel(AboutApp)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.retranslateUi(AboutApp)
        self.buttonBox.accepted.connect(AboutApp.accept)
        self.buttonBox.rejected.connect(AboutApp.reject)
        QtCore.QMetaObject.connectSlotsByName(AboutApp)

    def retranslateUi(self, AboutApp):
        _translate = QtCore.QCoreApplication.translate
        AboutApp.setWindowTitle(_translate("AboutApp", "About App"))
        self.textBrowser.setHtml(_translate("AboutApp", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:16pt; color:#ffffff;\">The detection of edges in a digital image allowsa reduction in the cost os storage and in turn a great abstraction of information. Specifically, the detection of edges in medical image allows us to distinguish the presence of anomalies as a support for medical diagnosis.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; color:#ffffff;\">The objective of this work is to implement an application that couples the Perona-Malik anisotropic diffusion model with at least three edge detectors for digital images. The In addition to being able to count on an edge image corresponding to a given original image, the user wants to know the influence of the diffusion coefficient on the final result.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; color:#ffffff;\">This application was conceived in python3, so a deep knowledge of the programming language is necessary for its understanding. In addition, it runs on both Windows and Linux as long as the necessary packages are installed.</span></p></body></html>"))
        self.label.setText(_translate("AboutApp", "<html><head/><body><p align=\"center\">About App</p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AboutApp = QtWidgets.QDialog()
    ui = Ui_AboutApp()
    ui.setupUi(AboutApp)
    AboutApp.show()
    sys.exit(app.exec_())
