import sys
import sys
from random import randint
from PyQt5.QtWidgets import QWidget, QApplication, QLabel
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QColor
from PyQt5 import uic


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.qp = QPainter()
        uic.loadUi('UI.ui', self)
        self.pushButton.clicked.connect(self.paint)
        self.show()
        self.coords = [200, 200]
        self.setGeometry(300, 300, 500, 500)
        self.do_paint = True

    def paint(self):
        self.do_paint = True
        self.repaint()

    def paintEvent(self, event):
        if self.do_paint:
            self.qp = QPainter()
            self.qp.begin(self)
            self.draw()
            self.qp.end()
            self.do_paint = False

    def draw(self):
        self.qp.setBrush(QColor(255, 255, 0))
        self.qp.setPen(QColor(0, 0, 0))
        self.qp.drawEllipse(*self.coords, randint(20, 200), randint(20, 200))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())