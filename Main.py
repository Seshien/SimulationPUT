import Ball
import PyQt5
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QColor, QPolygon
import sys



class Window(QWidget):
    def __init__(self, parent=None):
        super().__init__()
        self.interfejs()

    def interfejs(self):
        self.resize(800,600)
        self.setWindowTitle("Simulation")
        self.show()

def main():
    app = QApplication(sys.argv)
    okno = Window()
    sys.exit(app.exec_())


if __name__=="__main__":
    main()