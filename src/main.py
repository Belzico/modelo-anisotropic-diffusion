import qdarkstyle

from PyForm.present import Present
from PyQt5.QtWidgets import QApplication
from PyForm.main_window import MainWindow
from matplotlib.pyplot import switch_backend 

if __name__ == '__main__':
    
    app = QApplication([])

    present = Present()
    present.exec()

    app.setStyleSheet(qdarkstyle.load_stylesheet(qt_api='pyqt5'))
    switch_backend('agg')

    gui = MainWindow()
    gui.show()

    app.exec_()