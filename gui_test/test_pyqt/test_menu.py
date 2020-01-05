from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class MyWindow(QWidget):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setWindowTitle('按钮的功能')
        self.resize(700,500)
        self.init_gui()

        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.show_menu)

    def init_gui(self):
        self.button = QPushButton(self)
        self.button.setText("menu_button")
        self.button.setIcon(QIcon("images/left.png"))
        self.button.setIconSize(QSize(64,64))
        self.button.adjustSize()
        self.button.setFlat(True)
        self.show_window_file_menu()
        self.button.setMenu(self.menu)

        self.lbtn = QCommandLinkButton(self)
        # QCommandLinkButton("标题", "描述", window)
        self.lbtn.setIcon(QIcon("images/left2.png"))
        self.lbtn.setText('btn_title')
        self.lbtn.setDescription('button_content')
        self.lbtn.setFlat(True)
        self.lbtn.adjustSize()
        self.lbtn.setMenu(self.menu)
        self.lbtn.move(200,0)

        self.tbtn = QToolButton(self)
        self.tbtn.setText("tool_button")
        self.tbtn.setIcon(QIcon("images/left3.png"))
        self.tbtn.setToolTip("这是一个新建按钮")
        # Qt.ToolButtonIconOnly
        # 	仅显示图标
        # Qt.ToolButtonTextOnly
        # 	仅显示文字
        # Qt.ToolButtonTextBesideIcon
        # 	文本显示在图标旁边
        # Qt.ToolButtonTextUnderIcon
        # 	文本显示在图标下方
        # Qt.ToolButtonFollowStyle
        # 	遵循风格
        self.tbtn.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        self.tbtn.setAutoRaise(True)
        self.tbtn.setMenu(self.menu)
        self.tbtn.move(400, 0)
        self.tbtn.adjustSize()

        # three different ways to show the menu of this tool button
        # self.tbtn.setPopupMode(QToolButton.InstantPopup)
        # self.tbtn.setPopupMode(QToolButton.DelayedPopup)
        self.tbtn.setPopupMode(QToolButton.MenuButtonPopup)
        # this slot will be triggered when you clicked any menu related to this tool button
        self.tbtn.triggered.connect(lambda action:print('total_action:',action.data()))

        # Qt.NoArrow
        # 	无箭头
        # Qt.UpArrow
        # 	向上箭头
        # Qt.DownArrow
        # 	向下箭头
        # Qt.LeftArrow
        # 	向左箭头
        # Qt.RightArrow
        # 	向右箭头
        self.tbtn.setArrowType(Qt.RightArrow)

    def show_window_file_menu(self):
        self.menu = QMenu(self)

        sub_menu = QMenu(self.menu)
        sub_menu.setTitle('最近打开')
        # 行为动作 新建  打开  分割线 退出
        # new_action = QAction()
        # new_action.setText("新建")
        # new_action.setIcon(QIcon("xxx.png"))
        sub_action1 = QAction(QIcon("images/left3.png"), 'recent_file1', sub_menu)
        sub_action1.triggered.connect(lambda :print('open recent file1'))

        sub_action2 = QAction(QIcon("images/leftup.png"), 'recent_file2', sub_menu)
        sub_action2.triggered.connect(lambda: print('open recent file2'))

        sub_action3 = QAction(QIcon("images/leftdown.png"), 'recent_file2', sub_menu)
        sub_action3.triggered.connect(lambda: print('open recent file3'))

        sub_menu.addAction(sub_action1)
        sub_menu.addAction(sub_action2)
        sub_menu.addAction(sub_action3)

        myaction1 = QAction(QIcon("images/right.png"), 'new_file',self.menu)
        myaction1.triggered.connect(lambda :print('new_file'))
        myaction1.setData('new_file')

        myaction2 = QAction(QIcon("images/right2.png"), 'open_file',self.menu)
        myaction2.triggered.connect(lambda: print('open_file'))
        myaction2.setData('open_file')

        myaction3 = QAction(QIcon("images/right3.png"), 'exit_file',self.menu)
        myaction3.triggered.connect(lambda: print('exit_programme'))
        myaction3.setData('exit_programme')

        self.menu.addAction(myaction1)
        self.menu.addAction(myaction2)
        self.menu.addSeparator()
        self.menu.addMenu(sub_menu)
        self.menu.addSeparator()
        self.menu.addAction(myaction3)

    def show_menu(self,point):
        print('in show_menu')
        dest_point = self.mapToGlobal(point)
        self.show_window_file_menu()
        self.menu.exec_(dest_point)

    # def contextMenuEvent(self, QContextMenuEvent):
    #     # this method will be triggered when click the right button of your mouse
    #     self.show_window_file_menu()
    #     self.menu.exec_(QContextMenuEvent.globalPos())


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)

    mywindow = MyWindow()
    mywindow.show()
    mywindow.button.showMenu()

    sys.exit(app.exec_())