#! /usr/bin/env python3
import sys

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import (
    QApplication, QDialog, QGroupBox, QHBoxLayout, QPushButton, QVBoxLayout)

class App(QDialog):
    def __init__(self):
        super().__init__()
        self.title = 'Horizontal Layouts!'
        self.left = 10
        self.top = 10
        self.width = 320
        self.height = 100
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.create_horizontal_layout()
        window_layout = QVBoxLayout()
        window_layout.addWidget(self.horizontal_group_box)
        self.setLayout(window_layout)
        self.show()

    def create_horizontal_layout(self):
        self.horizontal_group_box = QGroupBox('What Color?')
        layout = QHBoxLayout()
        button_blue = QPushButton('Blue', self)
        button_blue.clicked.connect(self.on_click)
        layout.addWidget(button_blue)
        button_red = QPushButton('Red', self)
        button_red.clicked.connect(self.on_click)
        layout.addWidget(button_red)
        button_green = QPushButton('Green', self)
        button_green.clicked.connect(self.on_click)
        layout.addWidget(button_green)
        self.horizontal_group_box.setLayout(layout)

    @pyqtSlot()
    def on_click(self):
        print('Button pushed')
        
                
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
