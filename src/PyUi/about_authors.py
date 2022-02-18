# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './UiForm/about_authors.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AboutAuthors(object):
    def setupUi(self, AboutAuthors):
        AboutAuthors.setObjectName("AboutAuthors")
        AboutAuthors.resize(910, 610)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./UiForm/../../icons/python.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        AboutAuthors.setWindowIcon(icon)
        self.gridLayout = QtWidgets.QGridLayout(AboutAuthors)
        self.gridLayout.setObjectName("gridLayout")
        self.buttonBox = QtWidgets.QDialogButtonBox(AboutAuthors)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 2, 0, 1, 1)
        self.textBrowser = QtWidgets.QTextBrowser(AboutAuthors)
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout.addWidget(self.textBrowser, 1, 0, 1, 1)
        self.label = QtWidgets.QLabel(AboutAuthors)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.retranslateUi(AboutAuthors)
        self.buttonBox.accepted.connect(AboutAuthors.accept)
        self.buttonBox.rejected.connect(AboutAuthors.reject)
        QtCore.QMetaObject.connectSlotsByName(AboutAuthors)

    def retranslateUi(self, AboutAuthors):
        _translate = QtCore.QCoreApplication.translate
        AboutAuthors.setWindowTitle(_translate("AboutAuthors", "About Authors"))
        self.textBrowser.setHtml(_translate("AboutAuthors", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:24pt; font-weight:600; color:#ffffff;\">Students :</span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:24pt; color:#ffffff;\"> Reinaldo Barrera Travieso</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:7pt; color:#ffffff;\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:24pt; color:#ffffff;\">                   Ariel Plasencia Díaz</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; color:#ffffff;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:24pt; font-weight:600; color:#ffffff;\">Tutor :</span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:24pt; color:#ffffff;\"> Dr. Ángela León Mecías</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\'; color:#ffffff;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:24pt; font-weight:600; color:#ffffff;\">Emails :</span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:24pt; color:#ffffff;\"> reinaldobarrera9601@gmail.com</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:7pt; color:#ffffff;\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:24pt; color:#ffffff;\">               arielplasencia00@gmial.com</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:7pt; color:#ffffff;\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:24pt; color:#ffffff;\">               aleonmecias@gmail.com</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:6pt; color:#ffffff;\"> </span><span style=\" font-family:\'MS Shell Dlg 2\'; color:#ffffff;\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:24pt; font-weight:600; color:#ffffff;\">Faculty :</span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:24pt; color:#ffffff;\"> Mathematics and Computation</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:6pt; color:#ffffff;\"> </span><span style=\" font-family:\'MS Shell Dlg 2\'; color:#ffffff;\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:24pt; font-weight:600; color:#ffffff;\">Profession :</span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:24pt; color:#ffffff;\"> Computer Science</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:6pt; color:#ffffff;\"> </span><span style=\" font-family:\'MS Shell Dlg 2\'; color:#ffffff;\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:24pt; font-weight:600; color:#ffffff;\">Course :</span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:24pt; color:#ffffff;\"> Optimitation Models II</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:6pt; color:#ffffff;\"> </span><span style=\" font-family:\'MS Shell Dlg 2\'; color:#ffffff;\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:24pt; font-weight:600; color:#ffffff;\">Date :</span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:24pt; color:#ffffff;\"> 2022</span></p></body></html>"))
        self.label.setText(_translate("AboutAuthors", "<html><head/><body><p align=\"center\">About Authors</p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AboutAuthors = QtWidgets.QDialog()
    ui = Ui_AboutAuthors()
    ui.setupUi(AboutAuthors)
    AboutAuthors.show()
    sys.exit(app.exec_())
