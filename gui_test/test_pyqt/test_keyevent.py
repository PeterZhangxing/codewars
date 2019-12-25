from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class MyLabel(QLabel):
    def keyPressEvent(self, QKeyEvent):
        if QKeyEvent.key() == Qt.Key_Tab:
            print("按了Tab键")

        if QKeyEvent.modifiers() == Qt.ControlModifier and QKeyEvent.key() == Qt.Key_C:
            print("按了Ctrl+C")

        if QKeyEvent.modifiers() == Qt.ControlModifier|Qt.AltModifier and QKeyEvent.key() == Qt.Key_C:
            print("按了Ctrl+Alt+C")


class MyWindow(QWidget):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setWindowTitle('key_event')
        self.resize(500,500)
        self.init_gui()

    def init_gui(self):
        self.label = MyLabel(self)
        self.label.setText('mylabel')
        self.label.resize(200,200)
        self.label.move(150,150)
        self.label.setStyleSheet('background-color:cyan')
        self.label.grabKeyboard()


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)

    mywindow = MyWindow()
    mywindow.show()

    sys.exit(app.exec_())