import sys

from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QAction, QIcon
from PyQt6.QtWidgets import (
    QApplication, QCheckBox, QLabel, QMainWindow, QStatusBar, QToolBar)


def main(args):
    app = QApplication(args)
    w = MainWindow()
    w.show()
    app.exec()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Menus')
        label = self._add_label()
        self.setCentralWidget(label)
        self._add_toolbar()
        self.button = None  # made in _add_toolbar
        self.setStatusBar(QStatusBar(self))
        menu = self._add_menu()
        
    def _add_label(self):
        lab = QLabel('Howdy!')
        lab.setAlignment(Qt.AlignmentFlag.AlignCenter)
        return lab

    def _add_toolbar(self):
        toolbar = QToolBar('Main toolbar')
        toolbar.setIconSize(QSize(16, 16))
        self.addToolBar(toolbar)
        button = self._make_toolbar_button('&Your button', 'I am your button')
        self.button = button
        toolbar.addAction(button)
        toolbar.addSeparator()
        button2 = self._make_toolbar_button(
            'Your &button2', 'I am your button, too')
        toolbar.addAction(button2)
        toolbar.addWidget(QLabel('Hi there!'))
        toolbar.addWidget(QCheckBox())

    def _make_toolbar_button(self, txt, tip):
        button = QAction(QIcon('bug.png'), txt, self)
        button.setStatusTip(tip)
        button.triggered.connect(self.on_toolbar_button_click)
        button.setCheckable(True)
        return button

    def on_toolbar_button_click(self, s):
        print('click', s)

    def _add_menu(self):
        menu = self.menuBar()
        file_menu = menu.addMenu('&File')
        file_menu.add_action(self.button)
        return menu
        

if __name__ == '__main__':
    main(sys.argv)
