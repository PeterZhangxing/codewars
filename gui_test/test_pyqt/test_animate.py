from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class MyWindow(QWidget):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setWindowTitle('background_learning')
        self.resize(800, 800)
        # self.init_animation_gui()
        self.init_ag_gui()

    def init_ag_gui(self):
        red_btn = QPushButton("红色按钮", self)
        red_btn.resize(100, 100)
        red_btn.move(0, 0)
        red_btn.setStyleSheet("""
            background-color: red;
        """)

        green_btn = QPushButton("绿色按钮", self)
        green_btn.resize(100, 100)
        green_btn.move(150, 150)
        green_btn.setStyleSheet("""
            background-color: green;
        """)

        red_btn_animation = QPropertyAnimation(red_btn,b'pos',self)
        red_btn_animation.setKeyValueAt(0,QPoint(0,0))
        red_btn_animation.setKeyValueAt(0.25,QPoint(700,0))
        red_btn_animation.setKeyValueAt(0.5,QPoint(700,700))
        red_btn_animation.setKeyValueAt(0.75,QPoint(0,700))
        red_btn_animation.setKeyValueAt(1,QPoint(0,0))
        red_btn_animation.setDuration(6000)
        red_btn_animation.setLoopCount(2)

        green_btn_animation = QPropertyAnimation(green_btn,b'pos',self)
        green_btn_animation.setKeyValueAt(0,QPoint(150,150))
        green_btn_animation.setKeyValueAt(0.25,QPoint(150,550))
        green_btn_animation.setKeyValueAt(0.5,QPoint(550,550))
        green_btn_animation.setKeyValueAt(0.75,QPoint(550,150))
        green_btn_animation.setKeyValueAt(1,QPoint(150,150))
        green_btn_animation.setDuration(6000)
        green_btn_animation.setLoopCount(1)

        # animation_group = QParallelAnimationGroup(self)
        # animation_group.addAnimation(red_btn_animation)
        # animation_group.addAnimation(green_btn_animation)

        pause_animation = QPauseAnimation(self)
        pause_animation.setDuration(3000)

        animation_group = QSequentialAnimationGroup(self)
        animation_group.addAnimation(red_btn_animation)
        # animation_group.addPause(3000)
        animation_group.addAnimation(pause_animation)
        animation_group.addAnimation(green_btn_animation)

        red_btn.clicked.connect(animation_group.pause)
        green_btn.clicked.connect(animation_group.resume)

        animation_group.start()

    def init_animation_gui(self):
        btn = QPushButton("测试按钮", self)
        btn.move(0, 0)
        btn.resize(100, 100)
        btn.setStyleSheet("background-color: cyan;")
        btn.clicked.connect(self.change_animation)

        # 1. 创建一个动画对象, 并且设置目标 属性
        # animation = QPropertyAnimation(self)
        # animation.setTargetObject(btn)
        # animation.setPropertyName(b"pos")
        # animation = QPropertyAnimation(btn, b"geometry", self)
        # animation = QPropertyAnimation(btn, b"pos", self)
        # animation = QPropertyAnimation(btn, b"size", self)
        animation = QPropertyAnimation(btn, b"geometry", self)
        self.animation = animation

        # 2. 设置属性值 开始 插值 结束
        # animation.setStartValue(QPoint(0, 0))
        # animation.setKeyValueAt(0.5, 0.5)
        # animation.setKeyValueAt(1, 1)
        # animation.setEndValue(QPoint(300, 300))

        # animation.setStartValue(QSize(0, 0))
        # animation.setEndValue(QSize(300, 300))

        animation.setStartValue(QRect(0, 0,0,0))
        animation.setEndValue(QRect(200,200,300, 300))

        # 3. 动画时长
        animation.setDuration(3000)

        animation.setLoopCount(3)
        animation.setEasingCurve(QEasingCurve.OutBounce)
        # animation.setDirection(QAbstractAnimation.Backward)

        animation.currentLoopChanged.connect(lambda val:print("当前循环次数发生改变", val))
        animation.finished.connect(lambda :print("动画执行完毕"))
        animation.stateChanged.connect(lambda ns, os:print("状态发生改变", ns, os))

        # 4. 启动动画
        animation.start()
        print(animation.totalDuration(), animation.duration())

    def change_animation(self):
        if self.animation.state() == QAbstractAnimation.Running:
            self.animation.pause()
        elif self.animation.state() == QAbstractAnimation.Paused:
            self.animation.resume()
        elif self.animation.state() == QAbstractAnimation.Stopped:
            self.animation.start()

        print(self.animation.loopCount(), self.animation.currentLoop())
        print(self.animation.currentTime(), self.animation.currentLoopTime())

if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    mywindow = MyWindow()
    mywindow.show()
    sys.exit(app.exec_())