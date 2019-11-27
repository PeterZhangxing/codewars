from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys


class MyMainWin(QWidget):

    def __init__(self):
        super(MyMainWin,self).__init__()
        self.init_gui()

    def init_gui(self):
         layout = QGridLayout()

         self.pushbutton_c2f = QPushButton('C_TO_F >>>')
         self.pushbutton_f2c = QPushButton('<<< F_TO_C')

         self.label_c = QLabel()
         self.label_c.setText('C:')

         self.label_f = QLabel()
         self.label_f.setText('F:')

         self.input_c = QLineEdit()
         self.input_c.setValidator(QDoubleValidator(-199.99, 199.99, 2))

         self.input_f = QLineEdit()
         self.input_f.setValidator(QDoubleValidator(-1999.99, 1999.99, 2))

         layout.addWidget(self.pushbutton_c2f,0,1,1,1)
         layout.addWidget(self.pushbutton_f2c,3,1,1,1)

         layout.addWidget(self.label_c,1,0,1,1)
         layout.addWidget(self.label_f,1,2,1,1)

         layout.addWidget(self.input_c,2,0,1,1)
         layout.addWidget(self.input_f,2,2,1,1)

         self.pushbutton_c2f.clicked.connect(self.myc2f)
         self.pushbutton_f2c.clicked.connect(self.myf2c)

         self.setLayout(layout)
         self.setWindowTitle('transform c to f')

    def myc2f(self):
        # print('in c2f')
        c_iput = self.input_c.text()
        if not c_iput:
            return
        # print(type(c_iput))
        f_res = float(c_iput) * 9 / 5.0 + 32
        self.input_f.setText('%.2f'%f_res)

    def myf2c(self):
        # print('in f2c')
        f_iput = self.input_f.text()
        if not f_iput:
            return
        # print(type(f_iput))
        c_res = (float(f_iput) - 32) * 5 / 9.0
        self.input_c.setText('%.2f'%c_res)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myw = MyMainWin()
    myw.show()
    sys.exit(app.exec_())
