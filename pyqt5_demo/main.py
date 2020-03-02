from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from register_panel import RegisterPanel
from login_panel import LoginPanel
from calculator_panel import CalculatorPanel

if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)

    login_panel = LoginPanel()

    register_panel = RegisterPanel(login_panel)
    register_panel.move(0, login_panel.height())

    calculator_panel = CalculatorPanel()

    def show_register_panel():
        register_panel.show()
        animation = QPropertyAnimation(register_panel)
        animation.setTargetObject(register_panel)
        animation.setPropertyName(b"pos")
        animation.setStartValue(QPoint(0, login_panel.height()))
        animation.setEndValue(QPoint(0, 0))
        animation.setDuration(500)
        animation.setEasingCurve(QEasingCurve.OutBounce)
        animation.start(QAbstractAnimation.DeleteWhenStopped)

    def exit_register_panel():
        animation = QPropertyAnimation(register_panel)
        animation.setTargetObject(register_panel)
        animation.setPropertyName(b"pos")
        animation.setStartValue(QPoint(0, 0))
        animation.setEndValue(QPoint(0, login_panel.height()))
        animation.setDuration(500)
        animation.setEasingCurve(QEasingCurve.InBounce)
        animation.start(QAbstractAnimation.DeleteWhenStopped)

    def check_login(account,pwd):
        print('check_login',account,pwd)
        if account == '964725349' and pwd == 'redhat':
            login_panel.close()
            calculator_panel.show()
        else:
            login_panel.show_error_action()

    login_panel.show_register_pane_signal.connect(show_register_panel)
    login_panel.check_login_signal.connect(check_login)

    register_panel.register_account_pwd_signal.connect(lambda account, pwd: print('register_panel',account, pwd))
    register_panel.exit_signal.connect(exit_register_panel)

    login_panel.show()
    sys.exit(app.exec_())