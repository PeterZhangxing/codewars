from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from resources.register_ui import Ui_Form

class RegisterPanel(QWidget,Ui_Form):
    exit_signal = pyqtSignal()
    register_account_pwd_signal = pyqtSignal(str, str)

    def __init__(self, parent=None, *args, **kwargs):
        super(RegisterPanel, self).__init__(parent, *args, **kwargs)
        self.setAttribute(Qt.WA_StyledBackground,True)
        self.setupUi(self)
        self.animation_targets = [ self.pushButton_about,self.pushButton_quit,self.pushButton_reset ]
        self.animation_targets_pos = [ target.pos() for target in self.animation_targets ]
        self.pushButton_menu.setChecked(True)

    def show_hide_menue(self,ischecked):
        # print('show_hide_menue',ischecked)
        animation_group = QSequentialAnimationGroup(self)
        for index,target in enumerate(self.animation_targets):
            animation = QPropertyAnimation(self)
            animation.setTargetObject(target)
            animation.setPropertyName(b'pos')
            animation.setStartValue(self.animation_targets_pos[index])
            animation.setEndValue(self.pushButton_menu.pos())
            animation.setDuration(200)
            animation.setEasingCurve(QEasingCurve.OutBounce)
            animation_group.addAnimation(animation)

        if not ischecked:
            animation_group.setDirection(QAbstractAnimation.Forward)
        else:
            animation_group.setDirection(QAbstractAnimation.Backward)
        animation_group.start()

    def about_me(self):
        # print('about_me')
        QMessageBox.about(self, "Baidu", "https://www.baidu.com")

    def reset_input(self):
        # print('reset_input')
        self.lineEdit_username.clear()
        self.lineEdit_password.clear()
        self.lineEdit_confirm.clear()

    def enable_register_btn(self):
        username = self.lineEdit_username.text()
        password = self.lineEdit_password.text()
        confirm = self.lineEdit_confirm.text()
        isenabled = False
        if len(username)*len(password)*len(confirm) != 0 and password == confirm:
            isenabled = True
        self.pushButton_register.setEnabled(isenabled)

    def exit_panel(self):
        # print('exit_panel')
        self.exit_signal.emit()
        self.close()

    def check_register(self):
        # print('check_register')
        username = self.lineEdit_username.text()
        password = self.lineEdit_password.text()
        self.register_account_pwd_signal.emit(username,password)


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)

    window = RegisterPanel()
    window.exit_signal.connect(lambda :print("退出"))
    window.register_account_pwd_signal.connect(lambda a, p: print(a, p))
    window.show()

    sys.exit(app.exec_())