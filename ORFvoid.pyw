# -*- coding: utf-8 -*-

import sys, os
from ui_ORFvoid import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        
        self.setupUi(self)


def main():
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    app.exec_()

if __name__ == '__main__':
    sys.exit(main())
