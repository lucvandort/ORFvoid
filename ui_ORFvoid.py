# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\ORFvoid.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(609, 132)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.jpgfolder_select = QtWidgets.QPushButton(self.centralwidget)
        self.jpgfolder_select.setObjectName("jpgfolder_select")
        self.gridLayout.addWidget(self.jpgfolder_select, 0, 2, 1, 1)
        self.jpgfolder_label = QtWidgets.QLabel(self.centralwidget)
        self.jpgfolder_label.setObjectName("jpgfolder_label")
        self.gridLayout.addWidget(self.jpgfolder_label, 0, 0, 1, 1)
        self.jpgfolder = QtWidgets.QLineEdit(self.centralwidget)
        self.jpgfolder.setObjectName("jpgfolder")
        self.gridLayout.addWidget(self.jpgfolder, 0, 1, 1, 1)
        self.orffolder = QtWidgets.QLineEdit(self.centralwidget)
        self.orffolder.setObjectName("orffolder")
        self.gridLayout.addWidget(self.orffolder, 1, 1, 1, 1)
        self.orffolder_label = QtWidgets.QLabel(self.centralwidget)
        self.orffolder_label.setObjectName("orffolder_label")
        self.gridLayout.addWidget(self.orffolder_label, 1, 0, 1, 1)
        self.orffolder_select = QtWidgets.QPushButton(self.centralwidget)
        self.orffolder_select.setObjectName("orffolder_select")
        self.gridLayout.addWidget(self.orffolder_select, 1, 2, 1, 1)
        self.voidfolder_select = QtWidgets.QPushButton(self.centralwidget)
        self.voidfolder_select.setObjectName("voidfolder_select")
        self.gridLayout.addWidget(self.voidfolder_select, 2, 2, 1, 1)
        self.voidfolder = QtWidgets.QLineEdit(self.centralwidget)
        self.voidfolder.setObjectName("voidfolder")
        self.gridLayout.addWidget(self.voidfolder, 2, 1, 1, 1)
        self.voidfolder_label = QtWidgets.QLabel(self.centralwidget)
        self.voidfolder_label.setObjectName("voidfolder_label")
        self.gridLayout.addWidget(self.voidfolder_label, 2, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.matchbutton = QtWidgets.QPushButton(self.centralwidget)
        self.matchbutton.setObjectName("matchbutton")
        self.horizontalLayout.addWidget(self.matchbutton)
        self.voidbutton = QtWidgets.QPushButton(self.centralwidget)
        self.voidbutton.setObjectName("voidbutton")
        self.horizontalLayout.addWidget(self.voidbutton)
        self.quitbutton = QtWidgets.QPushButton(self.centralwidget)
        self.quitbutton.setObjectName("quitbutton")
        self.horizontalLayout.addWidget(self.quitbutton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ORFvoid"))
        self.jpgfolder_select.setText(_translate("MainWindow", "Select"))
        self.jpgfolder_label.setText(_translate("MainWindow", "JPG folder:"))
        self.orffolder_label.setText(_translate("MainWindow", "ORF folder:"))
        self.orffolder_select.setText(_translate("MainWindow", "Select"))
        self.voidfolder_select.setText(_translate("MainWindow", "Select"))
        self.voidfolder_label.setText(_translate("MainWindow", "Void folder:"))
        self.matchbutton.setText(_translate("MainWindow", "Match JPG <-> ORF"))
        self.voidbutton.setText(_translate("MainWindow", "Void unmatched ORF"))
        self.quitbutton.setText(_translate("MainWindow", "Quit"))

