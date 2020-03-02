from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from resources.login_ui import Ui_Form

class LoginPanel(QWidget,Ui_Form):

    show_register_pane_signal = pyqtSignal()
    check_login_signal = pyqtSignal(str, str)

    def __init__(self, parent=None, *args, **kwargs):
        super(LoginPanel, self).__init__(parent, *args, **kwargs)
        self.setAttribute(Qt.WA_StyledBackground,True)
        self.setupUi(self)

        movie = QMovie(":/loginpanel/images/login_top_bg.gif")
        movie.setScaledSize(QSize(500, 190))
        self.label_register.setMovie(movie)
        movie.start()

        # self.comboBox_account.currentTextChanged['QString'].connect(Form.userinfo_changed)
        # self.lineEdit_pwd.textChanged['QString'].connect(Form.userinfo_changed)
        # self.checkBox_autologin.clicked['bool'].connect(Form.autologin_changed)
        # self.checkBox_rempwd.clicked['bool'].connect(Form.rem_pwd_changed)
        # self.pushButton_register.clicked.connect(Form.register_panel_show)
        # self.pushButton_qq.clicked.connect(Form.dispaly_qq)
        # self.pushButton_login.clicked.connect(Form.get_login_info)

    def userinfo_changed(self,content):
        # print('userinfo_changed',content)
        account = self.comboBox_account.currentText()
        pwd = self.lineEdit_pwd.text()
        isenabled = False
        if len(account)*len(pwd) != 0:
            isenabled = True
        self.pushButton_login.setEnabled(isenabled)

    def autologin_changed(self,ischecked):
        # print('autologin_changed',ischecked)
        if ischecked:
            self.checkBox_rempwd.setChecked(True)

    def rem_pwd_changed(self,ischecked):
        # print('rem_pwd_changed',ischecked)
        if not ischecked:
            self.checkBox_autologin.setChecked(False)

    def register_panel_show(self):
        print('register_panel_show')
        self.show_register_pane_signal.emit()

    def dispaly_qq(self):
        # print('dispaly_qq')
        link = "http://shang.qq.com/wpa/qunwpa?idkey=b4d516fe37a2da8c8690140b133cb5a194aef98e639f4481500e271e1850ab3d"
        QDesktopServices.openUrl(QUrl(link))

    def get_login_info(self):
        # print('get_login_info')
        account = self.comboBox_account.currentText()
        pwd = self.lineEdit_pwd.text()
        self.check_login_signal.emit(account,pwd)

    def show_error_action(self):
        animation = QPropertyAnimation(self)
        animation.setTargetObject(self.widget_2)
        animation.setPropertyName(b"pos")

        animation.setKeyValueAt(0,self.widget_2.pos())
        animation.setKeyValueAt(0.25,self.widget_2.pos()+QPoint(15,0))
        animation.setKeyValueAt(0.5,self.widget_2.pos())
        animation.setKeyValueAt(0.75, self.widget_2.pos() + QPoint(-15, 0))
        animation.setKeyValueAt(1, self.widget_2.pos())

        animation.setDuration(100)
        animation.setLoopCount(3)
        # animation.setEasingCurve(QEasingCurve.InBounce)
        animation.start(QAbstractAnimation.DeleteWhenStopped)

if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)

    window = LoginPanel()
    window.show()

    sys.exit(app.exec_())