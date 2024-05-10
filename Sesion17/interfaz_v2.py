import sys
import PyQt5.QtWidgets as PyQt
from PyQt5 import uic

class Principal(PyQt.QMainWindow):
    def __init__(self):
        super().__init__()
        self.initGUI()
        self.show()

    def initGUI(self):
        uic.loadUi('app.ui',self)
        self.calcular.clicked.connect(self.imprimir)

    def imprimir(self):
        if self.suma.isChecked()==True:
            a=self.num1.text()
            b=self.num2.text()
            self.respuesta.setText(str(int(a)+int(b)))

def main():
    app = PyQt.QApplication([])
    window = Principal()
    sys.exit(app.exec_())

if __name__=="__main__":
    main()