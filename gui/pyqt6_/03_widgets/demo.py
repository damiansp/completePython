import sys

#from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QApplication, QCheckBox, QComboBox, QDateEdit, QDateTimeEdit, QDial,
    QDoubleSpinBox, QFontComboBox, QLabel, QLCDNumber, QLineEdit, QMainWindow,
    QProgressBar, QPushButton, QRadioButton, QSlider, QSpinBox, QTimeEdit,
    QVBoxLayout, QWidget)


def main(args):
    app = QApplication(args)
    window = MainWindow()
    window.show()
    app.exec()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Widget Demo')
        self.widget = self._init_widget()
        self.setCentralWidget(self.widget)

    def _init_widget(self):
        layout = QVBoxLayout()
        widgets = [
            QCheckBox, QComboBox, QDateEdit, QDateTimeEdit, QDial,
            QDoubleSpinBox, QFontComboBox, QLabel, QLCDNumber, QLineEdit,
            QProgressBar, QPushButton, QRadioButton, QSlider, QSpinBox,
            QTimeEdit]
        for w in widgets:
            layout.addWidget(w())
        widget = QWidget()
        widget.setLayout(layout)
        return widget
    

if __name__ == '__main__':
    main(sys.argv)
