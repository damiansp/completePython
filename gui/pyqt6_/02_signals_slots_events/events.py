import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QLabel, QMainWindow


def main(args):
    app = QApplication(args)
    window = MainWindow()
    window.show()
    app.exec()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.label = QLabel('Click in this window')
        self.setCentralWidget(self.label)

    def mouseMoveEvent(self, e):
        self.label.setText('Mouse move')

    def mousePressEvent(self, e):
        match e.button():
            case Qt.MouseButton.LeftButton:
                self.label.setText('LEFT Button')
            case Qt.MouseButton.MiddleButton:
                self.label.setText('Middle Button')
            case Qt.MouseButton.RightButton:
                self.label.setText('Right Button')

    def mouseReleaseEvent(self, e):
        self.label.setText('Mouse release')

    def mouseDoubleClickEvent(self, e):
        self.label.setText('Mouse double click')


if __name__ == '__main__':
    main(sys.argv)
