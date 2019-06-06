# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import Variables
import Calibration
import MainFunctions as Main
from queue import Queue

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(192, 363)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 110, 171, 61))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.leftSide = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.leftSide.setObjectName("leftSide")
        self.horizontalLayout.addWidget(self.leftSide)
        self.rightSide = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.rightSide.setObjectName("rightSide")
        self.horizontalLayout.addWidget(self.rightSide)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(10, 180, 171, 151))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.label_3.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_4.addWidget(self.label_3)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.l_h = QtWidgets.QSlider(self.verticalLayoutWidget_4)
        self.l_h.setMaximum(179)
        self.l_h.setOrientation(QtCore.Qt.Horizontal)
        self.l_h.setObjectName("l_h")
        self.verticalLayout_3.addWidget(self.l_h)
        self.l_s = QtWidgets.QSlider(self.verticalLayoutWidget_4)
        self.l_s.setMaximum(255)
        self.l_s.setOrientation(QtCore.Qt.Horizontal)
        self.l_s.setObjectName("l_s")
        self.verticalLayout_3.addWidget(self.l_s)
        self.l_v = QtWidgets.QSlider(self.verticalLayoutWidget_4)
        self.l_v.setMaximum(255)
        self.l_v.setOrientation(QtCore.Qt.Horizontal)
        self.l_v.setObjectName("l_v")
        self.verticalLayout_3.addWidget(self.l_v)
        self.u_h = QtWidgets.QSlider(self.verticalLayoutWidget_4)
        self.u_h.setMaximum(179)
        self.u_h.setOrientation(QtCore.Qt.Horizontal)
        self.u_h.setObjectName("u_h")
        self.verticalLayout_3.addWidget(self.u_h)
        self.u_s = QtWidgets.QSlider(self.verticalLayoutWidget_4)
        self.u_s.setMaximum(255)
        self.u_s.setOrientation(QtCore.Qt.Horizontal)
        self.u_s.setObjectName("u_s")
        self.verticalLayout_3.addWidget(self.u_s)
        self.u_v = QtWidgets.QSlider(self.verticalLayoutWidget_4)
        self.u_v.setMaximum(255)
        self.u_v.setOrientation(QtCore.Qt.Horizontal)
        self.u_v.setObjectName("u_v")
        self.verticalLayout_3.addWidget(self.u_v)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 10, 171, 89))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.btnCalibrate = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.btnCalibrate.setObjectName("btnCalibrate")
        self.verticalLayout_2.addWidget(self.btnCalibrate)
        self.checkCalibrated = QtWidgets.QCheckBox(self.verticalLayoutWidget_2)
        self.checkCalibrated.setEnabled(True)
        self.checkCalibrated.setCheckable(True)
        self.checkCalibrated.setChecked(False)
        self.checkCalibrated.setObjectName("checkCalibrated")
        self.verticalLayout_2.addWidget(self.checkCalibrated)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.btnStart = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.btnStart.setObjectName("btnStart")
        self.btnStart.setDisabled(True)
        self.horizontalLayout_3.addWidget(self.btnStart)
        self.btnStop = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.btnStop.setObjectName("btnStop")
        self.btnStop.setDisabled(True)
        self.horizontalLayout_3.addWidget(self.btnStop)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 251, 22))
        self.menubar.setObjectName("menubar")
        self.menuMenu = QtWidgets.QMenu(self.menubar)
        self.menuMenu.setObjectName("menuMenu")
        MainWindow.setMenuBar(self.menubar)
        self.actionSair = QtWidgets.QAction(MainWindow)
        self.actionSair.setObjectName("actionSair")
        self.menuMenu.addAction(self.actionSair)
        self.menubar.addAction(self.menuMenu.menuAction())

        # Actions
        self.u_h.valueChanged.connect(self.change)
        self.u_s.valueChanged.connect(self.change)
        self.u_v.valueChanged.connect(self.change)
        self.l_h.valueChanged.connect(self.change)
        self.l_s.valueChanged.connect(self.change)
        self.l_v.valueChanged.connect(self.change)
        self.btnCalibrate.clicked.connect(self.callCalibration)
        self.btnStart.clicked.connect(self.callStart)
        self.btnStop.clicked.connect(self.setStopFlag)
        self.actionSair.triggered.connect(self.exitProgram)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "VSSS"))
        self.label_4.setText(_translate("MainWindow", "Nosso lado"))
        self.leftSide.setText(_translate("MainWindow", "ESQUERDA"))
        self.rightSide.setText(_translate("MainWindow", "DIREITA"))
        self.label_3.setText(_translate("MainWindow", "Threshold Bola"))
        self.l_h.setToolTip(_translate("MainWindow", "Hue MIN"))
        self.l_s.setToolTip(_translate("MainWindow", "Saturation MIN"))
        self.l_v.setToolTip(_translate("MainWindow", "Value MIN"))
        self.u_h.setToolTip(_translate("MainWindow", "Hue MAX"))
        self.u_s.setToolTip(_translate("MainWindow", "Saturation MAX"))
        self.u_v.setToolTip(_translate("MainWindow", "Value MAX"))
        self.btnCalibrate.setText(_translate("MainWindow", "Calibrar"))
        self.checkCalibrated.setText(_translate("MainWindow", "Calibrado"))
        self.btnStart.setText(_translate("MainWindow", "Start"))
        self.btnStop.setText(_translate("MainWindow", "Stop"))
        self.menuMenu.setTitle(_translate("MainWindow", "Menu"))
        self.actionSair.setText(_translate("MainWindow", "Sair"))

    def change(self):
        Variables.l_h = self.l_h.value()
        Variables.l_s = self.l_s.value()
        Variables.l_v = self.l_v.value()
        Variables.u_h = self.u_h.value()
        Variables.u_s = self.u_s.value()
        Variables.u_v = self.u_v.value()

    def callCalibration(self):
        Calibration.CalibrarCamera()
        self.checkCalibrated.setChecked(True)

    def setStopFlag(self):
        Variables.stopFlag = True
        self.btnStart.setDisabled(False)
        self.btnStop.setDisabled(True)

    def callStart(self):
        Variables.stopFlag = False
        self.btnStart.setDisabled(True)
        self.btnStop.setDisabled(False)
        Main.startCapture()

    def exitProgram(self):
        Variables.stopFlag = True
        sys.exit(app.exec_())

    def setStartDisabled(self, val):
        self.btnStart.setDisabled(val)

    def setStopDisable(self, val):
        self.btnStop.setDisabled(val)


if __name__ == "__main__":
    import sys
    Variables.Global()
    Calibration.configureCalibration()
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    Variables.ui = ui
    ui.setupUi(MainWindow)
    MainWindow.setFixedSize(MainWindow.size())
    MainWindow.show()
    sys.exit(app.exec_())
