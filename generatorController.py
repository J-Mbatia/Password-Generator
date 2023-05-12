from PyQt5.QtWidgets import *
from passwordGenerator import *
import random
import linecache


class Controller(QMainWindow, Ui_GeneratorWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setupUi(self)

        self.displayGenerator.setText('')

        self.checkUppercase.clicked.connect(lambda: self.Uppercase())
        self.checkSymbols.clikced.connect(lambda: self.Symbols())

    def displayPassword(self):
        pass

    def Uppercase(self):
        pass

    def Symbols(self):
        pass
