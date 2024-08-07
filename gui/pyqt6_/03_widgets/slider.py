import sys

from PyQt6.QtWidgets import QApplication, QMainWindow, QSlider


def main(args):
    app = QApplication(args)
    window = MainWindow()
    window.show()
    app.exec()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('QSlider')
        self.widget = self._init_widget()
        self.setCentralWidget(self.widget)

    def _init_widget(self):
        widget = QSlider()
        widget.setRange(-10, 3)  # .setMinimum()/.setMaximum()
        widget.valueChanged.connect(self._value_changed)
        widget.sliderMoved.connect(self._slider_moved)
        widget.sliderPressed.connect(self._slider_pressed)
        widget.sliderReleased.connect(self._slider_released)
        return widget

    def _value_changed(self, i):
        print('Value:', i)

    def _slider_moved(self, p):
        print('Slider position:', p)

    def _slider_pressed(self):
        print('Pressed')

    def _slider_released(self):
        print('...and relased')
        
    

if __name__ == '__main__':
    main(sys.argv)
