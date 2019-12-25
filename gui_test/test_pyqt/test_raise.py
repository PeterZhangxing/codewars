from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class MyLabel(QLabel):
    def mousePressEvent(self, evt):
        # self.raise_()
        self.lower()

class MyWindow(QWidget):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setWindowTitle('raise_lower_stuck')
        self.resize(500,500)
        self.init_gui()

    def init_gui(self):
        self.lable1 = MyLabel(self)
        self.lable1.resize(100,100)
        self.lable1.setText('Label1')
        self.lable1.setStyleSheet('background-color:red;')

        self.lable2 = MyLabel(self)
        self.lable2.resize(100,100)
        self.lable2.setText('Label2')
        self.lable2.setStyleSheet('background-color:yellow;')
        self.lable2.move(50,50)

if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)

    mywindow = MyWindow()
    mywindow.show()

    mylabel1 = MyLabel(mywindow)
    mylabel1.setText('23123123')
    mylabel2 = MyLabel(mywindow)
    mylabel2.setText('43423432')
    mylabel1.stackUnder(mylabel2)
    mylabel1.show()
    mylabel2.show()

    sys.exit(app.exec_())