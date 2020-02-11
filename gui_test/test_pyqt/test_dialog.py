from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class MyWindow1(QWidget):
    def __init__(self):
        super(MyWindow1, self).__init__()
        self.setWindowTitle('QDialog的学习')
        self.resize(500, 500)
        self.init_gui()

    def init_gui(self):
        btn = QPushButton(self)
        btn.setText("show window")
        btn.move(120, 120)

        d = QDialog(self)

        d.accepted.connect(lambda: print("点击了, 接受按钮"))
        d.rejected.connect(lambda: print("点击了, 拒绝按钮"))
        d.finished.connect(lambda val: print("点击了, 完成按钮", val))

        btn1 = QPushButton(d)
        btn1.setText("btn1")
        btn1.move(20, 20)
        btn1.clicked.connect(lambda: d.accept())

        btn2 = QPushButton(d)
        btn2.setText("btn2")
        btn2.move(60, 60)
        btn2.clicked.connect(lambda: d.reject())
        # btn2.clicked.connect(lambda :print(d.result()))

        btn3 = QPushButton(d)
        btn3.setText("btn3")
        btn3.move(60, 160)
        btn3.clicked.connect(lambda: d.done(8))
        # btn3.clicked.connect(lambda :d.setResult(888))

        # d.setModal(True)
        # d.setWindowModality(Qt.WindowModal)
        # d.setSizeGripEnabled(True)
        # d.open()
        # d.show()
        self.d = d

        btn.clicked.connect(self.show_dialog)

    def show_dialog(self):
        # self.d.setModal(True)
        self.d.setWindowModality(Qt.WindowModal)
        self.d.setSizeGripEnabled(True)
        self.d.show()

class MyWindow2(QWidget):
    def __init__(self):
        super(MyWindow2, self).__init__()
        self.setWindowTitle('QDialog的学习')
        self.resize(500, 500)
        self.init_gui()

    def init_gui(self):
        fd = QFontDialog(self)
        self.fd = fd
        font = QFont()
        self.font = font
        font.setFamily("宋体")
        font.setPointSize(36)
        # fd.setCurrentFont(font)
        # fd.setOptions(QFontDialog.NoButtons | QFontDialog.MonospacedFonts)
        # fd.setOption(QFontDialog.NoButtons)
        # print(fd.testOption(QFontDialog.MonospacedFonts))
        # print(fd.testOption(QFontDialog.ScalableFonts))

        btn = QPushButton(self)
        btn.setText("按钮")
        btn.move(100, 100)
        btn.clicked.connect(self.font_sel)

        label = QLabel(self)
        self.lab = label
        label.move(200, 100)
        label.setText("test font")

    def cfc(self,myfont):
        print(myfont.family())
        print("字体已经被选择", self.fd.selectedFont().family())
        self.lab.setFont(myfont)
        self.lab.adjustSize()

    def font_sel(self):
        self.fd.fontSelected.connect(self.cfc)
        # self.fd.currentFontChanged.connect(self.cfc)
        self.fd.show()

        # result = QFontDialog.getFont(self)
        # result = QFontDialog.getFont(self.font,self,"选择一个好看的字体")
        # if result[1]:
        #     self.lab.setFont(result[0])
        #     self.lab.adjustSize()

class MyWindow3(QWidget):
    def __init__(self):
        super(MyWindow3, self).__init__()
        self.setWindowTitle('QDialog的学习')
        self.resize(500, 500)
        self.init_gui()

    def init_gui(self):
        # QColorDialog.setCustomColor(3, QColor(100, 200, 50))
        # QColorDialog.setStandardColor(2, QColor(255, 0, 0))
        self.cd = QColorDialog(QColor(0,255,0),self)
        self.cd.setWindowTitle("选择一个好看的颜色")
        self.cd.setOptions(QColorDialog.NoButtons | QColorDialog.ShowAlphaChannel)

        btn = QPushButton(self)
        btn.setText("按钮")
        btn.move(100, 100)
        btn.clicked.connect(self.col_sel)

    def get_color(self,color_obj):
        # print(color_obj)
        # print(self.cd.selectedColor())
        myp = QPalette()
        myp.setColor(QPalette.Background,color_obj)
        # myp.setColor(QPalette.Background,self.cd.selectedColor())
        self.setPalette(myp)

    def col_sel(self):
        # self.cd.colorSelected.connect(self.get_color)
        # self.cd.currentColorChanged.connect(self.get_color)
        # self.cd.show()

        color = QColorDialog.getColor(QColor(255,0,0), self, "选择颜色")
        palette = QPalette()
        # palette.setColor(QPalette.Background, cd.selectedColor())
        palette.setColor(QPalette.Background, color)
        self.setPalette(palette)

