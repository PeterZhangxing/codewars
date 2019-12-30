from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class MyWindow(QWidget):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setWindowTitle("按钮的功能测试-抽象类")
        self.resize(500,500)

        self.init_pbtn()
        self.init_rbtn()
        self.init_cbtn()

    def paintEvent(self, QPaintEvent):
        self.painter = QPainter(self)

        self.painter.begin(self)

        self.pen = QPen(QColor(0,255,0),3)
        self.painter.setPen(self.pen)
        self.draw_text()
        self.painter.drawEllipse(100, 300, 200, 100)
        
        self.painter.end()

    def draw_text(self):
        self.painter.setFont(QFont('Decorative', 30))
        self.painter.drawText(250, 300, 'TEST')

    def init_rbtn(self):
        for i in range(3):
            self.rbtn = QRadioButton(self)
            self.rbtn.setText('radio_btn_%d'%i)
            self.rbtn.setAutoExclusive(False)
            self.rbtn.setCheckable(True)
            self.rbtn.setDown(True)
            self.rbtn.move(i*120,0)

    def init_cbtn(self):
        for i in range(3):
            self.cbtn = QCheckBox(self)
            self.cbtn.setText('check_btn_%d'%i)
            self.cbtn.setAutoExclusive(False)
            self.cbtn.setCheckable(True)
            self.cbtn.setDown(True)
            self.cbtn.setChecked(True)
            self.cbtn.move(i*120,100)

    def init_pbtn(self):
        self.btn = QPushButton(self)
        self.btn.setText("1")
        self.btn.pressed.connect(self.press_btn)

        self.btn.setAutoRepeat(True)
        self.btn.setAutoRepeatInterval(50)
        self.btn.setAutoRepeatDelay(1000)

        btnicon = QIcon('images/cartoon2.ico')
        self.btn.setIcon(btnicon)

        btnsize = QSize(64,64)
        self.btn.setIconSize(btnsize)

        self.btn.setShortcut("Alt+a")
        # self.btn.setDown(True)
        self.btn.setCheckable(True)

        self.btn.move(200,200)

    def press_btn(self):
        count = int(self.btn.text()) + 1
        self.btn.adjustSize()
        self.btn.setText(str(count))

    def mousePressEvent(self, QMouseEvent):
        print(QMouseEvent.pos())
        self.btn.toggle()
        rbtns = self.findChildren(QRadioButton)
        for rbtn in rbtns:
            rbtn.toggle()

        cbtns = self.findChildren(QCheckBox)
        for cbtn in cbtns:
            cbtn.toggle()


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)

    mywindow = MyWindow()
    # mywindow.draw_pic()
    mywindow.show()

    sys.exit(app.exec_())