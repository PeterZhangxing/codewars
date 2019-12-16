import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class MyDialog(QMainWindow):

    def __init__(self):
        super(MyDialog,self).__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('MyDialog')
        self.resize(300,200)
        self.move(300,300)

        self.button = QPushButton(self)
        self.button.setText('弹出对话框')
        self.button.move(50,50)
        self.button.clicked.connect(self.show_my_dialog)

    def show_my_dialog(self):
        dialog = QDialog()
        dialog.move(300,300)

        button = QPushButton('OK',dialog)
        button.clicked.connect(dialog.close)

        button.move(50,50)
        dialog.setWindowTitle('dialog')
        dialog.setWindowModality(Qt.ApplicationModal)

        dialog.exec_()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mywindow = MyDialog()
    mywindow.show()
    sys.exit(app.exec())