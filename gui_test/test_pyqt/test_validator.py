from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import re

class MyIntValidator(QIntValidator):
    def fixup(self, input):
        print(input)
        if len(input) == 0 or int(input) < 18:
            valid_age = 18
        elif int(input) > 90:
            valid_age = 90
        else:
            valid_age = int(input)
        return str(valid_age)

class MyValidator(QValidator):
    def __init__(self,start,end):
        super(MyValidator, self).__init__()
        try:
            self.start = int(start)
            self.end = int(end)
        except Exception as e:
            raise Exception('start and end must be integer numbers')

    def validate(self, input_str, pos_int):
        try:
            if self.start <= int(input_str) <= self.end:
                return (QValidator.Acceptable,input_str,pos_int)
            elif 1 <= int(input_str) < self.start:
                return (QValidator.Intermediate,input_str,pos_int)
            else:
                return (QValidator.Invalid,input_str,pos_int)
        except Exception as e:
            if len(input_str) == 0:
                return (QValidator.Intermediate,input_str,pos_int)
            return (QValidator.Invalid, input_str, pos_int)

    def fixup(self, input_str):
        try:
            if int(input_str) > self.end:
                valid_age = self.end
            elif int(input_str) < self.start:
                valid_age = self.start
            else:
                valid_age = int(input_str)
            return str(valid_age)
        except Exception as e:
            valid_age = self.start
            return str(valid_age)

class MyIpValidator(QValidator):
    def validate(self, input_str, pos_int):
        print(input_str, pos_int)
        # return (QValidator.Intermediate, input_str, pos_int)
        # return (QValidator.Invalid, input_str, pos_int)
        ip_pattern = re.compile(r"^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$")
        if not ip_pattern.match(input_str):
            return (QValidator.Invalid, input_str, pos_int)
        return (QValidator.Acceptable, input_str, pos_int)
        # count = -1
        # if pos_int >= 4:
        #     count = 0
        # if pos_int >= 8:
        #     count = 1
        # if pos_int >= 12:
        #     count = 2
        # if pos_int >= 14:
        #     count = 3
        # if count == -1:
        #     return (QValidator.Intermediate, input_str, pos_int)
        # ip_section = input_str.split('.')[count]
        # if int(ip_section) > 255:
        #     return (QValidator.Invalid, input_str, pos_int)
        # else:
        #     return (QValidator.Acceptable, input_str, pos_int)

    def fixup(self, input_str):
        print('***',input_str)
        ip_section_li = input_str.split('.')
        new_li = []
        for ip_section in ip_section_li:
            if int(ip_section) > 255:
                new_li.append(str(254))
            else:
                new_li.append(ip_section)
        return ('.'.join(new_li))

class MyWindow(QWidget):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setWindowTitle('test_validator')
        self.resize(500,500)
        self.init_gui()

    def init_gui(self):
        myeditor1 = QLineEdit(self)
        myeditor1.setText('test')
        myeditor1.setMaxLength(3)
        myeditor1.setReadOnly(True)
        myeditor1.move(100,100)

        myeditor2 = QLineEdit(self)
        myeditor2.setInputMask('>AA-9;#')
        myeditor2.move(100,150)

        myeditor3 = QLineEdit(self)
        myeditor3.setInputMask('9999-9999999;0')
        myeditor3.move(100,200)

        myintvalidator = MyIntValidator(18,90)
        myeditor4 = QLineEdit(self)
        myeditor4.setValidator(myintvalidator)
        myeditor4.move(100,250)

        myvalidator = MyValidator(22,120)
        myeditor5 = QLineEdit(self)
        myeditor5.setValidator(myvalidator)
        myeditor5.move(100,300)

        myipvalidator = MyIpValidator()
        myeditor6 = QLineEdit(self)
        myeditor6.setInputMask('999.999.999.999;0')
        myeditor6.setValidator(myipvalidator)
        myeditor6.move(100,350)

if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    mywindow = MyWindow()
    mywindow.show()
    sys.exit(app.exec())