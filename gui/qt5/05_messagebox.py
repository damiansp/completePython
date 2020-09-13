#! /usr/bin/env python3
import sys

from PyQt5.QtWidgets import QApplication, QMessageBox, QWidget


class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'Message Box!'
        self.left = 10
        self.top = 10
        self.width = 320
        self.height = 240
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        button_reply = QMessageBox.question(
            self,
            'Box Header',
            'Do you like me?',
            QMessageBox.Cancel | QMessageBox.No |  QMessageBox.Yes,
            QMessageBox.Cancel)
        print (
            {
                QMessageBox.Yes: 'You like me!',
                QMessageBox.No: 'Aw, nobody likes me.',
                QMessageBox.Cancel: "Can't decide, huh?"
            }[button_reply])
                

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
