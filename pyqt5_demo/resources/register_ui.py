# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'register.ui'
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
        Form.setStyleSheet("#Form {\n"
"    border-image:url(:/registerpanel/images/screen1.jpg);\n"
"}")
        self.pushButton_menu = QtWidgets.QPushButton(Form)
        self.pushButton_menu.setGeometry(QtCore.QRect(10, 50, 40, 40))
        self.pushButton_menu.setMinimumSize(QtCore.QSize(40, 40))
        self.pushButton_menu.setMaximumSize(QtCore.QSize(40, 40))
        self.pushButton_menu.setStyleSheet("QPushButton {\n"
"    border:2px solid yellow;\n"
"    border-radius:20px; \n"
"    background-color: rgb(255, 255, 127);\n"
"}\n"
"QPushButton:hover {\n"
"    border:2px solid green;\n"
"    border-radius:20px; \n"
"    background-color: rgb(170, 255, 0);\n"
"}\n"
"QPushButton:checked {\n"
"    border:3px solid blue;\n"
"    background-color: rgb(0, 255, 0);\n"
"}")
        self.pushButton_menu.setCheckable(True)
        self.pushButton_menu.setObjectName("pushButton_menu")
        self.pushButton_quit = QtWidgets.QPushButton(Form)
        self.pushButton_quit.setGeometry(QtCore.QRect(60, 20, 40, 40))
        self.pushButton_quit.setMinimumSize(QtCore.QSize(40, 40))
        self.pushButton_quit.setMaximumSize(QtCore.QSize(40, 40))
        self.pushButton_quit.setStyleSheet("QPushButton {\n"
"    border:2px solid yellow;\n"
"    border-radius:20px; \n"
"    background-color: rgb(255, 255, 127);\n"
"}\n"
"QPushButton:hover {\n"
"    border:2px solid green;\n"
"    border-radius:20px; \n"
"    background-color: rgb(170, 255, 0);\n"
"}\n"
"QPushButton:checked {\n"
"    border:3px solid blue;\n"
"    background-color: rgb(0, 255, 0);\n"
"}")
        self.pushButton_quit.setObjectName("pushButton_quit")
        self.pushButton_about = QtWidgets.QPushButton(Form)
        self.pushButton_about.setGeometry(QtCore.QRect(80, 70, 40, 40))
        self.pushButton_about.setMinimumSize(QtCore.QSize(40, 40))
        self.pushButton_about.setMaximumSize(QtCore.QSize(40, 40))
        self.pushButton_about.setStyleSheet("QPushButton {\n"
"    border:2px solid yellow;\n"
"    border-radius:20px; \n"
"    background-color: rgb(255, 255, 127);\n"
"}\n"
"QPushButton:hover {\n"
"    border:2px solid green;\n"
"    border-radius:20px; \n"
"    background-color: rgb(170, 255, 0);\n"
"}\n"
"QPushButton:checked {\n"
"    border:3px solid blue;\n"
"    background-color: rgb(0, 255, 0);\n"
"}")
        self.pushButton_about.setObjectName("pushButton_about")
        self.pushButton_reset = QtWidgets.QPushButton(Form)
        self.pushButton_reset.setGeometry(QtCore.QRect(30, 100, 40, 40))
        self.pushButton_reset.setMinimumSize(QtCore.QSize(40, 40))
        self.pushButton_reset.setMaximumSize(QtCore.QSize(40, 40))
        self.pushButton_reset.setStyleSheet("QPushButton {\n"
"    border:2px solid yellow;\n"
"    border-radius:20px; \n"
"    background-color: rgb(255, 255, 127);\n"
"}\n"
"QPushButton:hover {\n"
"    border:2px solid green;\n"
"    border-radius:20px; \n"
"    background-color: rgb(170, 255, 0);\n"
"}\n"
"QPushButton:checked {\n"
"    border:3px solid blue;\n"
"    background-color: rgb(0, 255, 0);\n"
"}")
        self.pushButton_reset.setObjectName("pushButton_reset")
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(240, 160, 241, 237))
        self.layoutWidget.setObjectName("layoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.layoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setHorizontalSpacing(10)
        self.formLayout.setVerticalSpacing(5)
        self.formLayout.setObjectName("formLayout")
        self.label_username = QtWidgets.QLabel(self.layoutWidget)
        self.label_username.setMinimumSize(QtCore.QSize(0, 50))
        self.label_username.setStyleSheet("font: 87 10pt \"Arial Black\";")
        self.label_username.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_username.setObjectName("label_username")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_username)
        self.label_password = QtWidgets.QLabel(self.layoutWidget)
        self.label_password.setMinimumSize(QtCore.QSize(0, 50))
        self.label_password.setStyleSheet("font: 87 10pt \"Arial Black\";")
        self.label_password.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_password.setObjectName("label_password")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_password)
        self.lineEdit_password = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_password.setMinimumSize(QtCore.QSize(0, 40))
        self.lineEdit_password.setStyleSheet("QLineEdit {\n"
"    border:none;\n"
"    border-bottom:2px solid green;\n"
"    background-color:transparent;\n"
"}\n"
"\n"
"")
        self.lineEdit_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_password.setClearButtonEnabled(True)
        self.lineEdit_password.setObjectName("lineEdit_password")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_password)
        self.label_confirm = QtWidgets.QLabel(self.layoutWidget)
        self.label_confirm.setMinimumSize(QtCore.QSize(0, 50))
        self.label_confirm.setStyleSheet("font: 87 10pt \"Arial Black\";")
        self.label_confirm.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_confirm.setObjectName("label_confirm")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_confirm)
        self.lineEdit_confirm = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_confirm.setMinimumSize(QtCore.QSize(0, 40))
        self.lineEdit_confirm.setStyleSheet("QLineEdit {\n"
"    border:none;\n"
"    border-bottom:2px solid green;\n"
"    background-color:transparent;\n"
"}\n"
"\n"
"")
        self.lineEdit_confirm.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_confirm.setClearButtonEnabled(True)
        self.lineEdit_confirm.setObjectName("lineEdit_confirm")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_confirm)
        self.pushButton_register = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_register.setEnabled(False)
        self.pushButton_register.setMinimumSize(QtCore.QSize(120, 40))
        self.pushButton_register.setStyleSheet("QPushButton {\n"
"    border: 2px solid yellow;\n"
"    border-radius: 10px;\n"
"    background-color: rgb(85, 255, 255);\n"
"    font-size: 16px ;\n"
"    color:pink;\n"
"}\n"
"QPushButton:disabled {\n"
"    background: gray;\n"
"}\n"
"QPushButton:pressed {\n"
"    background: red;\n"
"    font-size: 18px ;\n"
"}")
        self.pushButton_register.setObjectName("pushButton_register")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.SpanningRole, self.pushButton_register)
        self.lineEdit_username = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_username.setMinimumSize(QtCore.QSize(0, 40))
        self.lineEdit_username.setStyleSheet("QLineEdit {\n"
"    border:none;\n"
"    border-bottom:2px solid green;\n"
"    background-color:transparent;\n"
"}\n"
"\n"
"")
        self.lineEdit_username.setClearButtonEnabled(True)
        self.lineEdit_username.setObjectName("lineEdit_username")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_username)
        self.layoutWidget.raise_()
        self.pushButton_quit.raise_()
        self.pushButton_about.raise_()
        self.pushButton_reset.raise_()
        self.pushButton_menu.raise_()

        self.retranslateUi(Form)
        self.pushButton_about.clicked.connect(Form.about_me)
        self.pushButton_menu.clicked['bool'].connect(Form.show_hide_menue)
        self.pushButton_quit.clicked.connect(Form.exit_panel)
        self.pushButton_reset.clicked.connect(Form.reset_input)
        self.pushButton_register.clicked.connect(Form.check_register)
        self.lineEdit_username.textChanged['QString'].connect(Form.enable_register_btn)
        self.lineEdit_password.textChanged['QString'].connect(Form.enable_register_btn)
        self.lineEdit_confirm.textChanged['QString'].connect(Form.enable_register_btn)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton_menu.setText(_translate("Form", "Menu"))
        self.pushButton_quit.setText(_translate("Form", "Quit"))
        self.pushButton_about.setText(_translate("Form", "About"))
        self.pushButton_reset.setText(_translate("Form", "Reset"))
        self.label_username.setText(_translate("Form", "username:"))
        self.label_password.setText(_translate("Form", "password:"))
        self.label_confirm.setText(_translate("Form", "confirm:"))
        self.pushButton_register.setText(_translate("Form", "Register"))
import pyqt5demo_rc
