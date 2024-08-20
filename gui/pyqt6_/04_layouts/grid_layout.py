import sys

from PyQt6.QtWidgets import QApplication, QGridLayout, QMainWindow, QWidget

from layout_colorwidget import Color


def main(args):
    app = QApplication(args)
    window = MainWindow()
    window.show()
    app.exec()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Grid Layout')
        layout = self._add_layout()
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def _add_layout(self):
        layout = QGridLayout()
        layout.addWidget(Color('red'), 0, 0)
        layout.addWidget(Color('green'), 1, 0)
        layout.addWidget(Color('blue'), 1, 1)
        layout.addWidget(Color('purple'), 2, 1)
        return layout
        

if __name__ == '__main__':
    main(sys.argv)
