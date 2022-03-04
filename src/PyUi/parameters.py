# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './UiForm/parameters.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(667, 297)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./UiForm/../../icons/python.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(420, 250, 171, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(70, 40, 71, 30))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(370, 70, 91, 30))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(70, 100, 81, 30))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(400, 120, 61, 30))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.sigmaSpin = QtWidgets.QSpinBox(Dialog)
        self.sigmaSpin.setGeometry(QtCore.QRect(170, 40, 41, 30))
        self.sigmaSpin.setMaximum(10)
        self.sigmaSpin.setProperty("value", 1)
        self.sigmaSpin.setObjectName("sigmaSpin")
        self.iterationSpin = QtWidgets.QSpinBox(Dialog)
        self.iterationSpin.setGeometry(QtCore.QRect(490, 20, 48, 30))
        self.iterationSpin.setMinimum(1)
        self.iterationSpin.setMaximum(100)
        self.iterationSpin.setSingleStep(1)
        self.iterationSpin.setProperty("value", 4)
        self.iterationSpin.setObjectName("iterationSpin")
        self.updbSpin = QtWidgets.QDoubleSpinBox(Dialog)
        self.updbSpin.setGeometry(QtCore.QRect(170, 100, 91, 30))
        self.updbSpin.setDecimals(5)
        self.updbSpin.setProperty("value", 0.1765)
        self.updbSpin.setObjectName("updbSpin")
        self.updfSpin = QtWidgets.QDoubleSpinBox(Dialog)
        self.updfSpin.setGeometry(QtCore.QRect(490, 120, 81, 30))
        self.updfSpin.setDecimals(5)
        self.updfSpin.setProperty("value", 0.0179)
        self.updfSpin.setObjectName("updfSpin")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(20, 160, 121, 30))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.edgeBox = QtWidgets.QComboBox(Dialog)
        self.edgeBox.setGeometry(QtCore.QRect(170, 160, 101, 30))
        self.edgeBox.setObjectName("edgeBox")
        self.edgeBox.addItem("")
        self.edgeBox.addItem("")
        self.edgeBox.addItem("")
        self.edgeBox.addItem("")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(370, 20, 101, 30))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.clusterSpin = QtWidgets.QSpinBox(Dialog)
        self.clusterSpin.setGeometry(QtCore.QRect(490, 70, 48, 30))
        self.clusterSpin.setMinimum(1)
        self.clusterSpin.setMaximum(100)
        self.clusterSpin.setProperty("value", 8)
        self.clusterSpin.setObjectName("clusterSpin")
        self.coeffBox = QtWidgets.QComboBox(Dialog)
        self.coeffBox.setGeometry(QtCore.QRect(490, 180, 171, 30))
        self.coeffBox.setObjectName("coeffBox")
        self.coeffBox.addItem("")
        self.coeffBox.addItem("")
        self.coeffBox.addItem("")
        self.coeffBox.addItem("")
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(300, 180, 171, 30))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Parameters"))
        self.label.setText(_translate("Dialog", "Sigma"))
        self.label_2.setText(_translate("Dialog", "Clusters"))
        self.label_3.setText(_translate("Dialog", "UPDB"))
        self.label_4.setText(_translate("Dialog", "UPDF"))
        self.label_6.setText(_translate("Dialog", "Edges Type"))
        self.edgeBox.setItemText(0, _translate("Dialog", "Scharr"))
        self.edgeBox.setItemText(1, _translate("Dialog", "Canny"))
        self.edgeBox.setItemText(2, _translate("Dialog", "Sobel"))
        self.edgeBox.setItemText(3, _translate("Dialog", "Laplace"))
        self.label_7.setText(_translate("Dialog", "Iteration"))
        self.coeffBox.setItemText(0, _translate("Dialog", "Perona and Malik II"))
        self.coeffBox.setItemText(1, _translate("Dialog", "Perona and Malik I"))
        self.coeffBox.setItemText(2, _translate("Dialog", "Weickert"))
        self.coeffBox.setItemText(3, _translate("Dialog", "Charbonnier"))
        self.label_8.setText(_translate("Dialog", "Coefficient Type"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
