#! /usr/bin/env python3
import sys

from PyQt5.QtWidgets import QApplication, QLineEdit, QLabel, QMainWindow


class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'Absolute Postioning!'
        self.left = 10
        self.top = 10
        self.width = 320
        self.height = 240
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        label = QLabel('Python', self)
        label.move(50, 50)
        lab2 = QLabel('PyQt5', self)
        lab2.move(100, 100)
        lab3 = QLabel('Examples', self)
        lab3.move(150, 150)
        lab4 = QLabel('Oh Boy!', self)
        lab4.move(200, 200)
        self.show()
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
