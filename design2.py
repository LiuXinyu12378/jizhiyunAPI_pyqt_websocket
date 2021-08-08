# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QTextCursor

from utils import send_data





class Ui_dialog(object):
    def setupUi(self, dialog):
        dialog.setObjectName("dialog")
        dialog.resize(917, 655)
        dialog.setToolTipDuration(-4)
        self.textEdit = QtWidgets.QTextEdit(dialog)
        self.textEdit.setGeometry(QtCore.QRect(10, 400, 901, 241))
        self.textEdit.setObjectName("textEdit")
        self.textEdit.setText("xinyuuliu's 智能家居：")
        self.textEdit.moveCursor(QTextCursor.End)

        self.label = QtWidgets.QLabel(dialog)
        self.label.setGeometry(QtCore.QRect(130, 150, 111, 31))
        self.label.setMaximumSize(QtCore.QSize(16777215, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setLineWidth(6)
        self.label.setScaledContents(True)
        self.label.setWordWrap(False)
        self.label.setOpenExternalLinks(False)
        self.label.setObjectName("label")

        self.radioButton = QtWidgets.QRadioButton(dialog)
        self.radioButton.setGeometry(QtCore.QRect(250, 150, 93, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.radioButton.setFont(font)
        self.radioButton.setObjectName("radioButton")
        self.radioButton.toggled.connect(lambda: self.btnstate(self.radioButton))

        self.radioButton_2 = QtWidgets.QRadioButton(dialog)
        self.radioButton_2.setGeometry(QtCore.QRect(350, 150, 93, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_2.toggled.connect(lambda: self.btnstate(self.radioButton_2))

        self.label_3 = QtWidgets.QLabel(dialog)
        self.label_3.setGeometry(QtCore.QRect(220, -10, 541, 141))
        self.label_3.setObjectName("label_3")

        self.radioButton_3 = QtWidgets.QRadioButton(dialog)
        self.radioButton_3.setGeometry(QtCore.QRect(350, 200, 93, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.radioButton_3.setFont(font)
        self.radioButton_3.setObjectName("radioButton_3")
        self.radioButton_3.toggled.connect(lambda: self.btnstate2(self.radioButton_3))
        self.label_2 = QtWidgets.QLabel(dialog)
        self.label_2.setGeometry(QtCore.QRect(130, 200, 111, 31))
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setLineWidth(6)
        self.label_2.setScaledContents(True)
        self.label_2.setWordWrap(False)
        self.label_2.setOpenExternalLinks(False)
        self.label_2.setObjectName("label_2")
        self.radioButton_4 = QtWidgets.QRadioButton(dialog)
        self.radioButton_4.setGeometry(QtCore.QRect(250, 200, 93, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.radioButton_4.setFont(font)
        self.radioButton_4.setObjectName("radioButton_4")
        self.radioButton_4.toggled.connect(lambda: self.btnstate2(self.radioButton_4))
        self.label_4 = QtWidgets.QLabel(dialog)
        self.label_4.setGeometry(QtCore.QRect(550, 140, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(dialog)
        self.label_5.setGeometry(QtCore.QRect(550, 190, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")

        self.label_6 = QtWidgets.QLabel(dialog)
        self.label_6.setGeometry(QtCore.QRect(630, 150, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(dialog)
        self.label_7.setGeometry(QtCore.QRect(630, 190, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")

        self.label_3.raise_()
        self.textEdit.raise_()
        self.label.raise_()
        self.radioButton.raise_()
        self.radioButton_2.raise_()
        self.radioButton_3.raise_()
        self.label_2.raise_()
        self.radioButton_4.raise_()
        self.label_4.raise_()
        self.label_5.raise_()


        self.retranslateUi(dialog)
        QtCore.QMetaObject.connectSlotsByName(dialog)

    def retranslateUi(self, dialog):
        _translate = QtCore.QCoreApplication.translate
        dialog.setWindowTitle(_translate("dialog", "Dialog"))
        self.label.setText(_translate("dialog", "灯1开关："))
        self.radioButton.setText(_translate("dialog", "开灯"))
        self.radioButton_2.setText(_translate("dialog", "关灯"))
        self.label_3.setText(_translate("dialog", "<html><head/><body><p><img src=\"o_nuttertools.png\"/></p></body></html>"))
        self.radioButton_3.setText(_translate("dialog", "关灯"))
        self.label_2.setText(_translate("dialog", "灯2开关："))
        self.radioButton_4.setText(_translate("dialog", "开灯"))
        self.label_4.setText(_translate("dialog", "温度："))
        self.label_5.setText(_translate("dialog", "湿度："))




# import nuttertools_rc
