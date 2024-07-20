import sys

from PyQt6.QtWidgets import (
    QApplication, QLabel, QLineEdit, QMainWindow, QVBoxLayout, QWidget)


def main(args):
    app = QApplication(args)
    window = MainWindow()
    window.show()
    app.exec()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Connect Widgets')
        self.label = QLabel()
        self.input = self._init_input()
        self.layout = self._init_layout()
        self.container = self._init_container()
        self.setCentralWidget(self.container)

    def _init_input(self):
        inp = QLineEdit()
        inp.textChanged.connect(self.label.setText)
        return inp

    def _init_layout(self):
        layout = QVBoxLayout()
        layout.addWidget(self.input)
        layout.addWidget(self.label)
        return layout

    def _init_container(self):
        container = QWidget()
        container.setLayout(self.layout)
        return container

if __name__ == '__main__':
    main(sys.argv)
