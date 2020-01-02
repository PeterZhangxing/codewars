from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import math
import time

class MyBtn(QPushButton):
    def __init__(self,parent):
        super(MyBtn, self).__init__(parent)
        self.resize(200,200)
        self.setCheckable(True)

    def hitButton(self, QPoint):
        center_x = self.width()//2
        center_y = self.height()//2

        point_x = QPoint.x()
        point_y = QPoint.y()

        distance = math.pow(point_x-center_x,2) + math.pow(point_y-center_y,2)
        if distance > math.pow(center_x,2):
            return False
        return True

    def paintEvent(self, QPaintEvent):
        super(MyBtn, self).paintEvent(QPaintEvent)
        painter = QPainter(self)
        pen = QPen(QColor(0,255,0),2)
        painter.setPen(pen)
        painter.drawEllipse(self.rect())


class MyWindow(QWidget):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setWindowTitle('按钮模拟点击')
        self.resize(500,500)
        self.init_gui()

    def init_gui(self):
        self.btn = MyBtn(self)
        self.btn.move(100,100)
        self.btn.setText('push me')

        self.btn.pressed.connect(lambda :print('pressed'))
        self.btn.released.connect(lambda :print('realsed'))
        self.btn.clicked.connect(lambda value:print('clicked',value))
        self.btn.toggled.connect(lambda value:print('toggled',value))

        self.test_btn = QPushButton(self)
        self.test_btn.setText('test_button')

        self.test_btn.pressed.connect(self.btn_pressed)

    def btn_pressed(self):
        # self.btn.click()
        self.btn.animateClick(1000)
        # self.btn.toggle()
        # self.btn.releaseMouse()


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)

    mywindow = MyWindow()
    mywindow.show()

    sys.exit(app.exec_())