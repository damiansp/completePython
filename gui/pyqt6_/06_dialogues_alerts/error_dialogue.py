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
        button = QMessageBox.critical(
            self,
            'ERROR',
            'I am explode!',
            buttons=(
                QMessageBox.StandardButton.Discard
                | QMessageBox.StandardButton.NoToAll
                | QMessageBox.StandardButton.Ignore))
        if button == QMessageBox.StandardButton.Discard:
            print('Discarding...')
        elif button == QMessageBox.StandardButton.NoToAll:
            print('No, no, and no again')
        else:
            print('Do nuffin')


if __name__ == '__main__':
    main(sys.argv)
        
