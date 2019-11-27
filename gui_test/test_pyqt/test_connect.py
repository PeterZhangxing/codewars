import sys
from PyQt5.QtWidgets import QMainWindow,QApplication,QPushButton,QVBoxLayout,QDialog,QWidget
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import *


class MyWindow(QWidget):

    def __init__(self):
        QMainWindow.__init__(self)
        # super(MyWindow, self).__init__()
        self.init_gui()

    def init_gui(self):
        self.setWindowTitle("my first main window")

        layout = QVBoxLayout()

        self.mybotton = QPushButton('push me')
        # self.mybotton.setFixedSize(120,50)
        self.mybotton.setGeometry(QRect(10,20,120,50))
        # print(self.mybotton.size().width())
        # self.mybotton.setDisabled(True)
        self.mybotton.move(10,10)
        self.mybotton.clicked.connect(self.mymove)

        layout.addWidget(self.mybotton)

        # self.pushButton = QPushButton('sdsad')
        # self.pushButton.setGeometry(QRect(150, 200, 75, 23))
        # self.pushButton.setObjectName("pushButton")

        self.setLayout(layout)
        self.resize(800, 700)

    def mymove(self):

        x = self.mybotton.x()
        y = self.mybotton.y()

        x += 30
        y += 20

        self.mybotton.move(x,y)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    mainwin = MyWindow()
    mainwin.show()

    sys.exit(app.exec_())