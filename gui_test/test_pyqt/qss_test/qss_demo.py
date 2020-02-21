from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class MyWindow(QWidget):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setWindowTitle('background_learning')
        self.resize(500, 500)
        self.init_gui()

    def init_gui(self):
        # btn = QPushButton(self)
        # btn.setText('test_btn')
        # btn.resize(200,150)
        # btn.move(150,200)

        # rdb = QRadioButton(self)
        # rdb.setText('test_radiobtn')
        # rdb.resize(190,100)
        # rdb.move(150,200)

        # le = QLineEdit(self)
        # le.setText('test line editor')
        # le.resize(300,400)
        # le.move(20,10)
        # # le.setEchoMode(QLineEdit.Password)
        # le.setReadOnly(True)

        # te = QTextEdit('this is a test of text edit',self)
        # te.resize(300,400)
        # te.move(20,10)

        # sb = QSpinBox(self)
        # sb.resize(300,60)
        # sb.move(20,10)

        # cb = QComboBox(self)
        # cb.setEditable(True)
        # cl = QCompleter(['python','c++','java','PHP','jsp'],cb)
        # cb.setCompleter(cl)
        # cb.addItems(['python','c++','java','PHP','jsp'])
        # cb.resize(200,60)
        # cb.move(20,10)

        # sl = QSlider(Qt.Horizontal,self)
        # sl.resize(300,16)
        # sl.move(20,10)
        # sl.valueChanged.connect(lambda val:print(val))

        pb = QProgressBar(self)
        pb.resize(400,40)
        pb.move(10,100)
        pb.setValue(60)

if __name__ == '__main__':
    import sys
    from imqssf_tool import QssFileDealer

    app = QApplication(sys.argv)
    QssFileDealer.set_app_qss(app,'qss_demo.qss')
    mywindow = MyWindow()
    mywindow.show()
    sys.exit(app.exec_())