class MyWindow4(QWidget):
    def __init__(self):
        super(MyWindow4, self).__init__()
        self.setWindowTitle('QDialog的学习')
        self.resize(500, 500)
        self.init_gui()

    def init_gui(self):
        self.fd = QFileDialog(self, "选择一个文件", "./", "All(*.*);;Images(*.png *.jpg);;Python文件(*.py)")
        self.fd.setDefaultSuffix("txt")
        # self.fd.setAcceptMode(QFileDialog.AcceptSave)
        # self.fd.setFileMode(QFileDialog.Directory)
        self.fd.setFileMode(QFileDialog.ExistingFiles)
        # self.fd.setNameFilter("IMG(*.jpg *.png *.jpeg)")
        self.fd.setNameFilters(["All(*.*)", "Images(*.png *.jpg)", "Python文件(*.py)"])

        self.fd.setLabelText(QFileDialog.FileName, "顺哥的文件")
        self.fd.setLabelText(QFileDialog.Accept, "顺哥的接受")
        self.fd.setLabelText(QFileDialog.Reject, "顺哥的拒绝")

        btn = QPushButton(self)
        btn.setText("按钮")
        btn.move(100, 100)
        btn.clicked.connect(self.file_sel)

    def file_sel(self):
        # result = QFileDialog.getOpenFileName(self, "选择一个py文件", "./", "All(*.*);;Images(*.png *.jpg);;Python文件(*.py)", "Python文件(*.py)")
        # ('/root/PycharmProjects/codewars/gui_test/test_pyqt/test_checkbox.py', 'Python文件(*.py)')

        # result = QFileDialog.getOpenFileNames(self, "选择一个py文件", "./", "All(*.*);;Images(*.png *.jpg);;Python文件(*.py)", "Python文件(*.py)")
        # (['/root/PycharmProjects/codewars/gui_test/test_pyqt/my_viewer.py', '/root/PycharmProjects/codewars/gui_test/test_pyqt/test_absbtn.py', '/root/PycharmProjects/codewars/gui_test/test_pyqt/test_abspinbox.py', '/root/PycharmProjects/codewars/gui_test/test_pyqt/testbutton.py'], 'Python文件(*.py)')

        # result = QFileDialog.getOpenFileUrl(self, "选择一个py文件", QUrl("./"), "All(*.*);;Images(*.png *.jpg);;Python文件(*.py)", "Python文件(*.py)")
        # result = QFileDialog.getSaveFileName(self, "选择一个py文件", "./", "All(*.*);;Images(*.png *.jpg);;Python文件(*.py)", "Python文件(*.py)")
        # ('/root/PycharmProjects/codewars/gui_test/test_pyqt/123213', 'Python文件(*.py)')

        # result = QFileDialog.getExistingDirectory(self, "选择一个py文件", "./")
        # /root/PycharmProjects/codewars/gui_test/test_pyqt/__pycache__

        # result = QFileDialog.getExistingDirectoryUrl(self, "选择一个py文件", QUrl("./"))
        # PyQt5.QtCore.QUrl('file:///root/PycharmProjects/codewars/devops')

        # print(result)
        # self.fd.fileSelected.connect(self.get_file)
        # self.fd.currentChanged.connect(self.get_file)
        # self.fd.currentUrlChanged.connect(lambda url: print("当前路径QUrl发生改变时", url))
        # self.fd.directoryEntered.connect(lambda path: print("当前目录字符串进入时", path))
        # self.fd.directoryUrlEntered.connect(lambda url: print("当前目录QUrl进入时", url))
        self.fd.filterSelected.connect(lambda filter: print("当前名称过滤字符串被选中时", filter))

        self.fd.fileSelected.connect(lambda val: print("单个文件被选中-字符串", val))
        self.fd.filesSelected.connect(lambda val: print("多个文件被选中-列表[字符串]", val))
        self.fd.urlSelected.connect(lambda val: print("单个文件被选中-url", val))
        self.fd.urlsSelected.connect(lambda val: print("多个文件被选中-列表[url]", val))
        '''
        多个文件被选中-列表[url] [PyQt5.QtCore.QUrl('file:///root/PycharmProjects/codewars/gui_test/test_pyqt/f_slot_signal.py'), PyQt5.QtCore.QUrl('file:///root/PycharmProjects/codewars/gui_test/test_pyqt/loadqss.py')]
        多个文件被选中-列表[字符串] ['/root/PycharmProjects/codewars/gui_test/test_pyqt/f_slot_signal.py', '/root/PycharmProjects/codewars/gui_test/test_pyqt/loadqss.py']
        '''

        # self.fd.setWindowModality(Qt.WindowModal)
        # self.fd.show()
        self.fd.open()

    def get_file(self,file_name):
        print(file_name)

