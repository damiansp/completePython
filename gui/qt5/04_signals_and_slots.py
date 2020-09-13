#! /usr/bin/env python3
import sys

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (
    QApplication, QComboBox, QDialog, QPushButton, QVBoxLayout)


class Dialog(QDialog):
    def __init__(self):
        super(Dialog, self).__init__()
        mainLayout = QVBoxLayout()
        button = QPushButton('Click Me')
        button.clicked.connect(self.slot_method)
        mainLayout.addWidget(button)
        self.setLayout(mainLayout)
        self.setWindowTitle('Button Clicker')
    
    def slot_method(self):
        print('slot method called')
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialog = Dialog()
    sys.exit(dialog.exec_())
