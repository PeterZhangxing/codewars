from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class MyWindow(QWidget):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setWindowTitle('test_frame')
        self.resize(500,500)
        self.init_gui()

    def init_gui(self):
        # te = QTextEdit("xxx", self)
        te = QTextEdit(self)
        self.te = te
        te.move(50, 100)
        te.resize(300, 300)
        te.setStyleSheet("background-color: cyan;")
        te.setPlaceholderText("waiting for input")

        tcf = QTextCharFormat()
        tcf.setFontFamily("宋体")
        tcf.setToolTip('input content')
        tcf.setFontPointSize(10)
        tcf.setFontCapitalization(QFont.Capitalize)
        tcf.setForeground(QColor(0, 0, 255))
        tcf.setFontOverline(True)
        tcf.setFontUnderline(True)
        te.setCurrentCharFormat(tcf)

        test_btn = QPushButton(self)
        test_btn.move(50, 10)
        test_btn.setText("测试按钮")
        test_btn.pressed.connect(self.btn_test)

    def btn_test(self):
        # 设置普通文本内容
        # self.te.setPlainText("<h1>ooo</h1>")
        # self.te.insertPlainText("<h1>ooo</h1>")
        # print(self.te.toPlainText())

        # 富文本的操作
        # self.te.setHtml("<h1>ooo</h1>")
        # self.te.insertHtml("<h6>社会我顺哥</h6>")
        # print(self.te.toHtml())
        # self.te.setText("<h1xxx>ooo</h1xxx>")
        # self.te.append("<h3>ooo</h3>")

        # self.te.setText("")
        # self.te.clear()

        # QTextDocument
        # print(self.te.document())

        # QTextCursor
        # print(self.te.textCursor)
        tetc = self.te.textCursor()
        # tetc.insertText("weight")
        # tetc.insertHtml('<h1>测试按钮</h1>')
        # tlf = QTextListFormat()
        # tlf.setIndent(3)
        # tlf.setNumberPrefix("<<")
        # tlf.setNumberSuffix(">>")
        # tlf.setStyle(QTextListFormat.ListDecimal)
        # tl = tetc.createList(tlf)
        # print(tl)

        # tif = QTextImageFormat()
        # tif.setToolTip('picture')
        # tif.setName('images/up.png')
        # tif.setWidth(20)
        # tif.setHeight(20)
        # tetc.insertImage(tif)

        # tff = QTextFrameFormat()
        # tff.setBorder(10)
        # tff.setBorderBrush(QColor(100, 50, 50))
        # tff.setRightMargin(50)
        #
        # tff1 = QTextFrameFormat()
        # tff1.setBorder(10)
        # tff1.setBorderBrush(QColor(0, 0, 255))
        # tff1.setRightMargin(50)
        #
        # doc = self.te.document()
        # root_frame = doc.rootFrame()
        # root_frame.setFrameFormat(tff1)
        #
        # tetc.insertFrame(tff)

        # tbf = QTextBlockFormat()
        # tcf = QTextCharFormat()
        # tcf.setFontFamily("隶书")
        # tcf.setFontItalic(True)
        # tcf.setFontPointSize(20)
        # tbf.setAlignment(Qt.AlignRight)
        # tbf.setRightMargin(20)
        # tbf.setIndent(3)
        # tetc.insertBlock(tbf,tcf)

        # ttf = QTextTableFormat()
        # ttf.setAlignment(Qt.AlignBottom)
        # ttf.setCellPadding(16)
        # ttf.setCellSpacing(3)
        # col_style_li = [QTextLength(QTextLength.PercentageLength,20) for i in range(9)]
        # ttf.setColumnWidthConstraints(col_style_li)
        # tetc.insertTable(5,5,ttf)

        # tcf = QTextCharFormat()
        # tcf.setFontFamily("幼圆")
        # tcf.setFontPointSize(60)
        # tcf.setFontStrikeOut(True)
        # # tetc.setCharFormat(tcf)
        # tetc.mergeCharFormat(tcf)

        tbf = QTextBlockFormat()
        tbf.setIndent(2)
        tbf.setAlignment(Qt.AlignCenter)
        tbf.setBackground(QColor(255,0,0))
        tetc.mergeBlockFormat(tbf)

if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    mywindow = MyWindow()
    mywindow.show()
    sys.exit(app.exec())