#! /usr/bin/env python3
import sys

from PyQt5.QtWidgets import QApplication, QFileDialog, QWidget


class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'File Dialogues!'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.open_file_name_dialog()
        self.open_file_names_dialog()
        self.save_file_dialog()
        self.show()
    
    def _open_qfile_dialog(self, cmd, ext):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file_type = 'Python' if ext == 'py' else 'Text'
        f, _ = cmd(self,
                   str(cmd.__name__),
                   '',
                   f'All Files (*);;{file_type} Files (*.{ext})')
        if f:
            print(f)

    def open_file_name_dialog(self):
        self._open_qfile_dialog(QFileDialog.getOpenFileName, 'py')

    def open_file_names_dialog(self):
        self._open_qfile_dialog(QFileDialog.getOpenFileNames, 'py')
        
    def save_file_dialog(self):
        self._open_qfile_dialog(QFileDialog.getSaveFileName, 'txt')

                
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
