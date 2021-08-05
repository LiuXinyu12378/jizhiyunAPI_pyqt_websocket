# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from utils import write1, write0, ws, send_led0, send_led1


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(463, 347)

        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(20, 120, 431, 211))
        self.textEdit.setObjectName("textEdit")
        self.textEdit.setText("xinyuuliu's 智能家居：")

        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(80, 70, 61, 31))
        self.label.setMaximumSize(QtCore.QSize(16777215, 31))
        self.label.setLineWidth(6)
        self.label.setScaledContents(True)
        self.label.setWordWrap(False)
        self.label.setOpenExternalLinks(False)
        self.label.setObjectName("label")

        self.radioButton = QtWidgets.QRadioButton(Dialog)
        self.radioButton.setGeometry(QtCore.QRect(170, 80, 93, 16))
        self.radioButton.toggled.connect(lambda: self.btnstate(self.radioButton))
        self.radioButton.setObjectName("radioButton")

        self.radioButton_2 = QtWidgets.QRadioButton(Dialog)
        self.radioButton_2.setGeometry(QtCore.QRect(270, 80, 93, 16))
        self.radioButton_2.toggled.connect(lambda: self.btnstate(self.radioButton_2))
        self.radioButton_2.setObjectName("radioButton_2")

        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(190, 30, 54, 12))
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "智能家居"))
        self.label.setText(_translate("Dialog", "灯开关："))
        self.radioButton.setText(_translate("Dialog", "开灯"))
        self.radioButton_2.setText(_translate("Dialog", "关灯"))
        self.label_2.setText(_translate("Dialog", "智能家居"))


    def btnstate(self, btn):
        # 输出按钮1与按钮2的状态，选中还是没选中
        if btn.text() == '开灯':
            if btn.isChecked() == True:
                send_led0()

        if btn.text() == "关灯":
            if btn.isChecked() == True:
                send_led1()

