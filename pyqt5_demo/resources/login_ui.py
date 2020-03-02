# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(500, 450)
        Form.setMinimumSize(QtCore.QSize(500, 450))
        Form.setMaximumSize(QtCore.QSize(500, 450))
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setStyleSheet("")
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_register = QtWidgets.QLabel(self.widget)
        self.label_register.setObjectName("label_register")
        self.horizontalLayout.addWidget(self.label_register)
        self.verticalLayout.addWidget(self.widget)
        self.widget_2 = QtWidgets.QWidget(Form)
        self.widget_2.setStyleSheet("")
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 12)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_register = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_register.setFlat(True)
        self.pushButton_register.setObjectName("pushButton_register")
        self.horizontalLayout_2.addWidget(self.pushButton_register, 0, QtCore.Qt.AlignLeft|QtCore.Qt.AlignBottom)
        self.widget_3 = QtWidgets.QWidget(self.widget_2)
        self.widget_3.setStyleSheet("")
        self.widget_3.setObjectName("widget_3")
        self.gridLayout = QtWidgets.QGridLayout(self.widget_3)
        self.gridLayout.setObjectName("gridLayout")
        self.comboBox_account = QtWidgets.QComboBox(self.widget_3)
        self.comboBox_account.setMinimumSize(QtCore.QSize(0, 45))
        self.comboBox_account.setStyleSheet("QComboBox {\n"
"    font-size: 20px;\n"
"    border: none;\n"
"    border-bottom: 1px solid lightgray;\n"
"    background-color: transparent;\n"
"}\n"
"QComboBox:hover {\n"
"    border-bottom: 1px solid gray;\n"
"}\n"
"QComboBox:focus {\n"
"    border-bottom: 1px solid rgb(18, 183, 245);\n"
"}\n"
"QComboBox::drop-down {\n"
"    background-color: transparent;\n"
"    width: 60px;\n"
"    height: 40px;\n"
"}\n"
"QComboBox::down-arrow {\n"
"    image: url(:/loginpanel/images/down3.png);\n"
"    width: 60px;\n"
"    height: 20px;\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"    min-height: 60px;\n"
"}\n"
"QComboBox QAbstractItemView:item {\n"
"    color: lightblue;\n"
"}")
        self.comboBox_account.setEditable(True)
        self.comboBox_account.setObjectName("comboBox_account")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/loginpanel/images/login_combobox_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.comboBox_account.addItem(icon, "")
        self.comboBox_account.addItem(icon, "")
        self.gridLayout.addWidget(self.comboBox_account, 0, 0, 1, 2)
        self.lineEdit_pwd = QtWidgets.QLineEdit(self.widget_3)
        self.lineEdit_pwd.setMinimumSize(QtCore.QSize(0, 45))
        self.lineEdit_pwd.setStyleSheet("QLineEdit {\n"
"    font-size: 20px;\n"
"    border: none;\n"
"    border-bottom: 1px solid lightgray;\n"
"    background-color: transparent;\n"
"}\n"
"QLineEdit:hover {\n"
"    border-bottom: 1px solid gray;\n"
"}\n"
"QLineEdit:focus {\n"
"    border-bottom: 1px solid rgb(18, 183, 245);\n"
"}")
        self.lineEdit_pwd.setEchoMode(QtWidgets.QLineEdit.PasswordEchoOnEdit)
        self.lineEdit_pwd.setClearButtonEnabled(True)
        self.lineEdit_pwd.setObjectName("lineEdit_pwd")
        self.gridLayout.addWidget(self.lineEdit_pwd, 1, 0, 1, 2)
        self.checkBox_autologin = QtWidgets.QCheckBox(self.widget_3)
        self.checkBox_autologin.setObjectName("checkBox_autologin")
        self.gridLayout.addWidget(self.checkBox_autologin, 2, 0, 1, 1)
        self.checkBox_rempwd = QtWidgets.QCheckBox(self.widget_3)
        self.checkBox_rempwd.setObjectName("checkBox_rempwd")
        self.gridLayout.addWidget(self.checkBox_rempwd, 2, 1, 1, 1)
        self.pushButton_login = QtWidgets.QPushButton(self.widget_3)
        self.pushButton_login.setEnabled(False)
        self.pushButton_login.setMinimumSize(QtCore.QSize(0, 50))
        self.pushButton_login.setStyleSheet("QPushButton {\n"
"    background-color: rgb(33, 174, 250);\n"
"    border-radius: 8px;\n"
"    color: white;\n"
"    spacing: 40px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(72, 203, 250);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(85, 85, 255);\n"
"}\n"
"QPushButton:disabled {\n"
"    background-color: rgb(167, 167, 167);\n"
"}")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/loginpanel/images/login_btn_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_login.setIcon(icon1)
        self.pushButton_login.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_login.setObjectName("pushButton_login")
        self.gridLayout.addWidget(self.pushButton_login, 3, 0, 1, 2)
        self.horizontalLayout_2.addWidget(self.widget_3)
        self.pushButton_qq = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_qq.setMinimumSize(QtCore.QSize(80, 80))
        self.pushButton_qq.setMaximumSize(QtCore.QSize(80, 80))
        self.pushButton_qq.setStyleSheet("QPushButton {\n"
"    border-image: url(:/loginpanel/images/login_qrcode.png);\n"
"}")
        self.pushButton_qq.setObjectName("pushButton_qq")
        self.horizontalLayout_2.addWidget(self.pushButton_qq, 0, QtCore.Qt.AlignRight|QtCore.Qt.AlignBottom)
        self.horizontalLayout_2.setStretch(0, 2)
        self.horizontalLayout_2.setStretch(1, 6)
        self.horizontalLayout_2.setStretch(2, 2)
        self.verticalLayout.addWidget(self.widget_2)
        self.verticalLayout.setStretch(0, 3)
        self.verticalLayout.setStretch(1, 4)

        self.retranslateUi(Form)
        self.comboBox_account.currentTextChanged['QString'].connect(Form.userinfo_changed)
        self.lineEdit_pwd.textChanged['QString'].connect(Form.userinfo_changed)
        self.checkBox_autologin.clicked['bool'].connect(Form.autologin_changed)
        self.checkBox_rempwd.clicked['bool'].connect(Form.rem_pwd_changed)
        self.pushButton_register.clicked.connect(Form.register_panel_show)
        self.pushButton_qq.clicked.connect(Form.dispaly_qq)
        self.pushButton_login.clicked.connect(Form.get_login_info)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_register.setText(_translate("Form", "TextLabel"))
        self.pushButton_register.setText(_translate("Form", "Register"))
        self.comboBox_account.setItemText(0, _translate("Form", "964725349"))
        self.comboBox_account.setItemText(1, _translate("Form", "1184318368"))
        self.checkBox_autologin.setText(_translate("Form", "AutoLogin"))
        self.checkBox_rempwd.setText(_translate("Form", "RememberPassword"))
        self.pushButton_login.setText(_translate("Form", "Security Login"))
        self.pushButton_qq.setText(_translate("Form", "qrccode"))
import pyqt5demo_rc
