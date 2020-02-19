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
        mycb = QCheckBox("复选框", self)
        mycb.resize(200, 100)
        mycb.move(0, 0)

        mysb = QSpinBox(self)
        mysb.resize(200,100)
        mysb.move(0,200)

        mycb_stylesheet = """
        QCheckBox {
            color: gray;    
            border: 10px double rgb(0, 0, 255);
            padding: 50px;
        }
 
        QCheckBox::indicator {
            subcontrol-origin: content;
            subcontrol-position: left center;
            background: white;
            border: 2px solid gray;
        }
 
        QCheckBox::indicator:checked {
            background: rgb(255, 0, 0);
        }
        """
        mycb.setStyleSheet(mycb_stylesheet)

        mysb_stylesheet = """
        QSpinBox {
            font-size: 26px;
            font-family: 隶书;
            font-style: italic;
            font-weight: 900;
            color: orange;
            border: 10px double red;
            border-radius: 20px;
            background-color: lightgray;
        }
        QSpinBox::up-button, QSpinBox::down-button {
            width: 50px;
            height: 80px;
        }
        
        QSpinBox::up-button {
            subcontrol-origin: padding;
            subcontrol-position:left center;
            image: url(../images/source/up.png)
        }
        QSpinBox::up-button:hover {
            bottom: 10px;
        }
        
        QSpinBox::down-button {
            subcontrol-origin: padding;
            subcontrol-position:right center;
            image: url(../images/source/down.png)
        }
        QSpinBox::down-button:hover {
            top: 10px;
        }
        """
        mysb.setStyleSheet(mysb_stylesheet)

if __name__ == '__main__':
    import sys
    # from imqssf_tool import QssFileDealer

    app = QApplication(sys.argv)
    # QssFileDealer.set_app_qss(app,'qssfile1.qss')
    mywindow = MyWindow()
    mywindow.show()
    sys.exit(app.exec_())