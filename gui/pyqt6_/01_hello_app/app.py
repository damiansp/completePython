import sys

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import (
    QApplication as QApp, QMainWindow, QPushButton, QWidget)


WINDOW_DIMS = (400, 300)


def main(args):
    app = QApp(args)
    window = MainWindow()
    window.show()
    app.exec()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Basic App')
        button = QPushButton('Click Me!')
        self.setFixedSize(QSize(*WINDOW_DIMS))
        self.setCentralWidget(button)
    

if __name__ == '__main__':
    main(sys.argv)

