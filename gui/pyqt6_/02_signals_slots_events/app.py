import sys

from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton


def main(args):
    app = QApplication(args)
    window = MainWindow()
    window.show()
    app.exec()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Signals, Slots, and Events')
        self._add_button()
        self.n_clicks = 0
        self.button_is_checked = False

    def _add_button(self):
        button = QPushButton('Click Me!')
        button.setCheckable(True)
        button.clicked.connect(self.click_button)
        button.clicked.connect(self.toggle_button)
        button.released.connect(self.button_released)
        self.setCentralWidget(button)

    def click_button(self):
        self.n_clicks += 1
        print(f'Clicked {self.n_clicks} times')

    def toggle_button(self, checked):
        self.button_is_checked = checked
        print('  Checked:', checked)
        
    def button_released(self):
        print(f'  Button released.  Checked: {self.button_is_checked}')
        
    

if __name__ == '__main__':
    main(sys.argv)
