from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class MyABS(QAbstractSpinBox):
    def __init__(self,parent=None, num ="0", *args, **kwargs):
        super(MyABS, self).__init__(parent)
        self.lineEdit().setText(num)
        self.setFrame(False)

    # def stepEnabled(self):
    #     try:
    #         current_num = int(self.text())
    #         if current_num == 0:
    #             return QAbstractSpinBox.StepUpEnabled
    #         elif current_num == 9:
    #             return QAbstractSpinBox.StepDownEnabled
    #         elif current_num < 0 or current_num > 9:
    #             return QAbstractSpinBox.StepNone
    #         else:
    #             return QAbstractSpinBox.StepUpEnabled | QAbstractSpinBox.StepDownEnabled
    #     except Exception as e:
    #         self.lineEdit().setText('0')

    def stepEnabled(self):
        try:
            int(self.text())
            return QAbstractSpinBox.StepUpEnabled | QAbstractSpinBox.StepDownEnabled
        except Exception as e:
            return QAbstractSpinBox.StepNone

    def stepBy(self, p_int):
        current_num = int(self.text())+p_int
        self.lineEdit().setText(str(current_num))

    def validate(self, p_str, p_int):
        print(p_str,p_int)
        try:
            num = int(p_str)
            if num < 18:
                return (QValidator.Intermediate, p_str, p_int)
            elif num <= 180:
                return (QValidator.Acceptable, p_str, p_int)
            else:
                return (QValidator.Invalid, p_str, p_int)
        except Exception as e:
            return (QValidator.Invalid, p_str, p_int)

    def fixup(self, p_str):
        print(p_str)
        return "18"

class MyWindow(QWidget):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setWindowTitle('QKeySequenceEdit的学习')
        self.resize(500,500)
        self.init_gui()

    def init_gui(self):
        self.asb = MyABS(self)
        self.asb.resize(100,30)
        self.asb.move(100,100)

        self.asb.editingFinished.connect(lambda: print("结束编辑"))

        # print(asb.isAccelerated())
        self.asb.setAccelerated(True)
        # print(asb.isAccelerated())
        self.asb.setReadOnly(False)

        test_btn = QPushButton(self)
        test_btn.move(200, 200)
        test_btn.setText("测试按钮")
        test_btn.clicked.connect(self.btn_test)

        clear_btn = QPushButton(self)
        clear_btn.move(200, 250)
        clear_btn.setText("删除按钮")
        clear_btn.clicked.connect(self.clear_btn)

    def btn_test(self):
        cl = QCompleter(["sz", "123", "18"], self.asb)
        self.asb.lineEdit().setCompleter(cl)
        # self.asb.lineEdit().setAlignment(Qt.AlignCenter)
        self.asb.setAlignment(Qt.AlignCenter)
        # print(self.asb.hasFrame())
        self.asb.setButtonSymbols(QAbstractSpinBox.NoButtons)

    def clear_btn(self):
        self.asb.clear()
        QAbstractSpinBox.NoButtons = 1
        self.asb.setButtonSymbols(QAbstractSpinBox.NoButtons)

if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    mywindow = MyWindow()
    mywindow.show()
    sys.exit(app.exec_())