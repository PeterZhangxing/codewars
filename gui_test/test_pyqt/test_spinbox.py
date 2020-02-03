from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class MySpinBox(QSpinBox):
    def textFromValue(self,p_int):
        res_str = str(p_int) + "-$-" + str(p_int)
        return res_str

    def valueFromText(self,p_str):
        print("xxx",p_str)

class MyWindow(QWidget):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setWindowTitle('QSpinBox的学习')
        self.resize(500,500)
        self.init_gui()

    def init_gui(self):
        # self.spb = QSpinBox(self)
        self.spb = MySpinBox(self)
        self.spb.resize(100,25)
        self.spb.move(100,100)
        # self.spb.setDisplayIntegerBase(2)
        print(self.spb.displayIntegerBase())

        self.spb.valueChanged[str].connect(lambda val:print(type(val),val))
        self.spb.valueChanged.connect(lambda val:print(type(val),val))

        btn = QPushButton(self)
        btn.setText("测试按钮")
        btn.move(150, 150)
        btn.clicked.connect(lambda :self.spb.lineEdit().setText("30*30"))
        btn.clicked.connect(lambda :print(type(self.spb.text()),self.spb.text()))
        btn.clicked.connect(lambda :print(self.spb.value()))
        btn.clicked.connect(lambda :self.spb.setSingleStep(2))

        btn1 = QPushButton(self)
        btn1.setText("测试按钮1")
        btn1.move(250, 150)
        btn1.clicked.connect(self.setfixnrange)

    def setfixnrange(self):
        # self.spb.setMaximum(10)
        # self.spb.setMinimum(0)
        self.spb.setRange(0, 6)
        self.spb.setPrefix("周")
        self.spb.setSuffix("&")
        self.spb.setWrapping(True)
        self.spb.setSpecialValueText("周日")
        print(self.spb.minimum())

if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    mywindow = MyWindow()
    mywindow.show()
    sys.exit(app.exec_())