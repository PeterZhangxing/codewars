import sys
from PyQt5.QtWidgets import QApplication,QWidget


if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = QWidget()

    w.resize(500,300)

    w.move(200,100)

    w.setWindowTitle('first window')

    w.show()

    exit(app.exec_())