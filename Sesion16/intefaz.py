import PyQt5.QtWidgets as PyQt
from PyQt5.QtCore import Qt

class MyGUI(PyQt.QWidget):
    def __init__(self):
        super().__init__()
        self.initGUI()
        self.show()

    def initGUI(self):
        self.setGeometry(700,150,300,500)
        self.setWindowTitle('Mi primer GUI')

        button = PyQt.QPushButton(self)
        button.setText('Calcular')
        button.setStyleSheet("QPushButton{background-color:white;"\
                             "font-size:36px}")
        button.move(100,300)
        button.resize(150,70)
        
        self.label=PyQt.QLabel(self)
        self.label.move(100,150)
        self.label.resize(150,70)
        self.label.setStyleSheet("QLabel{background-color: purple;"\
                                 "font-weight:bold;font-size:36px}")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.edit=PyQt.QLineEdit(self)
        self.edit.move(100,100)
        self.edit.resize(250,60)
        self.edit.setStyleSheet("QLineEdit{font-size:18px}")

        #-------------- Signal/Slot -----------------
        button.clicked.connect(self.imprimir)
        #--------------------------------------------

    def imprimir(self):
        self.label.setText(self.edit.text())

def main():
    app=PyQt.QApplication([])
    window=MyGUI()
    app.exec_()

if __name__=="__main__":
    main()