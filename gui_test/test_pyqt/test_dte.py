from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class MyWindow(QWidget):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setWindowTitle('QTime学习')
        self.resize(500,500)
        self.init_gui()

    def init_gui(self):
        self.dte = QDateTimeEdit(QDateTime.currentDateTime(),self)
        # self.dte = QDateTimeEdit(self)
        # self.dte = QDateTimeEdit(QDate.currentDate(), self)
        # self.dte = QDateTimeEdit(QTime.currentTime(), self)
        self.dte.move(100,100)
        # self.dte.resize(150,30)
        self.dte.setCalendarPopup(True)
        self.dte.setDisplayFormat("yyyy-MM-MMMM-dd-dddd && mm:ss:zzz")

        # self.dte.setMaximumDateTime(QDateTime(2022, 12, 30, 24, 00))
        # self.dte.setMinimumDateTime(QDateTime(2020, 12, 30, 24, 00))
        self.dte.setDateTimeRange(QDateTime.currentDateTime().addDays(-3), QDateTime.currentDateTime().addDays(3))

        self.dte.timeChanged.connect(lambda val:print('time:',val))
        self.dte.dateChanged.connect(lambda val:print('date:',val))
        self.dte.dateTimeChanged.connect(lambda val:print('datetime:',val))

        time_now = QTime.currentTime()
        time_now.start()
        self.time_now = time_now

        btn = QPushButton(self)
        btn.move(200, 200)
        btn.setText("测试")
        btn.clicked.connect(self.test_btn)

        btn1 = QPushButton(self)
        btn1.move(200, 260)
        btn1.setText("测试timecount")
        btn1.clicked.connect(self.time_count)

    def test_btn(self):
        print(self.dte.sectionCount())
        print(self.dte.currentSection())
        print(self.dte.currentSectionIndex())
        # self.dte.setSpecialValueText("start")
        self.dte.setFocus()
        # self.dte.setCurrentSectionIndex(2)
        self.dte.setCurrentSection(QDateTimeEdit.DaySection)
        print(self.dte.sectionText(QDateTimeEdit.DaySection))
        # QDateTime
        print(self.dte.dateTime().time())
        print(self.dte.dateTime().date())
        print(self.dte.sectionText(QDateTimeEdit.MonthSection))
        print(self.dte.text())

    def time_count(self):
        time_count = self.time_now.elapsed()
        print(type(time_count),time_count//1000)

if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    mywindow = MyWindow()
    mywindow.show()
    sys.exit(app.exec_())