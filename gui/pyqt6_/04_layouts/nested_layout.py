import sys

from PyQt6.QtGui import QColor, QPalette
from PyQt6.QtWidgets import (
    QApplication, QHBoxLayout, QMainWindow, QVBoxLayout, QWidget)


def main(args):
    app = QApplication(args)
    window = MainWindow()
    window.show()
    app.exec()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Horizontal Layout')
        layout = self._add_layout()
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def _add_layout(self):
        layout1 = QHBoxLayout()
        layout2 = self._add_layout2()
        layout1.addLayout(layout2)
        layout1.addWidget(Color('green'))
        layout3 = self._add_layout3()
        layout1.addLayout(layout3)
        #layout1.setContentsMargins(0, 0, 0, 0)
        layout1.setSpacing(20)
        return layout1

    def _add_layout2(self):
        layout2 = QVBoxLayout()
        layout2.addWidget(Color('red'))
        layout2.addWidget(Color('yellow'))
        layout2.addWidget(Color('purple'))
        return layout2

    def _add_layout3(self):
        layout3 = QVBoxLayout()
        layout3.addWidget(Color('red'))
        layout3.addWidget(Color('purple'))
        return layout3


class Color(QWidget):
    def __init__(self, color):
        super().__init__()
        self.setAutoFillBackground(True)
        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor(color))
        self.setPalette(palette)
        

if __name__ == '__main__':
    main(sys.argv)
