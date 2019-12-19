import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class MyColorDialog(QWidget):

    def __init__(self,parent=None):
        super(MyColorDialog, self).__init__(parent)
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('MyColorDialog')
        self.resize(200,300)

        mylayout = QVBoxLayout()

        self.color_button = QPushButton('设置颜色')
        self.color_button.clicked.connect(self.getcolor)
        mylayout.addWidget(self.color_button)

        self.color_button1 = QPushButton('设置背景颜色')
        self.color_button1.clicked.connect(self.getbgcolor)
        mylayout.addWidget(self.color_button1)

        self.color_label = QLabel()
        self.color_label.setText('Hello，测试颜色例子')
        mylayout.addWidget(self.color_label)

        self.setLayout(mylayout)

    def getcolor(self):
        color = QColorDialog.getColor()
        p = QPalette()
        p.setColor(QPalette.Window,color)

        self.color_label.setPalette(p)

    def getbgcolor(self):
        color = QColorDialog.getColor()
        p = QPalette()
        p.setColor(QPalette.Window,color)

        self.color_label.setAutoFillBackground(True)
        self.color_label.setPalette(p)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mywindow = MyColorDialog()
    mywindow.show()
    sys.exit(app.exec_())