from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class MyWindow(QWidget):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setWindowTitle('test_frame')
        self.resize(500,500)
        self.init_gui()

    def init_gui(self):
        myframe = QFrame(self)
        myframe.resize(200,200)
        myframe.move(100,100)
        myframe.setStyleSheet('background-color:green;')
        # myframe.setFrameShape(QFrame.Box)
        # myframe.setFrameShape(QFrame.Panel)
        # myframe.setFrameShadow(QFrame.Raised)
        myframe.setFrameStyle(QFrame.Box|QFrame.Raised)

        myframe.setLineWidth(10)
        myframe.setMidLineWidth(5)

        # myframe.setFrameRect(QRect(20, 30, 40, 50))

if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    mywindow = MyWindow()
    mywindow.show()
    sys.exit(app.exec())