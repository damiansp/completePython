import sys

from PyQt6.QtWidgets import QApplication, QComboBox, QMainWindow

IMG = '../img'


def main(args):
    app = QApplication(args)
    window = MainWindow()
    window.show()
    app.exec()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('QComboBox')
        widget = self._make_combobox()
        self.setCentralWidget(widget)

    def _make_combobox(self):
        widget = QComboBox()
        widget.addItems(['Uno', 'Dos', 'Tres'])
        widget.currentIndexChanged.connect(self._index_changed)
        widget.currentTextChanged.connect(self._text_changed)
        return widget

    def _index_changed(self, i: int):
        print(i)

    def _text_changed(self, s: str):
        print(s)
        

if __name__ == '__main__':
    main(sys.argv)
