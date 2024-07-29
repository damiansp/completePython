import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QApplication, QListWidget, QListWidgetItem, QMainWindow)


def main(args):
    app = QApplication(args)
    window = MainWindow()
    window.show()
    app.exec()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('QListWidget')
        widget = self._make_list_widget()
        self.setCentralWidget(widget)

    def _make_list_widget(self):
        widget = QListWidget()
        widget.addItems(['Aon', 'Da', 'Tri'])
        widget.currentItemChanged.connect(self._index_changed)
        widget.currentTextChanged.connect(self._value_changed)
        return widget

    def _index_changed(self, i: QListWidgetItem):
        print(i.text())

    def _value_changed(self, v: str):
        print(v)
        

if __name__ == '__main__':
    main(sys.argv)
