from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import time

class MyWindow(QWidget):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setWindowTitle('QDialog的学习')
        self.resize(500, 500)
        self.init_gui()

    def init_gui(self):
        self.cw = QCalendarWidget(self)
        self.cw.setFixedWidth(400)
        self.cw.move(250-self.cw.width()//2,10)

        # self.cw.setMaximumDate(QDate(2022,1,1))
        # self.cw.setMinimumDate(QDate.currentDate())
        # self.cw.setDateRange(QDate(1990, 1, 1), QDate(2020, 11, 12))
        # self.cw.setSelectedDate(QDate(-9999, 1, 1))

        self.cw.setDateEditEnabled(True)
        self.cw.setDateEditAcceptDelay(3000)

        # self.cw.currentPageChanged.connect(lambda mydate:print('PageChanged:',mydate))
        # self.cw.clicked.connect(lambda mydate:print('clicked:',mydate))
        # self.cw.activated.connect(lambda mydate:print('activated:',mydate))
        self.cw.selectionChanged.connect(lambda :print('selectionChanged:',self.cw.selectedDate()))

        btn = QPushButton(self)
        btn.setText("按钮")
        btn.move(100, 300)
        btn.clicked.connect(self.get_date)

    def get_date(self):
        print(self.cw.selectedDate())
        print(self.cw.monthShown())
        print(self.cw.yearShown())

        # showToday()
        # showSelectedDate()
        # showNextYear()
        # showPreviousYear()
        # showNextMonth()
        # showPreviousMonth()
        # setCurrentPage(int year, int month)

        # self.cw.setCurrentPage(2008,1)
        # self.cw.showToday()
        self.cw.showNextYear()

if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    mywindow = MyWindow()
    mywindow.show()
    sys.exit(app.exec_())