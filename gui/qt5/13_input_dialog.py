#! /usr/bin/env python3
import sys

from PyQt5.QtWidgets import QApplication, QInputDialog, QLineEdit, QWidget


class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'Input Dialogues!'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.get_int()
        self.get_text()
        self.get_float()
        self.get_choice()
        self.show()

    def get_int(self):
        i, ok_pressed = QInputDialog.getInt(
            self, 'Get integer', 'Percentage:', 28, 0, 100, 1)
        if ok_pressed:
            print(i)

    def get_float(self):
        d, ok_pressed = QInputDialog.getDouble(
            self, 'Get double', 'Value:', 10.5, 0, 100, 1)
        if ok_pressed:
            print(d)

    def get_choice(self):
        items = ('Red', 'Blue', 'Green')
        item, ok_pressed = QInputDialog.getItem(
            self, 'Get item', 'Color:', items, 0, False)
        if ok_pressed:
            print(item)

    def get_text(self):
        text, ok_pressed = QInputDialog.getText(
            self, 'Get text', 'Your Name:', QLineEdit.Normal, '')
        if ok_pressed and text != '':
            print(text)
                
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
