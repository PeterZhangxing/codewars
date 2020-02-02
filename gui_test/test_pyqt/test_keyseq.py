from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class MyWindow(QWidget):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setWindowTitle('QKeySequenceEdit的学习')
        self.resize(500,500)
        self.init_gui()

    def init_gui(self):
        kse = QKeySequenceEdit(self)
        # ks = QKeySequence(QKeySequence.Copy)
        # ks = QKeySequence(Qt.CTRL + Qt.Key_C, Qt.CTRL + Qt.Key_A)
        ke = QKeySequence("Ctrl+C")
        kse.setKeySequence(ke)

        btn = QPushButton(self)
        btn.move(100, 100)
        btn.setText("测试按钮")
        btn.clicked.connect(lambda :print(kse.keySequence().toString(), kse.keySequence().count()))

        kse.editingFinished.connect(lambda :print('finishing editing'))
        kse.keySequenceChanged.connect(lambda key_val:print("键位序列发生改变",key_val.toString()))


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    mywindow = MyWindow()
    mywindow.show()
    sys.exit(app.exec_())