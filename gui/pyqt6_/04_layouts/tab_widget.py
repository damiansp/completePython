import sys

from PyQt6.QtWidgets import QApplication, QMainWindow, QTabWidget

from layout_colorwidget import Color


def main(args):
    app = QApplication(args)
    window = MainWindow()
    window.show()
    app.exec()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Tab Widget')
        tabs = self._make_tabs()
        self.setCentralWidget(tabs)

    def _make_tabs(self):
        tabs = QTabWidget()
        tabs.setDocumentMode(True)
        tabs.setTabPosition(QTabWidget.TabPosition.West)
        tabs.setMovable(True)
        for color in ['red', 'green', 'blue', 'yellow']:
            tabs.addTab(Color(color), color)
        return tabs
    

if __name__ == '__main__':
    main(sys.argv)
