from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class MyWindow(QWidget):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setWindowTitle('test_line_edit')
        self.resize(500,500)
        self.setMaximumSize(800,800)
        self.setMinimumSize(400,400)
        self.widget_margin = 50
        self.init_gui()

    def init_gui(self):
        self.name = QLineEdit(self)
        self.name.setToolTip('username')
        self.name.textChanged.connect(self.judge_content)

        self.pwd = QLineEdit(self)
        self.pwd.setToolTip('password')
        self.pwd.setEchoMode(QLineEdit.PasswordEchoOnEdit)
        self.pwd.textChanged.connect(self.judge_content)

        self.subtn = QPushButton('submit',self)
        self.subtn.resize(self.pwd.width(),self.pwd.height())
        self.subtn.setEnabled(False)
        # self.subtn.clicked.connect(self.test_copy)
        self.subtn.clicked.connect(self.test_login)

        self.tab = QLabel(self)

    def judge_content(self):
        name = self.name.text()
        pwd = self.pwd.text()
        if name and pwd:
            self.subtn.setEnabled(True)
        else:
            self.subtn.setEnabled(False)

    def test_login(self):
        name = self.name.text()
        pwd = self.pwd.text()
        if name != 'zx':
            self.name.setText('')
            self.name.setFocus()
            self.tab.setText('username not valid')
            self.tab.adjustSize()
            return None
        if pwd != 'redhat':
            self.pwd.setText('')
            self.pwd.setFocus()
            self.tab.setText('wrong password')
            self.tab.adjustSize()
            return None
        self.tab.setText('login successfully')
        self.tab.adjustSize()

    def test_copy(self):
        content = self.name.text()
        self.pwd.setText(content)
        # self.pwd.insert(content)

    def resizeEvent(self, QResizeEvent):
        name_x = (self.width()-self.name.width())/2
        name_y = self.height()/5
        self.name.move(name_x,name_y)

        pwd_x = name_x
        pwd_y = name_y + self.name.height() + self.widget_margin
        self.pwd.move(pwd_x,pwd_y)

        subtn_x = (self.width()-self.subtn.width())/2
        subtn_y = pwd_y + self.pwd.height() + self.widget_margin
        self.subtn.move(subtn_x,subtn_y)

        tab_x = name_x
        tab_y = subtn_y + self.subtn.height() + self.widget_margin
        self.tab.move(tab_x,tab_y)

if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)

    mywindow = MyWindow()
    mywindow.show()

    sys.exit(app.exec())