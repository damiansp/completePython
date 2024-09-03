from random import randint
import sys

from PyQt6.QtWidgets import (
    QApplication, QLabel, QMainWindow, QPushButton, QVBoxLayout, QWidget)


def main(args):
    app = QApplication(args)
    w = MainWindow()
    w.show()
    app.exec()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.w = AnotherWindow()
        self.button = QPushButton('Click for other window')
        self.button.clicked.connect(self._toggle_window)
        self.setCentralWidget(self.button)

    def _toggle_window(self, checked):
        if self.w.isVisible():
            self.w.hide()
        else:
            self.w.show()


class AnotherWindow(QWidget):
    '''This window is a QWidget. If it has no parent, it will appear as a free-
    floating window, as desired here
    '''
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.label = QLabel(f'Another Window: {randint(0, 100)}')
        layout.addWidget(self.label)
        self.setLayout(layout)

        
if __name__ == '__main__':
    main(sys.argv)
