import sys
import myfirst
from PyQt5.QtWidgets import QApplication,QMainWindow

if __name__ == '__main__':
    # 生成一个运行窗口的程序
    app = QApplication(sys.argv)
    # 生成放置控件的主窗口
    mwindow = QMainWindow()

    # 获取所有的控件
    ui = myfirst.Ui_MainWindow()
    # 将控件放置到主窗口内
    ui.setupUi(mwindow)

    # 显示放置了控件的主窗口
    mwindow.show()
    # 循环运行程序，直到退出程序
    sys.exit(app.exec_())