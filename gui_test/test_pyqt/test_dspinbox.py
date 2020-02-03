from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class MyDoubleSpinBox(QDoubleSpinBox):
    def textFromValue(self,p_float):
        res_str = str(p_float) + "-*-" + str(p_float)
        return res_str

class MyWindow(QWidget):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setWindowTitle('QDoubleSpinBox学习')
        self.resize(500,500)
        self.init_gui()

    def init_gui(self):
        self.mdsb = MyDoubleSpinBox(self)
        self.mdsb.resize(200,35)
        self.mdsb.move(100,100)

        # self.mdsb.setMaximum(88.88)
        # self.mdsb.setMinimum(22.22)
        self.mdsb.setRange(20.00,30.00)

        self.mdsb.setSingleStep(0.02)
        self.mdsb.setDecimals(2)
        self.mdsb.setWrapping(True)
        self.mdsb.setAccelerated(True)

        self.mdsb.setPrefix("^")
        self.mdsb.setSuffix("$")
        self.mdsb.setSpecialValueText('start')

        self.mdsb.valueChanged.connect(lambda val:print(type(val),val))
        self.mdsb.valueChanged[str].connect(lambda val:print(type(val),val))

        test_btn = QPushButton(self)
        test_btn.move(300, 300)
        test_btn.setText("测试按钮")
        test_btn.clicked.connect(self.get_val)

    def get_val(self):
        self.mdsb.setValue(20.11)
        mytext = self.mdsb.text()
        myval = self.mdsb.value()
        mycleantext = self.mdsb.cleanText()
        print("mytext:%s  myval:%s  mycleantext:%s"%(mytext,myval,mycleantext))

if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    mywindow = MyWindow()
    mywindow.show()
    sys.exit(app.exec_())