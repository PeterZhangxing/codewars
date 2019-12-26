from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class MyWindow(QWidget):
    def __init__(self,*args,**kwargs):
        super(MyWindow, self).__init__(*args,**kwargs)
        self.setWindowOpacity(0.8)
        self.resize(500,500)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.flag = False
        self.setMouseTracking(True)

        self.init_gui()

    def init_gui(self):
        self.btn_width = 60
        self.btn_height = 35
        self.btn_y = 5

        self.close_btn = QPushButton(self)
        self.close_btn.setText('close')
        self.close_btn.resize(self.btn_width,self.btn_height)
        self.close_btn.pressed.connect(self.close)

        self.max_btn = QPushButton(self)
        self.max_btn.setText('max')
        self.max_btn.resize(self.btn_width,self.btn_height)
        self.max_btn.pressed.connect(self.win_nor_max)

        self.min_btn = QPushButton(self)
        self.min_btn.setText('min')
        self.min_btn.resize(self.btn_width,self.btn_height)
        self.min_btn.pressed.connect(self.showMinimized)

    def win_nor_max(self):
        if self.isMaximized():
            self.showNormal()
            self.max_btn.setText('max')
        else:
            self.showMaximized()
            self.max_btn.setText('nor')

    def resizeEvent(self, QResizeEvent):
        window_width = self.width()
        close_btn_x = window_width - self.close_btn.width()
        self.close_btn.move(close_btn_x,self.btn_y)

        max_btn_x = close_btn_x - self.max_btn.width()
        self.max_btn.move(max_btn_x,self.btn_y)

        min_btn_x = max_btn_x -self.min_btn.width()
        self.min_btn.move(min_btn_x,self.btn_y)

    def mousePressEvent(self, QMouseEvent):
        self.flag = True
        self.mouse_x = QMouseEvent.globalPos().x()
        self.mouse_y = QMouseEvent.globalPos().y()

        self.ori_x = self.x()
        self.ori_y = self.y()

    def mouseMoveEvent(self, QMouseEvent):
        if self.flag:
            x_len = QMouseEvent.globalPos().x() - self.mouse_x
            y_len = QMouseEvent.globalPos().y() - self.mouse_y

            self.move(self.ori_x+x_len,self.ori_y+y_len)

    def mouseReleaseEvent(self, QMouseEvent):
        self.flag = False


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)

    mywindow = MyWindow()
    mywindow.show()

    sys.exit(app.exec_())