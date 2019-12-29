from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class MyWindow(QWidget):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setWindowTitle("交互状态案例的学习")
        self.resize(500, 500)
        self.init_gui()

    def init_gui(self):
        self.le1 = QLineEdit(self)
        self.le1.move(50, 50)

        self.le2 = QLineEdit(self)
        self.le2.move(100, 100)
        self.le2.setFocus()
        self.le2.setFocusPolicy(Qt.TabFocus)
        # self.le2.setFocusPolicy(Qt.ClickFocus)
        # self.le2.setFocusPolicy(Qt.StrongFocus)

        self.le3 = QLineEdit(self)
        self.le3.move(150, 150)

    def mousePressEvent(self, QMouseEvent):
        # self.focusNextPrevChild(True)
        # self.focusNextChild()
        self.focusPreviousChild()


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)

    mywindow = MyWindow()
    QWidget.setTabOrder(mywindow.le1, mywindow.le3)
    QWidget.setTabOrder(mywindow.le3, mywindow.le2)
    mywindow.show()

    sys.exit(app.exec_())