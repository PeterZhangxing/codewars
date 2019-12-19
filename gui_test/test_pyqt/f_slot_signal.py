from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class MyWindow(QWidget):

    def __init__(self):
        super(MyWindow,self).__init__()
        self.resize(350,280)
        self.setWindowTitle('这是一个好吃的积极')
        self.init_gui()

    def init_gui(self):
        self.button1 = QPushButton(self)
        self.button1.setText('push1')
        self.button1.move(10,10)
        self.button1.clicked.connect(self.change_wtitle)

        self.button2 = QPushButton(self)
        self.button2.setText('push2')
        self.button2.move(150,10)
        self.button2.clicked.connect(self.dis_parent)

        self.lable1 = QLabel(self)
        self.lable1.setText('label1')
        self.lable1.move(250,10)

        mylabel = QLabel()
        mylabel.destroyed.connect(self.test_des)

    def test_des(self,p_object):
        print('删除对象:',p_object)

    def dis_parent(self):
        for child in self.children():
            if child.inherits('QPushButton'):
                print('button:',child)
            elif child.inherits('QLabel'):
                print('label:',child)

    def change_wtitle(self):
        self.windowTitleChanged.connect(self.ctitle)
        self.setWindowTitle('My')

    def ctitle(self,title):
        # print(title)
        self.blockSignals(True)
        self.setWindowTitle(title+'Window1')
        self.blockSignals(False)


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    mywindow = MyWindow()
    mywindow.show()
    sys.exit(app.exec_())