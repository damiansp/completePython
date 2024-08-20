import sys

#from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QApplication, QHBoxLayout, #QLabel,
    QMainWindow, QPushButton,
    QStackedLayout, QVBoxLayout, QWidget)

from layout_colorwidget import Color


def main(args):
    app = QApplication(args)
    window = MainWindow()
    window.show()
    app.exec()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Tabbed Layout Demo')
        self.stack_layout = QStackedLayout()
        page_layout = self._add_page_layout()
        widget = QWidget()
        widget.setLayout(page_layout)
        self.setCentralWidget(widget)

    def _add_page_layout(self):
        page_layout = QVBoxLayout()
        button_layout = self._add_button_layout()
        page_layout.addLayout(button_layout)
        page_layout.addLayout(self.stack_layout)
        return page_layout
    
    def _add_button_layout(self):
        button_layout = QHBoxLayout()
        for color, f in zip(
                ['red', 'green', 'yellow'],
                [self._activate_tab1, self._activate_tab2, self._activate_tab3]
        ):
            btn = self._make_button(color, f)
            button_layout.addWidget(btn)
            self.stack_layout.addWidget(Color(color))
        return button_layout

    def _make_button(self, color, f):
        btn = QPushButton(color)
        btn.pressed.connect(f)
        return btn
        
    def _activate_tab1(self):
        self.stack_layout.setCurrentIndex(0)

    def _activate_tab2(self):
        self.stack_layout.setCurrentIndex(1)

    def _activate_tab3(self):
        self.stack_layout.setCurrentIndex(2)


if __name__ == '__main__':
    main(sys.argv)
