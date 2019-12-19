from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class MyWindow(QWidget):

    def __init__(self):
        super(MyWindow,self).__init__()
        self.resize(350,280)
        self.setWindowTitle('这是一个好吃的积极')
        self.init_gui()

    def init_gui(self):
        self.button1 = QPushButton(self)
        self.button1.setText('push1')
        self.button1.move(10,10)
        self.button1.clicked.connect(self.change_wtitle)

    def change_wtitle(self):
        self.windowTitleChanged.connect(self.ctitle)
        self.setWindowTitle('My')

    def ctitle(self,title):
        # print(title)
        self.blockSignals(True)
        self.setWindowTitle(title+'Window1')
        self.blockSignals(False)


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    mywindow = MyWindow()
    mywindow.show()
    sys.exit(app.exec_())