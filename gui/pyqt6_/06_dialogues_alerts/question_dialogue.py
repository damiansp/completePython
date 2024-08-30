import sys

from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox, QPushButton


def main(args):
    app = QApplication(args)
    window = MainWindow()
    window.show()
    app.exec()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Message Dialogues')
        self.button = QPushButton('For a good time, click here')
        self.button.clicked.connect(self._click)
        self.setCentralWidget(self.button)

    def _click(self, s):
        dlg = QMessageBox(self)
        dlg.setWindowTitle('I have a question')
        dlg.setText('A question dialogue')
        dlg.setStandardButtons(
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        dlg.setIcon(QMessageBox.Icon.Question)
        self.button = dlg.exec()
        if self.button == QMessageBox.StandardButton.Yes:
            print('Yes, you got it!')
        else:
            print('No way, Jose!')


if __name__ == '__main__':
    main(sys.argv)
        
