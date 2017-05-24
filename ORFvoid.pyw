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
            jpgfolder=self.jpgfolder.text(),
            orffolder=self.orffolder.text(),
            jpgfolder_include_subfolders=
            self.jpgfolder_include_subfolders.isChecked(),
            orffolder_include_subfolders=
            self.orffolder_include_subfolders.isChecked())
        self.matcher.match()
        self.jpgfiles.setPlainText(self.matcher.get_jpgfiles_view())
        self.orffiles.setPlainText(self.matcher.get_orffiles_view())
        self.voidfiles.setPlainText(self.matcher.get_voidfiles_view())
        self.jpgorphans.setPlainText(self.matcher.get_jpgorphans_view())

    def voidorf(self):
        if self.matcher:
            self.matcher.void(self.voidfolder.text())


class Matcher():
    def __init__(self,
                 jpgfolder,
                 orffolder,
                 jpgfolder_include_subfolders=False,
                 orffolder_include_subfolders=False):
        self.jpgfolder = jpgfolder
        self.orffolder = orffolder
        self.jpgfolder_include_subfolders = jpgfolder_include_subfolders
        self.orffolder_include_subfolders = orffolder_include_subfolders
        self.jpgfiles = []
        self.orffiles = []
        self.voidfiles = []
        self.jpgorphans = []

    def get_files_view(self, files):
        return ''.join("{}\n".format(os.path.basename(file))
                       for file in files)

    def get_jpgfiles_view(self):
        return self.get_files_view(self.jpgfiles)

    def get_orffiles_view(self):
        return self.get_files_view(self.orffiles)

    def get_voidfiles_view(self):
        return self.get_files_view(self.voidfiles)

    def get_jpgorphans_view(self):
        return self.get_files_view(self.jpgorphans)

    def match(self):
        os.chdir(self.jpgfolder)
        if self.jpgfolder_include_subfolders:
            self.jpgfiles = glob.glob("**/*.JPG", recursive=True)
        else:
            self.jpgfiles = glob.glob("*.JPG")
        jpglist = get_filenames_from_glob(self.jpgfiles)

        os.chdir(self.orffolder)
        if self.orffolder_include_subfolders:
            self.orffiles = glob.glob("**/*.ORF", recursive=True)
        else:
            self.orffiles = glob.glob("*.ORF")
        orflist = get_filenames_from_glob(self.orffiles)

        for jpgfile in self.jpgfiles:
            if get_filename_from_path(jpgfile) not in orflist:
                self.jpgorphans.append(jpgfile)

        for orffile in self.orffiles:
            if get_filename_from_path(orffile) not in jpglist:
                self.voidfiles.append(orffile)

    def void(self, voidfolder):
        make_sure_path_exists(voidfolder)

        for voidfile in self.voidfiles:
            shutil.move(
                os.path.join(voidfile),
                os.path.join(voidfolder, os.path.basename(voidfile)))


def make_sure_path_exists(path):
    try:
        os.makedirs(path)
    except OSError as exception:
        if exception.errno != errno.EEXIST:
            raise


def get_filename_from_path(path):
    return os.path.splitext(os.path.basename(path))[0]


def get_filenames_from_glob(iglob):
    return [get_filename_from_path(path) for path in iglob]


def main():
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    app.exec_()


if __name__ == '__main__':
    sys.exit(main())
