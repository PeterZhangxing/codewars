from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class MyWindow(QWidget):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setWindowTitle('background_learning')
        self.resize(800, 800)
        self.init_gui()

    def init_gui(self):
        common_stylesheet = """
        QPushButton {
            background-image: url(../images/source/puke.png);
            border-image: url(../images/source/border_test.png) 30px round;
            border-width: 30px;
            background-origin: content;
            background-clip: padding;
        }
        """
        self.setStyleSheet(common_stylesheet)
        v_layout = QVBoxLayout()
        self.setLayout(v_layout)
        for j in range(5):
            h_layout = QHBoxLayout()
            v_layout.addLayout(h_layout)
            end_num = 14
            if j == 4:
                end_num = 3
            for i in range(1,end_num):
                btn = QPushButton()
                btn.setFixedSize(109, 126)
                btn_stylesheet = """
                QPushButton {
                    padding-left: -%dpx;
                    padding-top: -%dpx;
                }
                """%((i-1)*49,j*66)
                btn.setStyleSheet(btn_stylesheet)
                h_layout.addWidget(btn)

if __name__ == '__main__':
    import sys
    # from imqssf_tool import QssFileDealer

    app = QApplication(sys.argv)
    # QssFileDealer.set_app_qss(app,'qssfile1.qss')
    mywindow = MyWindow()
    mywindow.show()
    sys.exit(app.exec_())