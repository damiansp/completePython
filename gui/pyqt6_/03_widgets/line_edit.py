import sys

#from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QLineEdit, QMainWindow


def main(args):
    app = QApplication(args)
    window = MainWindow()
    window.show()
    app.exec()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('LineEdit')
        self.widget = self._init_widget()
        self.setCentralWidget(self.widget)

    def _init_widget(self):
        widget = QLineEdit()
        widget.setMaxLength(10)
        widget.setPlaceholderText('Enter your text')
        #widget.setReadOnly(True)
        widget.returnPressed.connect(self._return_pressed)
        widget.selectionChanged.connect(self._selection_changed)
        widget.textChanged.connect(self._text_changed)
        widget.textEdited.connect(self._text_edited)
        return widget

    def _return_pressed(self):
        print('Returned')
        self.centralWidget().setText('Boom!')

    def _selection_changed(self):
        print('Selection changed')
        print(self.centralWidget().selectedText())

    def _text_changed(self, s):
        print('Text changed')
        print(s)

    def _text_edited(self, s):
        print('Text edited')
        print(s)
    

if __name__ == '__main__':
    main(sys.argv)
