#! /usr/bin/env python3
import sys

#from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import (
    QApplication,  QDialog, QGridLayout, QGroupBox, QPushButton, QVBoxLayout)


class App(QDialog):
    def __init__(self):
        super().__init__()
        self.title = 'Grid Layouts!'
        self.left = 10
        self.top = 10
        self.width = 320
        self.height = 100
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.create_grid_layout()
        window_layout = QVBoxLayout()
        window_layout.addWidget(self.horizontal_group_box)
        self.setLayout(window_layout)
        self.show()

    def create_grid_layout(self):
        self.horizontal_group_box = QGroupBox('Grid')
        layout = QGridLayout()
        layout.setColumnStretch(1, 2) # change width of col at idx 1
        layout.setColumnStretch(2, 4)
        for i in range(3):
            for j in range(3):
                layout.addWidget(QPushButton(str(3*i + j + 1)), i, j)
        self.horizontal_group_box.setLayout(layout)
        
                
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
