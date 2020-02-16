from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class MyWindow(QWidget):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setWindowTitle('layout的学习')
        self.resize(500, 500)
        # self.init_boxlayout_gui()
        # self.init_vhbox_gui()
        self.init_form_gui()

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