from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class MyWindow(QWidget):

    def __init__(self):
        super(MyWindow, self).__init__()
        self.resize(300,300)
        self.setWindowTitle('test_timer')
        self.init_gui()

    def init_gui(self):
        mystyle = QVBoxLayout()

        self.timer =QTimer()
        self.timer.timeout.connect(self.set_label_content)

        self.timer_lable = QLabel(self)
        self.timer_lable.setText('show current time')
        mystyle.addWidget(self.timer_lable)

        self.start_timer_buton = QPushButton(self)
        self.start_timer_buton.setText('start')
        self.start_timer_buton.clicked.connect(self.start_timer)
        mystyle.addWidget(self.start_timer_buton)

        self.stop_timer_buton = QPushButton(self)
        self.stop_timer_buton.setText('stop')
        self.stop_timer_buton.clicked.connect(self.stop_timer)
        mystyle.addWidget(self.stop_timer_buton)

        self.setLayout(mystyle)

    def set_label_content(self):
        self.timer_lable.setText(QDateTime.currentDateTime().toString("yyyy-MM-dd hh:mm:ss dddd"))

    def start_timer(self):
        self.timer.start(1000)
        self.start_timer_buton.setEnabled(False)
        self.stop_timer_buton.setEnabled(True)

    def stop_timer(self):
        self.timer.stop()
        self.start_timer_buton.setEnabled(True)
        self.stop_timer_buton.setEnabled(False)


class MyButton(QPushButton):

    def __init__(self,*args,**kwargs):
        super(MyButton,self).__init__(*args,**kwargs)
        self.setText('10')
        self.move(100,100)
        self.setStyleSheet("font-size:30px;")
        self.timer_id = self.startTimer(1000)

    def timerEvent(self, tevent):
        string = self.text()
        int_str = int(string) - 1
        self.setText(str(int_str))

        if int_str == 0:
            self.setText('Over')
            self.killTimer(self.timer_id)


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    # mywindow = MyWindow()
    # mywindow.show()

    test_window = QWidget()
    test_window.resize(600,300)
    mylabel = MyButton(test_window)
    test_window.show()

    sys.exit(app.exec_())