#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
ZetCode PyQt5 tutorial

This example shows a tooltip on
a window and a button.

Author: Jan Bodnar
Website: zetcode.com
Last edited: August 2017
"""

import sys
from PyQt5.QtWidgets import (QWidget, QToolTip,
    QPushButton, QApplication)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QListWidget, QListWidgetItem, QLabel, QApplication, QDialog

class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        QToolTip.setFont(QFont('SansSerif', 10))

        self.setToolTip('This is a <b>QWidget</b> widget')

        btn = QPushButton('Button', self)
        btn.setToolTip('This is a <b>QPushButton</b> widget')
        btn.resize(btn.sizeHint())
        btn.move(250, 250)
        btn.clicked.connect(self.buildExamplePopup)

        listWidget = QListWidget(self)
        listWidget.itemDoubleClicked.connect(self.buildExamplePopupz)
        for n in ["Jack", "Chris", "Joey", "Kim", "Duncan"]:
            QListWidgetItem(n, listWidget)
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Tooltips')
        self.show()

    @pyqtSlot()
    def buildExamplePopup(self):
        name = "aaaa"#item.text()
        self.exPopup = examplePopup(name)
        self.exPopup.setGeometry(100, 200, 100, 100)
        self.exPopup.show()

        

    @pyqtSlot(QListWidgetItem)
    def buildExamplePopupz(self, item):
        exPopup = ExamplePopup(item.text(), self)
        exPopup.setGeometry(100, 200, 100, 100)
        exPopup.show()

    @pyqtSlot()
    def on_click(self):
        print('PyQt5 button click')

class ExamplePopup(QDialog):

    def __init__(self, name, parent=None):
        super().__init__(parent)
        self.name = name
        self.label = QLabel(self.name, self)

class examplePopup(QWidget):

    def __init__(self, name):
        super().__init__()

        self.name = name

        self.initUI()

    def initUI(self):
        lblName = QLabel(self.name, self)

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
