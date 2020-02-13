from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class MyWindow(QWidget):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setWindowTitle('QDialog的学习')
        self.resize(500, 500)
        # self.init_em_gui()
        # self.init_pd_gui()
        self.init_mb_gui()

    def init_mb_gui(self):
        # self.mb = QMessageBox(QMessageBox.Critical, "title", "<h2>fuck you!</h2>", QMessageBox.Ok | QMessageBox.Discard, self)
        self.mb = QMessageBox(self)
        # self.mb.setWindowModality(Qt.NonModal)
        self.mb.setModal(False)
        self.mb.setText('<h3>Message:</h3>')
        self.mb.setInformativeText('<em>You are fucked!</em>')
        self.mb.setWindowTitle("test_mb")
        # self.mb.setIcon(QMessageBox.Information)
        # self.mb.setIcon(QMessageBox.Warning)
        self.mb.setIconPixmap(QPixmap('images/dog.jpg').scaled(80,80))
        self.mb_checkbox = QCheckBox("下次不再提醒", self.mb)
        self.mb.setCheckBox(self.mb_checkbox)
        self.mb.setDetailedText("Nothing to show here!")
        self.mb.setTextInteractionFlags(Qt.TextEditorInteraction)

        self.mb_cancel_btn = QPushButton("cancel", self.mb)
        self.mb_confirm_btn = QPushButton("yes", self.mb)
        self.mb.addButton(self.mb_cancel_btn, QMessageBox.NoRole)
        self.mb.addButton(self.mb_confirm_btn, QMessageBox.YesRole)

        # self.mb.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        # self.mb_cancel_btn = self.mb.button(QMessageBox.No)
        # self.mb_confirm_btn = self.mb.button(QMessageBox.Yes)

        # self.mb_cancel_btn = self.mb.addButton("cancel", QMessageBox.NoRole)
        # self.mb_confirm_btn = self.mb.addButton("yes", QMessageBox.YesRole)

        # print(mb_cancel_btn,mb_confirm_btn)
        self.mb.setDefaultButton(self.mb_confirm_btn)
        # self.mb.removeButton(self.mb_confirm_btn)
        self.mb.setEscapeButton(self.mb_cancel_btn)

        self.mb.buttonClicked.connect(self.mb_btn_clicked)

        btn = QPushButton(self)
        btn.move(200, 200)
        btn.setText("测试按钮")
        btn.clicked.connect(self.test_mb)

    def mb_btn_clicked(self,btn_obj):
        print(btn_obj)
        print(self.mb_checkbox.isChecked())

        btn_role = self.mb.buttonRole(btn_obj)
        if btn_obj == self.mb_confirm_btn:
            print("you pressed yes button!")
        elif btn_obj == self.mb_cancel_btn:
            print("you pressed cancel button!")
        else:
            pass

        if btn_role == QMessageBox.YesRole:
            print("you pressed yes_role button!")
        elif btn_role == QMessageBox.NoRole:
            print("you pressed cancel_role button!")
        else:
            print('no role!')

    def test_mb(self):
        # result = QMessageBox.about(self, "xx1", "xx2")
        # result = QMessageBox.aboutQt(self, "xx1")
        # result = QMessageBox.question(self, "xx1", "xx2", QMessageBox.Ok | QMessageBox.Discard, QMessageBox.Discard)
        # print(result, "xxx")

        self.mb.show()

    def init_pd_gui(self):
        self.pd = QProgressDialog(self)
        self.pd.setWindowTitle("xx3")
        self.pd.setLabelText("下载进度")
        self.pd.setCancelButtonText("取消下载")
        # self.pd.setMaximum(200)
        self.pd.setRange(1,101)

        # self.pd.setAutoClose(False)
        # self.pd.setAutoReset(False)
        self.pd.setMinimumDuration(100)
        # self.pd.open(lambda :print('cancelled'))

        # self.pd = QProgressDialog("xx1", "xx2", 1, 1000, self)
        # print(self.pd.maximum())
        # print(self.pd.minimum())

        btn = QPushButton(self)
        btn.move(200, 200)
        btn.setText("测试按钮")
        btn.clicked.connect(self.test_pd)

    def test_pd(self):
        self.pd.setValue(95)
        self.pd.show()
        timer = QTimer(self.pd)
        timer.timeout.connect(self.pd_timeout)
        self.pd.canceled.connect(self.cancelled)
        timer.start(500)
        self.timer = timer

    def cancelled(self):
        self.timer.stop()
        self.pd.cancel()

    def pd_timeout(self):
        if self.pd.value() + 1 >= self.pd.maximum():
            self.timer.stop()
        self.pd.setValue(self.pd.value()+1)

    def init_em_gui(self):
        btn = QPushButton(self)
        btn.move(200, 200)
        btn.setText("测试按钮")
        btn.clicked.connect(self.test_em)

        self.em = QErrorMessage(self)
        self.em.setWindowTitle("错误提示")
        self.em.setModal(True)

    def test_em(self):
        self.em.showMessage("Warning:\nfuck you!")
        self.em.showMessage("fuck you!")
        self.em.showMessage("fuck you!")
        self.em.showMessage("fuck you twice!")

        self.em.show()
        # self.em.open()

        # QErrorMessage.qtHandler()
        # qDebug("xxxx")
        # qWarning("123456")

if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    mywindow = MyWindow()
    mywindow.show()
    sys.exit(app.exec_())