class MyWindow(QWidget):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setWindowTitle('QDialog的学习')
        self.resize(500, 500)
        self.init_gui()

    def init_gui(self):
        # self.qid = QInputDialog(self,Qt.FramelessWindowHint)
        self.qid = QInputDialog(self)
        self.qid.setWindowModality(Qt.WindowModal)
        self.qid.setOptions(QInputDialog.UseListViewForComboBoxItems | QInputDialog.UsePlainTextEditForTextInput)

        self.qid.setWindowTitle('test_input_dialog')
        self.qid.setLabelText('hehe')
        self.qid.setOkButtonText('OK')
        self.qid.setCancelButtonText('Cancel')

        # self.qid.setInputMode(QInputDialog.IntInput)
        # self.qid.setIntValue(10)

        # self.qid.setInputMode(QInputDialog.DoubleInput)
        self.qid.setInputMode(QInputDialog.TextInput)

        # self.qid.setIntRange(10,20)
        # self.qid.setIntStep(2)
        # self.qid.setDoubleStep(0.2)
        # self.qid.setDoubleDecimals(3)
        # self.qid.setDoubleRange(10.000,20.000)
        # self.qid.show()
        # self.qid.setComboBoxItems(['python','c++','java'])
        # self.qid.setComboBoxEditable(True)

        btn = QPushButton(self)
        btn.setText("按钮")
        btn.move(100, 100)
        btn.clicked.connect(self.get_input)

    def get_input(self):
        # result = QInputDialog.getInt(self, "xxx1", "xxx2", 888, step=8)
        # result = QInputDialog.getDouble(self, "xxx1", "xxx2", 888.88, decimals = 2)
        # result = QInputDialog.getText(self, "xx1", "xx2", echo=QLineEdit.Password)
        # ('', False)
        # ('22213', True)

        # result = QInputDialog.getMultiLineText(self, "xx1", "xx2", "default")

        # result = QInputDialog.getItem(self, "xx1", "xx2", ["1", "2", "3"], 2, True)
        # ('2', True)
        # ('3', False)

        # print(result)

        # self.qid.intValueSelected.connect(lambda val:print("selected: ",val))
        # self.qid.intValueChanged.connect(lambda val:print("changed: ",val))

        # self.qid.doubleValueSelected.connect(lambda val:print("selected: ",val))
        # self.qid.doubleValueChanged.connect(lambda val:print("changed: ",val))

        self.qid.textValueSelected.connect(lambda val:print("selected: ",val))
        self.qid.textValueChanged.connect(lambda val:print("changed: ",val))
        self.qid.show()

if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    mywindow = MyWindow()
    mywindow.show()
    sys.exit(app.exec_())