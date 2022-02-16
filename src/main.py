from PyQt5.QtWidgets import QApplication
from PyForm.main_window import MainWindow
from matplotlib.pyplot import switch_backend 

if __name__ == '__main__':
    app = QApplication([])
    switch_backend('agg')

    gui = MainWindow()
    gui.show()

    app.exec_()
    