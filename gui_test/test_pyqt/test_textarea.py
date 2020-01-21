from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class MyTextEdit(QTextEdit):
    def mousePressEvent(self, me):
        # QMouseEvent
        print(me.pos())
        link_addr = self.anchorAt(me.pos())
        print(link_addr)
        if link_addr:
            QDesktopServices.openUrl(QUrl(link_addr))
        return super(MyTextEdit, self).mousePressEvent(me)

class MyWindow(QWidget):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setWindowTitle('test_frame')
        self.resize(500,500)
        self.init_gui()

    def init_gui(self):
        # te = QTextEdit("xxx", self)
        te = MyTextEdit(self)
        self.te = te
        te.move(50, 100)
        te.resize(300, 300)
        te.setStyleSheet("background-color: cyan;")
        te.setPlaceholderText("waiting for input")
        te.insertHtml("xxx " * 300 + "<a name='itcast' href='http://www.baidu.com'>撩课</a>" + "aaa" * 200)

        tcf = QTextCharFormat()
        tcf.setFontFamily("宋体")
        tcf.setToolTip('input content')
        tcf.setFontPointSize(10)
        # tcf.setFontCapitalization(QFont.Capitalize)
        tcf.setForeground(QColor(0, 0, 255))
        tcf.setFontOverline(True)
        tcf.setFontUnderline(True)
        te.setCurrentCharFormat(tcf)

        test_btn = QPushButton(self)
        test_btn.move(50, 10)
        test_btn.setText("测试按钮")
        test_btn.pressed.connect(self.btn_test)

        self.te.textChanged.connect(self.text_change)
        self.te.selectionChanged.connect(self.selection_change)
        self.te.copyAvailable.connect(self.copy_a)

    def text_change(self):
        print("文本内容发生了改变")

    def selection_change(self):
        print("文本选中的内容发生了改变")

    def copy_a(self, changed):
        print("复制是否可用", changed)

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

        # tbf = QTextBlockFormat()
        # tbf.setIndent(2)
        # tbf.setAlignment(Qt.AlignCenter)
        # tbf.setBackground(QColor(255,0,0))
        # tetc.mergeBlockFormat(tbf)

        # print("是否在段落的结尾:", tetc.atBlockEnd())
        # print("是否在段落的开始:", tetc.atBlockStart())
        # print("是否在文档的结尾:", tetc.atEnd())
        # print("是否在文档的开始:", tetc.atStart())
        #
        # print("在第几列", tetc.columnNumber())
        # print("光标位置", tetc.position())
        # print("在文本块中的位置", tetc.positionInBlock())

        # tetc.deleteChar()
        # tetc.deletePreviousChar()

        # print(tetc.selectionStart())
        # print(tetc.selectionEnd())
        # # tetc.clearSelection()
        # self.te.setTextCursor(tetc)
        # print(tetc.hasSelection())
        # tetc.removeSelectedText()
        # self.te.setFocus()

        # print(tetc.selectedText())
        # print(tetc.selection().toPlainText())
        # print(tetc.blockNumber())
        # print(tetc.block().text())
        # self.te.setFocus()

        # tetc.setPosition(6, QTextCursor.KeepAnchor)
        # tetc.movePosition(QTextCursor.Up, QTextCursor.KeepAnchor, 2)
        # tetc.select(QTextCursor.WordUnderCursor)
        # self.te.setTextCursor(tetc)
        # self.te.setFocus()

        # self.te.setAutoFormatting(QTextEdit.AutoBulletList)

        # self.te.setLineWrapMode(QTextEdit.NoWrap)
        # self.te.setLineWrapMode(QTextEdit.FixedPixelWidth)
        # self.te.setLineWrapMode(QTextEdit.FixedColumnWidth)
        # self.te.setLineWrapColumnOrWidth(8)
        # self.te.setOverwriteMode(True)

        # self.mytextcursor()

        # self.te.setFontFamily("幼圆")
        # self.te.setFontWeight(QFont.Black)
        # self.te.setFontItalic(True)
        # self.te.setFontPointSize(20)
        # self.te.setFontUnderline(True)
        #
        # self.te.setTextBackgroundColor(QColor(255, 0, 0))
        # self.te.setTextColor(QColor(0, 0, 255))
        #
        # myfont = QFont()
        # myfont.setStrikeOut(True)
        # self.te.setCurrentFont(myfont)

        # tcf = QTextCharFormat()
        # tcf.setFontFamily("宋体")
        # tcf.setFontPointSize(20)
        # tcf.setFontCapitalization(QFont.Capitalize)
        # tcf.setForeground(QColor(100, 200, 150))
        # self.te.setCurrentCharFormat(tcf)
        #
        # tcf2 = QTextCharFormat()
        # tcf2.setBackground(QColor(0,255,0))
        # tcf2.setFontStrikeOut(True)
        # self.te.mergeCurrentCharFormat(tcf2)

        # self.te.find('xx',QTextDocument.FindBackward|QTextDocument.FindCaseSensitively|QTextDocument.FindWholeWords)
        # self.te.setFocus()

        # self.te.scrollToAnchor('itcast')

        # self.te.setReadOnly(True)
        # self.te.insertPlainText("itlike")
        # print(self.te.isReadOnly())

        # self.te.setTabChangesFocus(True)
        print(self.te.tabStopDistance())
        print(self.te.tabStopWidth())
        self.te.setTabStopDistance(100)

    def mytextcursor(self):
        if self.te.cursorWidth() > 1:
            self.te.setCursorWidth(1)
            self.te.setOverwriteMode(False)
        else:
            self.te.setCursorWidth(8)
            self.te.setOverwriteMode(True)
        self.te.setFocus()

if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    mywindow = MyWindow()
    mywindow.show()
    sys.exit(app.exec())