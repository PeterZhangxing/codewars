from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class MyWindow(QWidget):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setWindowTitle('test_mouse_drag')
        self.resize(500,500)
        self.setMouseTracking(True)
        self.flag = False

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