from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from resources.calculator_ui import Ui_Form
from cal_utils import Calculator

class CalculatorPanel(QWidget,Ui_Form):

    def __init__(self, parent=None, *args, **kwargs):
        super(CalculatorPanel, self).__init__(parent, *args, **kwargs)
        self.setAttribute(Qt.WA_StyledBackground,True)
        self.setupUi(self)
        self.mycal = Calculator(self)
        self.mycal.show_content.connect(self.show_content)

    def get_key(self,title,role):
        # print('get_key:',title,role)
        self.mycal.parse_key_model({'title':title,'role':role})

    def show_content(self,content):
        self.lineEdit.setText(content)

if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    window = CalculatorPanel()
    window.show()

    sys.exit(app.exec_())