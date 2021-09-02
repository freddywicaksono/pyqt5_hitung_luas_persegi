import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from decimal import Decimal

qtcreator_file  = "persegi.ui" # Enter file here.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtcreator_file)


class MyWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.btnHitung.clicked.connect(self.hitung)

    def hitung(self):
        panjang = Decimal(self.txtPanjang.text())
        lebar = Decimal(self.txtLebar.text())
        luas = panjang * lebar
        self.txtLuas.setText(str(luas))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())