from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class MyWindow(QWidget):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setWindowTitle('QScrollBar的学习')
        self.resize(500, 500)
        self.init_gui()

    def init_gui(self):
        self.myscb = QScrollBar(self)
        self.myscb.move(100,100)
        self.myscb.resize(30,200)
        self.myscb.valueChanged.connect(lambda val:print(val))
        # self.myscb.grabKeyboard()
        self.myscb.setRange(100,200)
        self.myscb.setPageStep(100)

        self.myscbh = QScrollBar(Qt.Horizontal,self)
        self.myscbh.move(200,100)
        self.myscbh.resize(200,35)

        self.qd = QDial(self)
        self.qd.move(200,200)
        self.qd.setRange(0,100)
        self.qd.setNotchesVisible(True)
        # self.qd.valueChanged.connect(lambda val:print(val))
        self.qd.valueChanged.connect(self.changefont)
        self.qd.setWrapping(True)
        self.qd.setNotchTarget(5)
        self.qd.setPageStep(5)
        self.qd.grabKeyboard()

        self.label = QLabel(self)
        self.label.move(100, 10)
        self.label.setText("fuck you!")

    def changefont(self,val):
        self.label.setStyleSheet('font-size:%spx;'%val)
        self.label.adjustSize()

if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    mywindow = MyWindow()
    mywindow.show()
    sys.exit(app.exec_())