import sys

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QApplication, QLabel, QMainWindow

IMG = '../img'


def main(args):
    app = QApplication(args)
    window = MainWindow()
    window.show()
    app.exec()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('QLabel')
        widget = self._make_label()
        self.setCentralWidget(widget)

    def _make_label(self):
        widget = QLabel('Hello')
        font = widget.font()
        font.setPointSize(30)
        widget.setFont(font)
        widget.setAlignment(
            Qt.AlignmentFlag.AlignCenter | Qt.AlignmentFlag.AlignVCenter)
        # widget.setPixmap(QPixmap(f'{IMG}/otje.jpg'))
        # widget.setScaledContents(True)  # make fit window dims
        return widget
    

if __name__ == '__main__':
    main(sys.argv)
