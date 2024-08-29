import sys

from PyQt6.QtWidgets import (
    QApplication, QDialog, QDialogButtonBox, QLabel, QMainWindow, QPushButton,
    QVBoxLayout)


def main(args):
    app = QApplication(args)
    window = MainWindow()
    window.show()
    app.exec()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Dialogues')
        button = self._get_button()
        self.setCentralWidget(button)

    def _get_button(self):
        button = QPushButton('Click for dialogue!')
        button.clicked.connect(self._click_button)
        return button

    def _click_button(self, s):
        print('Click', s)
        dlg = Dialogue()
        if dlg.exec():
            print('Success!')
        else:
            print('Cancel!')


class Dialogue(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Well, hi there!')
        button_box = self._get_button_box()
        layout = self._get_layout()
        layout.addWidget(button_box)
        self.setLayout(layout)

    def _get_button_box(self):
        QBtn = (
            QDialogButtonBox.StandardButton.Ok
            | QDialogButtonBox.StandardButton.Cancel)
        button_box = QDialogButtonBox(QBtn)
        button_box.accepted.connect(self.accept)
        button_box.rejected.connect(self.reject)
        return button_box

    def _get_layout(self):
        layout = QVBoxLayout()
        msg = QLabel('Something happened, ok?')
        layout.addWidget(msg)
        return layout


if __name__ == '__main__':
    main(sys.argv)

    
