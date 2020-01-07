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
        self.pwd = QLineEdit(self)
        self.subtn = QPushButton('submit',self)
        self.subtn.clicked.connect(self.test_copy)

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


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)

    mywindow = MyWindow()
    mywindow.show()

    sys.exit(app.exec())