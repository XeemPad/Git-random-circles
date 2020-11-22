import sys
from random import randint

from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QColor

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(600, 520)
        self.startButton = QtWidgets.QPushButton(Form)
        self.startButton.setGeometry(QtCore.QRect(254, 472, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.startButton.setFont(font)
        self.startButton.setObjectName("startButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.startButton.setText(_translate("Form", "Пуск"))


class Widget(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        self.setGeometry(500, 200, 600, 520)
        self.setWindowTitle('Случайные окружности')

        self.do_paint = False
        self.startButton.clicked.connect(self.paint)

    def paint(self):
        self.do_paint = True
        self.update()

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_rings(qp)
            qp.end()

    def draw_rings(self, qp):
        color = randint(0, 255), randint(0, 255), randint(0, 255)
        qp.setBrush(QColor(*color))
        for _ in range(10):
            x, y = randint(0, 580), randint(0, 500)
            d = randint(5, 100)
            while x + d > 600 or y + d > 520:
                x, y = randint(0, 580), randint(0, 500)
                d = randint(5, 100)
            qp.drawEllipse(x, y, d, d)
        self.do_paint = False


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = Widget()
    window.show()

    sys.exit(app.exec())
