#! /usr/bin/env python3
import sys

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import (
    QApplication, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)


class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'Tables!'
        self.left = 0
        self.top = 0
        self.width = 300
        self.height = 200
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.create_table()
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.tableWidget)
        self.setLayout(self.layout)
        self.show()

    def create_table(self):
        N_ROWS = 4
        N_COLS = 2
        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(N_ROWS)
        self.tableWidget.setColumnCount(N_COLS)
        for r in range(N_ROWS):
            for c in range(N_COLS):
                self.tableWidget.setItem(
                    r, c, QTableWidgetItem(f'Cell ({r + 1}, {c + 1})'))
        self.tableWidget.move(0, 0)
        self.tableWidget.doubleClicked.connect(self.on_click)

    @pyqtSlot()
    def on_click(self):
        print()
        for table_widget_item in self.tableWidget.selectedItems():
            print(table_widget_item.row(),
                  table_widget_item.column(),
                  table_widget_item.text())
            

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
