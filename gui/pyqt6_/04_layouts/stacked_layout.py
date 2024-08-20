import sys

from PyQt6.QtWidgets import QApplication, QMainWindow, QStackedLayout, QWidget

from layout_colorwidget import Color


def main(args):
    app = QApplication(args)
    window = MainWindow()
    window.show()
    app.exec()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Stacked Layout')
        layout = self._add_layout()
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def _add_layout(self):
        layout = QStackedLayout()
        layout.addWidget(Color('red'))
        layout.addWidget(Color('green'))
        layout.addWidget(Color('blue'))
        layout.addWidget(Color('yellow'))
        layout.setCurrentIndex(3)
        return layout
        

if __name__ == '__main__':
    main(sys.argv)
