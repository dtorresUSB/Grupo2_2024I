import sys
import PyQt5.QtWidgets as PyQt
from PyQt5 import uic
import serial
import time
from serial_robot import comunicar

class Principal(PyQt.QMainWindow):
    def __init__(self):
        super().__init__()
        self.initGUI()
        self.show()

    def initGUI(self):
        uic.loadUi('app.ui',self)
        self.boton.clicked.connect(self.operacion)

    def operacion(self):
        ang=self.angulo.text()
        line=comunicar(ang)
        self.dato.setText(str(line[-1]))

def main():
    app = PyQt.QApplication([])
    window = Principal()
    sys.exit(app.exec_())

if __name__=="__main__":
    main()