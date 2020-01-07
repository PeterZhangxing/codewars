from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class MyWindow(QWidget):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setWindowTitle('test_checkbox')
        self.resize(500,500)
        self.init_gui()

    def init_gui(self):
        cbx1 = QCheckBox(self)
        cbx1.setText('fucking')
        cbx1.setIcon(QIcon('images/left.png'))
        cbx1.setIconSize(QSize(20,20))
        cbx1.setCheckState(Qt.PartiallyChecked)
        cbx1.move(10,100)
        cbx1.setTristate(True)

        cbx2 = QCheckBox(self)
        cbx2.setText('basketball')
        cbx2.setIcon(QIcon('images/right.png'))
        cbx2.setIconSize(QSize(20, 20))
        cbx2.setCheckState(Qt.Checked)
        cbx2.move(cbx1.width()+cbx1.x()+50,100)
        cbx2.setTristate(True)

        cbx3 = QCheckBox(self)
        cbx3.setText('football')
        cbx3.setIcon(QIcon('images/up.png'))
        cbx3.setIconSize(QSize(20, 20))
        cbx3.setCheckState(Qt.Unchecked)
        cbx3.move(cbx2.width() + cbx2.x() +50, 100)
        cbx3.setTristate(True)

        self.cbxg = QButtonGroup(self)
        self.cbxg.addButton(cbx1,1)
        self.cbxg.addButton(cbx2,2)
        self.cbxg.addButton(cbx3,3)
        self.cbxg.buttonClicked.connect(lambda btn:print(self.cbxg.id(btn)))
        self.cbxg.buttonClicked.connect(lambda btn:print(self.cbxg.checkedButton()))

if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)

    mywindow = MyWindow()
    mywindow.show()

    sys.exit(app.exec())