from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class MyWindow(QWidget):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setWindowTitle('test_plaintext')
        self.resize(500,500)
        self.init_gui()

    def init_gui(self):
        self.pte = QPlainTextEdit(self)
        self.pte.resize(300,300)
        self.pte.move(100,100)

        tcf = QTextCharFormat()
        tcf.setFontUnderline(True)
        tcf.setUnderlineColor(QColor(200, 100, 100))
        self.pte.setCurrentCharFormat(tcf)
        self.pte.setLineWrapMode(QPlainTextEdit.NoWrap)
        self.pte.setPlaceholderText('input here')
        self.pte.setTabChangesFocus(False)
        self.pte.setTabStopDistance(100)

        self.pte.setCenterOnScroll(True)
        self.pte.ensureCursorVisible()
        self.pte.setOverwriteMode(True)
        print(self.pte.blockCount())

        test_btn = QPushButton(self)
        test_btn.move(20, 20)
        test_btn.setText("测试按钮")
        test_btn.clicked.connect(self.btn_test)

        line_num_parent = QWidget(self)
        line_num_parent.resize(30, 300)
        line_num_parent.move(70, 100)
        line_num_parent.setStyleSheet("background-color: cyan;")

        self.line_num = QLabel(line_num_parent)
        self.line_num.move(0, 5)

        nums = [ str(i) for i in range(1,101) ]
        nums_content = '\n'.join(nums)
        self.line_num.setText(nums_content)
        self.line_num.adjustSize()

    def btn_test(self):
        # QTextCursor
        # QTextCursor.MoveOperation
        QTextCursor.MoveMode
        # self.pte.updateRequest.connect(lambda rect,dy:print(dy))
        self.pte.updateRequest.connect(lambda rect,dy:self.line_num.move(self.line_num.x(),self.line_num.y()+dy))
        tc = self.pte.textCursor()
        # tc = self.pte.cursorForPosition(QPoint(20, 60))
        tc.insertText('xxx')
        tc_pos = tc.position()
        # print(tc_pos,type(tc_pos))
        tc.setPosition(10,QTextCursor.KeepAnchor)
        self.pte.setTextCursor(tc)
        # self.pte.moveCursor(QTextCursor.StartOfBlock, QTextCursor.KeepAnchor)
        # self.pte.moveCursor(QTextCursor.StartOfBlock, QTextCursor.MoveAnchor)
        self.pte.setFocus()
        print(tc_pos, type(tc_pos))


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    mywindow = MyWindow()
    mywindow.show()
    sys.exit(app.exec_())