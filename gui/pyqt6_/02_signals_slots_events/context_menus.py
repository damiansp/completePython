import sys

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import (
    QApplication, #QLabel,
    QMainWindow, QMenu)


def main(args):
    app = QApplication(args)
    window = MainWindow()
    window.show()
    app.exec()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.show()
        self.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.customContextMenuRequested.connect(self.on_context_menu)

    def on_context_menu(self, pos):
        context = QMenu(self)
        context.addAction(QAction('test1', self))
        context.addAction(QAction('test2', self))
        context.addAction(QAction('test3', self))
        context.exec(self.mapToGlobal(pos))
        

if __name__ == '__main__':
    main(sys.argv)
