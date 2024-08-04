import sys

#from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QDoubleSpinBox, QMainWindow, QSpinBox


def main(args):
    app = QApplication(args)
    window = MainWindow()
    window.show()
    app.exec()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('SpinBoxes')
        self.widget = self._init_widget()
        self.setCentralWidget(self.widget)

    def _init_widget(self):
        widget = QSpinBox()
        #widget = QDoubleSpinBox()
        widget.setMinimum(-9)
        widget.setMaximum(3)
        #widget.setRange(-9, 3)
        widget.setPrefix('$')
        widget.setSuffix('c')
        widget.setSingleStep(3)  # 3.0 for QDoubleSpinBox
        widget.valueChanged.connect(self._value_changed)
        widget.textChanged.connect(self._text_changed)
        return widget

    def _value_changed(self, i):
        print('i:', i)

    def _text_changed(self, s):
        print('s:', s)
    

if __name__ == '__main__':
    main(sys.argv)
