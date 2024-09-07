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
        self.x = AnotherWindow()
        widget = self._get_widget()
        self.setCentralWidget(widget)

    def _get_widget(self):
        layout = QVBoxLayout()
        b = self._get_button(1)
        layout.addWidget(b)
        c = self._get_button(2)
        layout.addWidget(c)
        widget = QWidget()
        widget.setLayout(layout)
        return widget
        
    def _get_button(self, n):
        button = QPushButton(f'Click for window {n}')
        f = {1: self._toggle_window1, 2: self._toggle_window2}[n]
        button.clicked.connect(f)
        return button

    def _toggle_window1(self, checked):
        if self.w.isVisible():
            self.w.hide()
        else:
            self.x.show()

    def _toggle_window2(self, checked):
        if self.x.isVisible():
            self.x.hide()
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
