import sys

from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton


def main(args):
    app = QApplication(args)
    window = MainWindow()
    window.show()
    app.exec()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Signals, Slots, and Events')
        self.button = self._add_button()

    def _add_button(self):
        button = QPushButton('Click Me!')
        button.setCheckable(True)
        button.clicked.connect(self.click_button)
        self.setCentralWidget(button)
        return button

    def click_button(self):
        self.button.setText('Activated!')
        self.button.setEnabled(False)
        self.setWindowTitle('Game Over!')
    

if __name__ == '__main__':
    main(sys.argv)
