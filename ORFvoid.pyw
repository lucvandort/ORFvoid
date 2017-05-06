# -*- coding: utf-8 -*-

import sys
import os
import glob
import shutil
import errno
from ui_ORFvoid import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setupUi(self)

        self.jpgfolder_select.clicked.connect(self.jpgfolderDialog)
        self.orffolder_select.clicked.connect(self.orffolderDialog)
        self.voidfolder_select.clicked.connect(self.voidfolderDialog)

        self.matchbutton.clicked.connect(self.jpgorfmatch)
        self.voidbutton.clicked.connect(self.voidorf)
        self.quitbutton.clicked.connect(QApplication.quit)

        self.matcher = None

    def jpgfolderDialog(self):
        foldername = QFileDialog.getExistingDirectory(self,
                                                      'Select JPG folder')
        self.jpgfolder.setText(foldername)
        self.orffolder.setText(foldername)
        self.voidfolder.setText(os.path.join(foldername, "_void"))

    def orffolderDialog(self):
        foldername = QFileDialog.getExistingDirectory(self,
                                                      'Select ORF folder')
        self.orffolder.setText(foldername)

    def voidfolderDialog(self):
        foldername = QFileDialog.getExistingDirectory(self,
                                                      'Select ORF folder')
        self.voidfolder.setText(foldername)

    def jpgorfmatch(self):
        self.matcher = Matcher(
            jpgfolder=self.jpgfolder.text(), orffolder=self.orffolder.text())
        self.matcher.match()
        self.jpgfiles.setPlainText(self.matcher.get_jpgfiles_view())
        self.orffiles.setPlainText(self.matcher.get_orffiles_view())
        self.voidfiles.setPlainText(self.matcher.get_voidfiles_view())
        self.jpgorphans.setPlainText(self.matcher.get_jpgorphans_view())

    def voidorf(self):
        if self.matcher:
            self.matcher.void(self.voidfolder.text())


class Matcher():
    def __init__(self, jpgfolder, orffolder):
        self.jpgfolder = jpgfolder
        self.orffolder = orffolder
        self.jpgfiles = []
        self.orffiles = []
        self.voidfiles = []
        self.jpgorphans = []

    def get_jpgfiles_view(self):
        return ''.join("{}.JPG\n".format(filename)
                       for filename in self.jpgfiles)

    def get_orffiles_view(self):
        return ''.join("{}.ORF\n".format(filename)
                       for filename in self.orffiles)

    def get_voidfiles_view(self):
        return ''.join("{}.ORF\n".format(filename)
                       for filename in self.voidfiles)

    def get_jpgorphans_view(self):
        return ''.join("{}.JPG\n".format(filename)
                       for filename in self.jpgorphans)

    def match(self):
        os.chdir(self.jpgfolder)
        self.jpgfiles = [filename[:-4] for filename in glob.iglob("*.JPG")]

        os.chdir(self.orffolder)
        self.orffiles = [filename[:-4] for filename in glob.iglob("*.ORF")]

        for jpgfile in self.jpgfiles:
            if jpgfile not in self.orffiles:
                self.jpgorphans.append(jpgfile)

        for orffile in self.orffiles:
            if orffile not in self.jpgfiles:
                self.voidfiles.append(orffile)

    def void(self, voidfolder):
        make_sure_path_exists(voidfolder)

        for voidfile in self.voidfiles:
            filename = "{}.ORF".format(voidfile)
            shutil.move(
                os.path.join(self.orffolder, filename),
                os.path.join(voidfolder, filename))


def make_sure_path_exists(path):
    try:
        os.makedirs(path)
    except OSError as exception:
        if exception.errno != errno.EEXIST:
            raise


def main():
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    app.exec_()


if __name__ == '__main__':
    sys.exit(main())
