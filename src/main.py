from PyQt5.QtWidgets import QApplication
from PyForm.main_window import MainWindow
from matplotlib.pyplot import switch_backend 

import qdarkstyle

if __name__ == '__main__':
    app = QApplication([])
    app.setStyleSheet(qdarkstyle.load_stylesheet(qt_api='pyqt5'))
    switch_backend('agg')

    gui = MainWindow()
    gui.show()

    app.exec_()