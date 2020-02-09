from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class MyTestWindow(QWidget):
    def __init__(self):
        super(MyTestWindow, self).__init__()
        self.setWindowTitle('QScrollBar的学习')
        self.resize(500, 500)
        self.init_gui()

    def init_gui(self):
        myrb = QRubberBand(QRubberBand.Rectangle,self)
        myrb.setGeometry(100,100,30,30)
        print(myrb.isVisible())
        myrb.setVisible(True)
        print(myrb.isVisible())

class MyWindow(QWidget):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setWindowTitle('QScrollBar的学习')
        self.resize(500, 500)
        self.init_gui()

    def init_gui(self):
        self.myrb = QRubberBand(QRubberBand.Rectangle,self)
        self.cb_li = []
        for i in range(30):
            cb = QCheckBox(self)
            cb.setText('%s'%i)
            cb.move(i%4*50,i//4*50)
            self.cb_li.append(cb)

    def mousePressEvent(self,evt):
        self.origin_pos = evt.pos()
        self.myrb.setGeometry(QRect(self.origin_pos, QSize()))
        self.myrb.setVisible(True)
        # self.myrb.show()

    def mouseMoveEvent(self,evt):
        self.myrb.setGeometry(QRect(self.origin_pos,evt.pos()).normalized())

    def mouseReleaseEvent(self,evt):
        self.myrb.setVisible(False)
        # for child in self.children():
        #     if self.myrb.geometry().contains(child.geometry()) and child.inherits('QCheckBox'):
        #         child.toggle()

        for box in self.cb_li:
            if self.myrb.geometry().contains(box.geometry()):
                box.toggle()

if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    mywindow = MyWindow()
    mywindow.show()
    sys.exit(app.exec_())