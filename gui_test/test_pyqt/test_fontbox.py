from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class MyWindow(QWidget):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setWindowTitle("QFontComboBox的学习")
        self.resize(500, 500)
        self.init_gui()

    def init_gui(self):
        myfcb = QFontComboBox(self)
        myfcb.setEditable(False)

        mylab = QLabel(self)
        self.mylab = mylab
        mylab.move(100,100)
        # mylab.resize(150,30)
        mylab.setText("love学习love学习love学习")
        mylab.adjustSize()

        # myfcb.currentFontChanged.connect(lambda fontpbj:mylab.setFont(fontpbj))
        myfcb.currentFontChanged.connect(self.font_changed)

    def font_changed(self,font_obj):
        self.mylab.setFont(font_obj)
        self.mylab.adjustSize()

if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    mywindow = MyWindow()
    mywindow.show()
    sys.exit(app.exec_())