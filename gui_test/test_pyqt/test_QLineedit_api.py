from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class MyWindow(QWidget):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setWindowTitle('QLineEdit功能测试')
        self.resize(500,500)
        self.init_gui()

    def init_gui(self):
        self.myle = QLineEdit(self)
        self.myle.move(100,0)

        self.le = QLineEdit(self)
        self.le.resize(200,200)
        self.le.setStyleSheet('background-color:green;')
        self.le.setAlignment(Qt.AlignBottom | Qt.AlignRight)
        self.le.move(100,100)
        # self.le.setTextMargins(50,50,50,0)
        # self.le.setContentsMargins(50, 0, 0, 0)
        self.le.setDragEnabled(True)

        # QLineEdit events
        self.le.textEdited.connect(lambda content:print('Edited',content))
        self.le.textChanged.connect(lambda content:print('Changed',content))
        self.le.returnPressed.connect(lambda :self.myle.setFocus())
        self.le.editingFinished.connect(lambda: print("结束编辑"))
        self.le.selectionChanged.connect(lambda :print(self.le.selectedText()))
        self.le.cursorPositionChanged.connect(lambda old_p,new_p:print('old_pos:',old_p,';','new_pos:',new_p))

        self.mybtn = QPushButton(self)
        self.mybtn.setText('press me')
        self.mybtn.move(100,400)
        self.mybtn.clicked.connect(self.btn_clicked)

    def btn_clicked(self):
        # self.le.cursorBackward(True, 2)
        # self.le.cursorForward(True, 3)
        # self.le.cursorWordBackward(True)
        # self.le.cursorWordForward(True)
        # self.le.home(True)
        # self.le.end(False)
        # self.le.setCursorPosition(len(self.le.text()) / 2)
        # self.le.setCursorPosition(1.5)
        # print(self.le.cursorPosition())
        # print(self.le.cursorPositionAt(QPoint(55, 105)))
        # self.le.setText("社会我顺哥"*10)
        # self.le.home(False)
        # self.le.setFocus()
        # self.le.cursorBackward(True, 2)
        # self.le.backspace()
        # self.le.del_()
        # self.le.clear()
        # self.le.setText("")
        # self.le.setFocus()

        # self.le.cursorBackward(True, 3)
        # # le.copy()
        # self.le.cut()
        # self.le.setCursorPosition(0)
        # self.le.paste()
        # self.le.end(False)

        # self.le.setSelection(0,3) # start from position 0 select 3 characters
        # self.le.selectAll()
        # self.le.setSelection(0, len(self.le.text()))
        # self.le.deselect()

        self.le.setSelection(2, 3)
        print(self.le.hasSelectedText())

        print(self.le.selectedText())
        print(self.le.selectionStart())
        print(self.le.selectionEnd())
        print(self.le.selectionLength())
        '''
        True
        321
        2
        5
        3
        '''

if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    mywindow = MyWindow()
    mywindow.show()
    sys.exit(app.exec())