from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class MyWindow(QWidget):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.resize(300,300)
        self.setWindowTitle('test geometry')

        self.setMinimumSize(300,300)
        self.setMaximumSize(600,600)
        # self.move(0,0)
        # self.setGeometry(0,0,300,300)

        self.total_widgets = 9
        self.col = 3

        self.init_gui()

    def init_gui(self):
        my_button_width = self.width() // self.col
        total_rows = (self.total_widgets - 1) // self.col + 1
        my_button_height = self.height() // total_rows

        print(self.frameGeometry())
        # print(self.width())
        # print(self.height())
        # print(self.geometry().width())

        for i in range(self.total_widgets):
            my_btn = QPushButton(self)
            my_btn.setText('btn%d'%i)
            my_btn.setStyleSheet('background-color:grey;border:1px solid yellow;')
            my_btn_x = i % self.col * my_button_width
            my_btn_y = i // self.col * my_button_height
            my_btn.resize(my_button_width,my_button_height)
            my_btn.move(my_btn_x,my_btn_y)


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)

    mywindow = MyWindow()
    mywindow.show()
    mywindow.setGeometry(-10,-200,300,300)
    print(mywindow.frameSize())
    print(mywindow.frameGeometry())

    sys.exit(app.exec_())