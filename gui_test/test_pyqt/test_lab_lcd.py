from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class MyWindow(QWidget):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setWindowTitle('QDialog的学习')
        self.resize(500, 500)
        # self.init_label_gui()
        # self.init_lcd_gui()
        self.init_pbar_gui()

    def init_label_gui(self):
        label = QLabel(self)
        # label = QLabel("label_content", self)
        # label = QLabel("账号(&s):", self)
        # label = QLabel("<a href='http://www.baidu.com'>baidu</a>", self)
        # label = QLabel("123 456 789 " * 6, self)
        # label = QLabel("\n".join("123456789"), self)
        label.setStyleSheet("background-color: red;")
        label.move(10, 100)
        label.resize(100, 300)
        # label.adjustSize()

        # label.setOpenExternalLinks(True)
        label.setWordWrap(True)
        # label.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        label.setAlignment(Qt.AlignRight)
        # label.setMargin(15)
        # label.setIndent(15)
        label.setScaledContents(True)

        # pic = QPicture()
        # painter = QPainter(pic)
        # painter.setBrush(QBrush(QColor(0,255,0)))
        # painter.drawEllipse(0,0,5,5)
        # label.setPicture(pic)

        # label.setPixmap(QPixmap('images/dog.jpg'))

        # label.setTextFormat(Qt.PlainText)
        # label.setTextInteractionFlags(Qt.TextSelectableByMouse | Qt.TextSelectableByKeyboard | Qt.TextEditable)
        # label.setSelection(1,2)

        # label.setText("<img src='images/dog2.jpg' width=60 height=60>")
        label.setText("hehe<a href='http://www.itlike.com'>撩课</a>")
        # label.setNum(888.88)

        # movie = QMovie("shulan.gif")
        # label.setMovie(movie)
        # movie.start()
        # movie.setSpeed(1000)

        # label.clear()

        le1 = QLineEdit(self)
        le1.move(250, 250)

        le2 = QLineEdit(self)
        le2.move(250, 300)

        label.setBuddy(le1)

        label.linkHovered.connect(lambda a:print("linkHovered:",a))
        label.linkActivated.connect(lambda a:print("linkActivated:",a))

    def init_lcd_gui(self):
        lcd = QLCDNumber(self)
        lcd.move(0, 0)
        lcd.resize(300, 100)

        lcd.setDigitCount(2)
        lcd.setMode(QLCDNumber.Hex)

        print(lcd.checkOverflow(99))
        print(lcd.checkOverflow(100))

        lcd.overflow.connect(lambda :print("数值溢出"))
        lcd.display(99)

        lcd2 = QLCDNumber(self)
        lcd2.move(0, 100)
        lcd2.resize(300, 100)

        lcd3 = QLCDNumber(2,self)
        lcd3.move(0, 200)
        lcd3.resize(300, 100)

        lcd2.display(99)
        lcd3.display(99.32)

        lcd.setSegmentStyle(QLCDNumber.Outline)
        lcd2.setSegmentStyle(QLCDNumber.Filled)
        lcd3.setSegmentStyle(QLCDNumber.Flat)
        self.lcd3 = lcd3

        btn = QPushButton(self)
        btn.setText("测试按钮")
        btn.move(100, 450)
        btn.clicked.connect(self.lcd_get)

    def lcd_get(self):
        print(self.lcd3.value())
        print(self.lcd3.intValue())

    def init_pbar_gui(self):
        pb = QProgressBar(self)
        self.pb = pb
        pb.resize(400,50)
        pb.move(50,50)
        pb.valueChanged.connect(lambda val: print("当前的进度值为", val))
        # pb.setRange(0,200)
        # pb.setRange(0,0)
        # pb.setMaximum(1000)
        # print(pb.minimum())
        # print(pb.maximum())
        # pb.setValue(90)
        pb.setFormat("now %v/total %m %p%")
        pb.setAlignment(Qt.AlignRight | Qt.AlignHCenter)

        btn = QPushButton(self)
        btn.move(200, 200)
        btn.setText("测试按钮")
        btn.clicked.connect(self.test_pb)

        timebtn = QPushButton(self)
        timebtn.move(200, 250)
        timebtn.setText("测试timer")
        timebtn.clicked.connect(self.start_pb)

    def start_pb(self):
        self.mytimer = QTimer(self.pb)
        self.mytimer.timeout.connect(self.start_mytimer)
        self.mytimer.start(500)

    def start_mytimer(self):
        if self.pb.value() == self.pb.maximum():
            self.mytimer.stop()
            return
        self.pb.setValue(self.pb.value() + 1)

    def test_pb(self):
        # self.pb.setInvertedAppearance(True)
        # self.pb.setOrientation(Qt.Vertical)
        # self.pb.setTextDirection(QProgressBar.TopToBottom)
        # self.pb.resize(40,400)
        # print(self.pb.isTextVisible())
        print(self.pb.format())
        self.pb.reset()
        if self.pb.format() == "now %v/total %m %p%":
            self.pb.resetFormat()
        else:
            self.pb.setFormat("now %v/total %m %p%")

if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    mywindow = MyWindow()
    mywindow.show()
    sys.exit(app.exec_())