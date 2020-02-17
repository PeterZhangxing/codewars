from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class Label(QLabel):
    def sizeHint(self):
        return QSize(180, 180)

    def minimumSizeHint(self):
        return QSize(100, 180)

class MyWindow(QWidget):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setWindowTitle('layout的学习')
        self.resize(500, 500)
        # self.init_boxlayout_gui()
        # self.init_vhbox_gui()
        # self.init_form_gui()
        # self.init_grid_gui()
        # self.init_stack_gui()
        self.init_sizepolicy_gui()
        self.labs = self.get_labs()
        self.curpos = 0

    def get_labs(self):
        tmp_li = []
        for child in self.children():
            if child.__class__ == QLabel:
                # print(child.__class__)
                tmp_li.append(child)
        return tmp_li

    def init_sizepolicy_gui(self):
        label1 = Label("标签1")
        label1.setStyleSheet("background-color: cyan;")
        label2 = QLabel("标签2")
        label2.setStyleSheet("background-color: yellow;")
        label3 = QLabel("标签3")
        label3.setStyleSheet("background-color: red;")

        layout = QVBoxLayout()
        self.setLayout(layout)

        layout.addWidget(label1)
        layout.addWidget(label2)
        layout.addWidget(label3)

        # label1.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        # label1.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        # label1.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        label1.setSizePolicy(QSizePolicy.Maximum, QSizePolicy.Minimum)

        # sp = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        # sp.setRetainSizeWhenHidden(True)
        # label1.setSizePolicy(sp)

        # label1.setFixedSize(200, 200)
        # label2.setFixedSize(400, 100)
        # label1.hide()


    def init_stack_gui(self):
        s_layout = QStackedLayout()
        s_layout.currentChanged.connect(lambda val:print('current_index:',s_layout.widget(val).text()))
        self.sl = s_layout
        self.setLayout(s_layout)

        label1 = QLabel("标签1")
        label1.setStyleSheet("background-color: cyan;")
        label2 = QLabel("标签2")
        label2.setStyleSheet("background-color: yellow;")
        label3 = QLabel("标签3")
        label3.setStyleSheet("background-color: red;")
        label4 = QLabel("标签4")
        label4.setStyleSheet("background-color: orange;")

        label5 = QLabel("标签5")
        label5.setStyleSheet("background-color: pink;")
        label6 = QLabel("标签6")
        label6.setStyleSheet("background-color: blue;")
        label7 = QLabel("标签7")
        label7.setStyleSheet("background-color: cyan;")
        v_layout = QVBoxLayout()
        v_layout.addWidget(label5)
        v_layout.addWidget(label6)
        v_layout.addWidget(label7)

        print(s_layout.addWidget(label1))
        print(s_layout.addWidget(label2))
        print(s_layout.addWidget(label3))

        # s_layout.setStackingMode(QStackedLayout.StackAll)

        label1.setFixedSize(100, 100)
        label2.setFixedSize(150, 150)
        # s_layout.removeWidget(label1)
        # s_layout.removeWidget(label2)

        print(s_layout.currentIndex())
        s_layout.insertWidget(0,label4)
        print(s_layout.currentIndex())
        print(s_layout.currentWidget().text())
        print(s_layout.widget(0).text())

        timer = QTimer(self)
        timer.timeout.connect(self.stack_change)
        timer.start(1000)

    def stack_change(self):
        child = self.labs[self.curpos]
        self.sl.setCurrentWidget(child)
        self.curpos = (self.curpos + 1) % len(self.labs)
        # self.sl.setCurrentIndex((self.sl.currentIndex()+1)%self.sl.count())

    def init_grid_gui(self):
        g_layout = QGridLayout()
        self.setLayout(g_layout)

        label1 = QLabel("标签1")
        label1.setStyleSheet("background-color: cyan;")
        label2 = QLabel("标签2")
        label2.setStyleSheet("background-color: yellow;")
        label3 = QLabel("标签3")
        label3.setStyleSheet("background-color: red;")

        label5 = QLabel("标签5")
        label5.setStyleSheet("background-color: pink;")
        label6 = QLabel("标签6")
        label6.setStyleSheet("background-color: blue;")
        label7 = QLabel("标签7")
        label7.setStyleSheet("background-color: cyan;")
        v_layout = QVBoxLayout()
        # v_layout.setDirection(QBoxLayout.RightToLeft)
        v_layout.addWidget(label5)
        v_layout.addWidget(label6)
        v_layout.addWidget(label7)

        g_layout.addWidget(label1,0,0)
        g_layout.addWidget(label2,0,2)
        g_layout.addWidget(label3,1,0,3,3)
        g_layout.addLayout(v_layout,4, 0, 1, 4)

        # print(gl.getItemPosition(2))
        print(g_layout.itemAtPosition(1, 0).widget().text())
        print(g_layout.itemAtPosition(4, 0).layout())
        # g_layout.setColumnMinimumWidth(0, 300)
        # g_layout.setRowMinimumHeight(0, 300)

        g_layout.setColumnStretch(0, 2)
        g_layout.setColumnStretch(2, 1)
        g_layout.setRowStretch(4,1)

        # g_layout.setSpacing(30)
        g_layout.setVerticalSpacing(50)
        g_layout.setHorizontalSpacing(100)
        print('spacing:',g_layout.spacing())
        print('horizontalSpacing:',g_layout.horizontalSpacing())
        print('verticalSpacing:',g_layout.verticalSpacing())

        g_layout.setOriginCorner(Qt.BottomRightCorner)

        print('rowCount:',g_layout.rowCount())
        print('columnCount:',g_layout.columnCount())

    def init_form_gui(self):
        name_label = QLabel("姓名(&n):")
        age_label = QLabel("年龄(&g):")

        name_le = QLineEdit()
        age_sb = QSpinBox()
        age_sb.setRange(18,20000)
        age_sb.setAccelerated(True)

        # name_label.setBuddy(name_le)
        # age_label.setBuddy(age_sb)

        sex_label = QLabel("性别:")
        male_rb = QRadioButton("男")
        female_rb = QRadioButton("女")
        h_layout = QHBoxLayout()
        h_layout.addWidget(male_rb)
        h_layout.addWidget(female_rb)

        submit_btn = QPushButton("提交")

        mylayout = QFormLayout()
        # mylayout.addRow("姓名(&n)", name_le)
        # mylayout.addRow(name_label,name_le)
        # layout.addRow("年龄(&g)", age_sb)
        mylayout.addRow(age_label,age_sb)
        # layout.addRow("性别:", h_layout)
        mylayout.addRow(sex_label,h_layout)
        mylayout.addRow(submit_btn)

        # mylayout.labelForField(name_le).setText("xxx" * 10 + ':')
        # print(mylayout.formAlignment() == Qt.AlignLeft | Qt.AlignTop)
        mylayout.setFormAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        mylayout.setLabelAlignment(Qt.AlignRight)
        mylayout.setHorizontalSpacing(50)
        mylayout.setVerticalSpacing(10)

        # mylayout.setRowWrapPolicy(QFormLayout.WrapAllRows)
        mylayout.setRowWrapPolicy(QFormLayout.WrapLongRows)
        # mylayout.setRowWrapPolicy(QFormLayout.DontWrapRows)
        # layout.insertRow(-1, "性别:", h_layout)

        mylayout.setFieldGrowthPolicy(QFormLayout.ExpandingFieldsGrow)
        # mylayout.setFieldGrowthPolicy(QFormLayout.AllNonFixedFieldsGrow)

        mylayout.setWidget(4, QFormLayout.LabelRole, name_label)
        mylayout.setWidget(4, QFormLayout.FieldRole, name_le)

        age_sb.destroyed.connect(lambda :print("年龄步长被释放"))
        age_label.destroyed.connect(lambda :print("年龄标签被释放"))

        # mylayout.removeRow(h_layout)
        # mylayout.removeRow(age_label)
        # mylayout.removeRow(1)
        # mylayout.removeWidget(age_label)
        # age_label.setParent(None)

        # print(mylayout.takeRow(1).labelItem.widget())
        # print(mylayout.takeRow(2).fieldItem.widget())
        # mylayout.takeRow(4)

        # print(mylayout.rowCount())
        # print(mylayout.getWidgetPosition(male_rb))
        # print(mylayout.getWidgetPosition(age_sb))
        # print(mylayout.getLayoutPosition(h_layout))
        '''
        4
        (-1, 32766)
        (1, 1)
        (2, 1)
        '''
        self.setLayout(mylayout)
        print(self.children())

    def init_vhbox_gui(self):
        hlayout = QHBoxLayout()
        vlayout = QVBoxLayout()
        self.vlay = vlayout

        label1 = QLabel('label1')
        label1.setStyleSheet("background-color:red;")

        label2 = QLabel('label2')
        label2.setStyleSheet("background-color:blue;")

        label3 = QLabel('label3')
        label3.setStyleSheet("background-color:green;")

        # hlayout.addWidget(label1)
        # hlayout.addWidget(label2)
        # hlayout.addWidget(label3)
        # self.setLayout(hlayout)

        vlayout.addWidget(label1)
        vlayout.addWidget(label2)
        vlayout.addWidget(label3)
        self.setLayout(vlayout)

        timer = QTimer(self)
        timer.timeout.connect(self.change_direction)
        timer.start(1000)

    def change_direction(self):
        self.vlay.setDirection((self.vlay.direction() + 1) % 4)

    def init_boxlayout_gui(self):
        mylayout = QBoxLayout(QBoxLayout.LeftToRight)
        sublayout = QBoxLayout(QBoxLayout.TopToBottom)

        label1 = QLabel('label1')
        label1.setStyleSheet("background-color:red;")

        label2 = QLabel('label2')
        label2.setStyleSheet("background-color:blue;")

        label3 = QLabel('label3')
        label3.setStyleSheet("background-color:green;")

        label4 = QLabel('label4')
        label4.setStyleSheet("background-color:yellow;")

        label5 = QLabel('label5')
        label5.setStyleSheet("background-color:orange;")

        label6 = QLabel('label6')
        label6.setStyleSheet("background-color:grey;")

        label7 = QLabel('label_replaced')
        label7.setStyleSheet("background-color:cyan;")

        mylayout.addWidget(label1,1)
        mylayout.addWidget(label2,1)
        mylayout.addWidget(label3,1)

        sublayout.addWidget(label4,1)
        sublayout.addWidget(label5,1)
        sublayout.addWidget(label6,3)
        sublayout.replaceWidget(label4,label7)
        # label4.hide()
        label4.setParent(None)

        mylayout.insertLayout(1,sublayout)

        mylayout.insertSpacing(1,30)
        mylayout.insertStretch(2,1)
        mylayout.setContentsMargins(10,20,30,40)
        print(mylayout.contentsMargins().left())
        print(mylayout.contentsMargins().top())

        self.setLayout(mylayout)

if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    mywindow = MyWindow()
    mywindow.show()
    sys.exit(app.exec_())