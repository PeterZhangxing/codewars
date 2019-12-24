from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
# QMouseEvent

class MyWindow(QWidget):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setWindowTitle('test_cursor')
        self.resize(300,300)

        pixmap = QPixmap('images/boy.png').scaled(50,50)
        mycur = QCursor(pixmap,0,0)
        self.setCursor(mycur)
        self.setMouseTracking(True)

        self.mylabel = QLabel(self)
        self.mylabel.setText('moving with you')
        self.mylabel.setStyleSheet('background-color:green;')

    def mouseMoveEvent(self, mv):
        self.mx = mv.localPos().x()
        self.my = mv.localPos().y()
        self.move_label()

    def move_label(self):
        self.mylabel.move(self.mx,self.my)

    def enterEvent(self, QEvent):
        print('enter the window')
        self.mylabel.setText('you are welcom!')

    def leaveEvent(self, QEvent):
        print('leave the window')
        self.mylabel.setText('thanks for coming!')


class OutWindow(QWidget):
    def __init__(self,*args,**kwargs):
        super(OutWindow, self).__init__(*args,**kwargs)
        self.setWindowTitle('deal_event')
        self.resize(500,500)

        icon = QIcon('images/boy.png')
        self.setWindowIcon(icon)
        self.setWindowOpacity(0.4)

    def mousePressEvent(self, mpe):
        print(mpe.isAccepted())
        print('OutWindow pressed')
        mpe.accept()


class InnerWindow(QWidget):
    def __init__(self,*args,**kwargs):
        super(InnerWindow, self).__init__(*args,**kwargs)
        # self.setWindowTitle('deal_event')
        self.resize(300, 300)
        self.setAttribute(Qt.WA_StyledBackground,True)
        self.setStyleSheet("background-color:green;")

    def mousePressEvent(self, mpe):
        print(mpe.isAccepted())
        mpe.ignore()
        print('InnerWindow pressed')


class MyLabel(QLabel):
    def __init__(self,*args,**kwargs):
        super(MyLabel, self).__init__(*args,**kwargs)
        # self.setWindowTitle('deal_event')
        self.setText('my label')
        self.move(100,100)

    def mousePressEvent(self, QMouseEvent):
        print(QMouseEvent.isAccepted())
        print("标签鼠标按下")
        QMouseEvent.ignore()


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)

    # mywindow = MyWindow()
    # mywindow.show()

    outwin = OutWindow()
    innerwin = InnerWindow(outwin)
    mylabel = MyLabel(innerwin)
    outwin.show()

    sys.exit(app.exec_())