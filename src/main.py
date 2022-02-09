from PyQt5.QtWidgets import QApplication
from PyForm.main_window import MainWindow

if __name__ == '__main__':
    app = QApplication([])

    gui = MainWindow()
    gui.show()

    app.exec_()