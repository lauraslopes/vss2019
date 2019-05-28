# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(250, 650)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.startButton = QtWidgets.QPushButton(self.centralwidget)
        self.startButton.setGeometry(QtCore.QRect(0, 120, 80, 25))
        self.startButton.setObjectName("startButton")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(0, 0, 191, 122))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.l_h = QtWidgets.QSlider(self.verticalLayoutWidget)
        self.l_h.setOrientation(QtCore.Qt.Horizontal)
        self.l_h.setObjectName("l_h")
        self.l_h.setMinimum(0)
        self.l_h.setMaximum(179)
        self.l_h.valueChanged.connect(self.change)
        self.verticalLayout_2.addWidget(self.l_h)
        self.l_s = QtWidgets.QSlider(self.verticalLayoutWidget)
        self.l_s.setOrientation(QtCore.Qt.Horizontal)
        self.l_s.setObjectName("l_s")
        self.l_s.setMinimum(0)
        self.l_s.setMaximum(255)
        self.l_s.valueChanged.connect(self.change)
        self.verticalLayout_2.addWidget(self.l_s)
        self.l_v = QtWidgets.QSlider(self.verticalLayoutWidget)
        self.l_v.setOrientation(QtCore.Qt.Horizontal)
        self.l_v.setObjectName("l_v")
        self.l_v.setMinimum(0)
        self.l_v.setMaximum(255)
        self.l_v.valueChanged.connect(self.change)
        self.verticalLayout_2.addWidget(self.l_v)
        self.u_h = QtWidgets.QSlider(self.verticalLayoutWidget)
        self.u_h.setOrientation(QtCore.Qt.Horizontal)
        self.u_h.setObjectName("u_h")
        self.u_h.setMinimum(0)
        self.u_h.setMaximum(179)
        self.u_h.valueChanged.connect(self.change)
        self.verticalLayout_2.addWidget(self.u_h)
        self.u_s = QtWidgets.QSlider(self.verticalLayoutWidget)
        self.u_s.setOrientation(QtCore.Qt.Horizontal)
        self.u_s.setObjectName("u_s")
        self.u_s.setMinimum(0)
        self.u_s.setMaximum(255)
        self.u_s.valueChanged.connect(self.change)
        self.verticalLayout_2.addWidget(self.u_s)
        self.u_v = QtWidgets.QSlider(self.verticalLayoutWidget)
        self.u_v.setOrientation(QtCore.Qt.Horizontal)
        self.u_v.setObjectName("u_v")
        self.u_v.setMinimum(0)
        self.u_v.setMaximum(255)
        self.u_v.valueChanged.connect(self.change)
        self.verticalLayout_2.addWidget(self.u_v)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.startButton.setText(_translate("MainWindow", "Start"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
