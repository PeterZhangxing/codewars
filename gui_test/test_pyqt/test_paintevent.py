from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

# class MyWindow(QWidget):
#     def paintEvent(self, QPaintEvent):
#         print('paint window')
#         return super(MyWindow, self).paintEvent(QPaintEvent)
#
# class MyBtn(QPushButton):
#     def paintEvent(self, QPaintEvent):
#         print('paint button')
#         return super(MyBtn, self).paintEvent(QPaintEvent)
#
#
# if __name__ == '__main__':
#     import sys
#     import time
#
#     app = QApplication(sys.argv)
#
#     mywindow = MyWindow()
#     mywindow.setWindowTitle("交互状态")
#     mywindow.resize(500, 500)
#
#     mybtn = MyBtn(mywindow)
#     mybtn.setText("按钮")
#     mybtn.destroyed.connect(lambda: print('mybtn has been deleted'))
#     mybtn.pressed.connect(lambda :mybtn.setEnabled(False))
#
#     mybtn1 = MyBtn(mywindow)
#     mybtn1.setText("按钮1")
#     mybtn1.pressed.connect(lambda :mybtn1.hide())
#     mybtn1.move(200, 0)
#
#     mybtn2 = MyBtn(mywindow)
#     mybtn2.setText("按钮2")
#     mybtn2.pressed.connect(lambda :mybtn2.setHidden(True))
#     mybtn2.move(400, 0)
#
#     mybtn3 = MyBtn(mywindow)
#     mybtn3.setText("按钮3")
#     mybtn3.destroyed.connect(lambda: print('mybtn3 has been deleted'))
#     mybtn3.setAttribute(Qt.WA_DeleteOnClose, True)
#     mybtn3.pressed.connect(lambda :mybtn3.close())
#     mybtn3.move(0, 50)
#
#     mywindow.show()
#
#     # time.sleep(2)
#     # mybtn.deleteLater()
#
#     sys.exit(app.exec_())

class MyWindow(QWidget):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setWindowTitle("交互状态案例的学习")
        self.resize(500, 500)
        self.init_gui()

    def init_gui(self):
        self.label = QLabel(self)
        self.label.setText('标签')
        self.label.move(100,50)
        self.label.hide()

        self.myle = QLineEdit(self)
        self.myle.move(100,100)
        self.myle.textChanged.connect(self.change_line_text)

        self.mybtn = QPushButton(self)
        self.mybtn.setText("登录")
        self.mybtn.move(100, 150)
        self.mybtn.setEnabled(False)
        self.mybtn.pressed.connect(self.check_cotent)

    def change_line_text(self,text):
        self.mybtn.setEnabled(len(text)>0)

    def check_cotent(self):
        content = self.myle.text()
        if content == 'redhat':
            self.label.setText('登录成功')
        else:
            self.label.setText('登录失败')

        self.label.adjustSize()
        self.label.show()

if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)

    mywindow = MyWindow()
    mywindow.show()
    
    sys.exit(app.exec_())