from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class MyTestWindow(QWidget):
    def __init__(self):
        super(MyTestWindow, self).__init__()
        self.setWindowTitle('example for slider')
        self.resize(500,500)
        self.init_gui()

    def init_gui(self):
        label = QLabel(self)
        label.setText("0")
        label.move(200, 200)
        label.resize(100, 30)

        sd = QSlider(self)
        sd.move(100, 100)
        sd.resize(20,300)

        # sd.valueChanged.connect(lambda val:label.setText(str(val)))
        sd.valueChanged.connect(lambda :label.setText(str(sd.value())))

        sd.setMaximum(100)
        sd.setMinimum(66)
        sd.setTracking(True)
        sd.setTickPosition(QSlider.TicksBothSides)
        sd.setTickInterval(2)

        # 当前数值
        # sd.setValue(88)
        sd.setSliderPosition(80)

        # 步长设置
        sd.setSingleStep(5)
        sd.setPageStep(8)

        # 倒立外观
        # sd.setInvertedAppearance(True)
        # sd.setInvertedControls(True)
        sd.setOrientation(Qt.Horizontal)
        sd.resize(300, 20)

        sd.sliderMoved.connect(lambda val:print(val))
        sd.actionTriggered.connect(lambda val:print(val))
        sd.rangeChanged.connect(lambda min, max:print(min, max))
        sd.setRange(50,200)

class MySlider(QSlider):
    def __init__(self,parent=None,*args,**kwargs):
        super(MySlider, self).__init__(parent,*args,**kwargs)
        self.setTickPosition(QSlider.TicksBothSides)
        self.setTickInterval(10)
        self.init_gui()

    def init_gui(self):
        self.lab = QLabel(self)
        self.lab.setText("0")
        self.lab.setStyleSheet("color:red;")
        self.lab.hide()

    def mousePressEvent(self, evnt):
        # QMouseEvent
        super(MySlider, self).mousePressEvent(evnt)
        # lab_x = (self.width()-self.lab.width())/2
        lab_x = self.width()/2-self.lab.width()/2
        lab_y = (1 - self.value() / (self.maximum() - self.minimum())) * (self.height() - self.lab.height())
        self.lab.move(lab_x,lab_y)
        self.lab.show()

    def mouseMoveEvent(self, evnt):
        super(MySlider, self).mouseMoveEvent(evnt)
        lab_x = self.width()/2-self.lab.width()/2
        lab_y = (1 - self.value() / (self.maximum() - self.minimum())) * (self.height() - self.lab.height())
        self.lab.move(lab_x,lab_y)
        self.lab.setText(str(self.value()))
        self.lab.adjustSize()

    def mouseReleaseEvent(self, evnt):
        super(MySlider, self).mouseReleaseEvent(evnt)
        self.lab.hide()

class MyWindow(QWidget):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setWindowTitle('example for slider')
        self.resize(500, 500)
        self.init_gui()

    def init_gui(self):
        self.myslider = MySlider(self)
        self.myslider.move(235,100)
        self.myslider.resize(30,300)

if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    # mywindow = MyTestWindow()
    mywindow = MyWindow()
    mywindow.show()
    sys.exit(app.exec_())