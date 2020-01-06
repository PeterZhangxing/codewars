from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class MyWindow(QWidget):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setWindowTitle('QRadioButton-功能测试')
        self.resize(500,500)
        self.init_gui()

    def init_gui(self):
        mrbtn = QRadioButton('Male',self)
        mrbtn.setIcon(QIcon('images/loading'))
        # mrbtn.setIconSize(QSize(60,60))
        mrbtn.setChecked(True)
        mrbtn.setShortcut('Alt+M')
        mrbtn.move(50,100)

        frbtn = QRadioButton('Female',self)
        frbtn.setChecked(True)
        frbtn.setShortcut('Alt+F')
        frbtn.move(50,150)

        self.gender_rbtn_group = QButtonGroup(self)
        self.gender_rbtn_group.addButton(mrbtn)
        self.gender_rbtn_group.addButton(frbtn)
        self.gender_rbtn_group.setId(mrbtn,1)
        self.gender_rbtn_group.setId(frbtn,2)
        self.gender_rbtn_group.buttonClicked.connect(self.get_gender_button_id)

        yrbtn = QRadioButton('Yes',self)
        yrbtn.setChecked(True)
        yrbtn.setShortcut('Alt+Y')
        yrbtn.move(200,100)

        nrbtn = QRadioButton('No',self)
        nrbtn.setShortcut('Alt+N')
        nrbtn.move(200,150)

        self.choose_rbtn_group = QButtonGroup(self)
        self.choose_rbtn_group.addButton(yrbtn)
        self.choose_rbtn_group.addButton(nrbtn)
        self.choose_rbtn_group.setId(yrbtn,1)
        self.choose_rbtn_group.setId(nrbtn,2)
        self.choose_rbtn_group.buttonClicked[int].connect(self.get_choose_button_id)

    def get_gender_button_id(self,QAbstractButton):
        print(QAbstractButton.isChecked())
        btnid = self.gender_rbtn_group.id(QAbstractButton)
        print(btnid)
        # self.gender_rbtn_group.setExclusive(False)
        # self.gender_rbtn_group.removeButton(r_female)
        # print(self.gender_rbtn_group.buttons())
        # print(self.gender_rbtn_group.button(2))
        # print(self.gender_rbtn_group.checkedButton())

    def get_choose_button_id(self,btnid):
        print(btnid)
        print(self.choose_rbtn_group.children())
        print(self.choose_rbtn_group.checkedId())
        print(self.choose_rbtn_group.buttons())
        print(self.choose_rbtn_group.button(btnid))


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)

    mywindow = MyWindow()
    mywindow.show()

    sys.exit(app.exec())