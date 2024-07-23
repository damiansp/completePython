import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QCheckBox, QMainWindow

IMG = '../img'


def main(args):
    app = QApplication(args)
    window = MainWindow()
    window.show()
    app.exec()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('QCheckbox')
        widget = self._make_checkbox()
        self.setCentralWidget(widget)

    def _make_checkbox(self):
        widget = QCheckBox()
        widget.setCheckState(Qt.CheckState.Checked)
        widget.stateChanged.connect(self._show_state)
        return widget

    def _show_state(self, s):
        print(s)
        print(s == Qt.CheckState.Checked.value)
        

if __name__ == '__main__':
    main(sys.argv)
