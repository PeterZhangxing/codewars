from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class MyMainWindow(QMainWindow):
    def __init__(self):
        super(MyMainWindow, self).__init__()
        self.setWindowTitle("信息提示案例")
        self.resize(500,500)
        self.setWindowFlags(Qt.WindowContextHelpButtonHint)
        self.statusBar() # display status bar on the mainwindow
        self.init_gui()

    def init_gui(self):
        self.setStatusTip('this is a window')

        self.label = QLabel(self)
        self.label.setText('mother fucker')
        self.label.setToolTip('this is a label')
        self.label.setStatusTip('this is a label')
        self.label.setToolTipDuration(2000)
        self.label.setWhatsThis('this is a label')


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)

    mywindow = MyMainWindow()
    mywindow.show()

    sys.exit(app.exec_())