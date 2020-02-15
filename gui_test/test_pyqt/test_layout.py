from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class MyWindow(QWidget):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setWindowTitle('layout的学习')
        self.resize(500, 500)
        self.init_gui()

    def init_gui(self):
        mylayout = QBoxLayout(QBoxLayout.LeftToRight)
        sublayout = QBoxLayout(QBoxLayout.TopToBottom)

        label1 = QLabel('label1')
        label1.setStyleSheet("background-color:red;")

        label2 = QLabel('label2')
        label2.setStyleSheet("background-color:blue;")

        label3 = QLabel('label3')
        label3.setStyleSheet("background-color:green;")

        label4 = QLabel('label4')
        label4.setStyleSheet("background-color:yellow;")

        label5 = QLabel('label5')
        label5.setStyleSheet("background-color:orange;")

        label6 = QLabel('label6')
        label6.setStyleSheet("background-color:grey;")

        label7 = QLabel('label_replaced')
        label7.setStyleSheet("background-color:cyan;")

        mylayout.addWidget(label1,1)
        mylayout.addWidget(label2,1)
        mylayout.addWidget(label3,1)

        sublayout.addWidget(label4,1)
        sublayout.addWidget(label5,1)
        sublayout.addWidget(label6,3)
        sublayout.replaceWidget(label4,label7)
        # label4.hide()
        label4.setParent(None)

        mylayout.insertLayout(1,sublayout)

        mylayout.insertSpacing(1,30)
        mylayout.insertStretch(2,1)
        mylayout.setContentsMargins(10,20,30,40)
        print(mylayout.contentsMargins().left())
        print(mylayout.contentsMargins().top())

        self.setLayout(mylayout)

if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    mywindow = MyWindow()
    mywindow.show()
    sys.exit(app.exec_())