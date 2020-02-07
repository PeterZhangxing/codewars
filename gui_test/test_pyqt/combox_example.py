from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class MyWindow(QWidget):
    city_dic = {
        "北京": {
            "东城": "001",
            "西城": "002",
            "朝阳": "003",
            "丰台": "004"
        },
        "上海": {
            "黄埔": "005",
            "徐汇": "006",
            "长宁": "007",
            "静安": "008",
            "松江": "009"
        },
        "广东": {
            "广州": "010",
            "深圳": "011",
            "湛江": "012",
            "佛山": "013"
        }
    }

    def __init__(self):
        super(MyWindow, self).__init__()
        self.setWindowTitle('QTime学习')
        self.resize(500,500)
        self.init_gui()

    def init_gui(self):
        self.pro_cb = QComboBox(self)
        self.city_cb = QComboBox(self)

        # self.pro_cb.showPopup()
        self.pro_cb.setMaxVisibleItems(1)
        self.pro_cb.currentIndexChanged[str].connect(self.pro_changed)
        self.city_cb.showPopup()
        self.city_cb.currentIndexChanged[str].connect(self.city_changed)
        # self.city_cb.highlighted[str].connect(lambda p_str:print(p_str))
        self.city_cb.highlighted[int].connect(lambda p_index:print(self.city_cb.itemData(p_index),self.city_cb.itemText(p_index)))

        self.pro_cb.addItems(self.city_dic.keys())
        self.pro_cb.move(100,100)
        self.city_cb.move(200,100)

    def pro_changed(self,pro_name):
        # print(pro_name)
        city_dict = self.city_dic[pro_name]
        # print(city_dict)
        self.city_cb.blockSignals(True)
        self.city_cb.clear()
        self.city_cb.blockSignals(False)
        for key,val in city_dict.items():
            self.city_cb.addItem(QIcon('images/left.png'),key,val)

    def city_changed(self,city_name):
        print(city_name)
        print(self.city_cb.currentData())

if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    mywindow = MyWindow()
    mywindow.show()
    sys.exit(app.exec_())