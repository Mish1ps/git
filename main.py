import sys
from PyQt5.QtGui import QPainter, QPen
from PyQt5.QtCore import Qt
from random import randint
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.coord = []
        self.do_paint = False
        self.pushButton.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            qp.setBrush(Qt.yellow)
            for i in self.coord:
                x, y, d = i
                qp.drawEllipse(x, y, d, d)
            qp.end()
            self.do_paint = False

    def paint(self):
        d = randint(10, 80)
        x, y = randint(d, self.size().width() - d), randint(d, self.size().height() - d)
        self.coord.append([x, y, d])
        self.do_paint = True
        self.repaint()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
