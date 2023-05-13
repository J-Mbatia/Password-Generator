from PyQt5 import QtWidgets
from PyQt5 import QtCore, Qt

import generatorController
from passCraftGUI import Ui_MainScreen
from generatorController import Controller
from checkerController import Controller
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)


class MainScreenController:

    def __init__(self):
        self.app = QtWidgets.QApplication([])
        self.main_screen = QtWidgets.QMainWindow()
        self.ui = Ui_MainScreen()
        self.ui.setupUi(self.main_screen)
        self.ui.generatorButton.clicked.connect(self.open_generator)
        self.ui.checkerButton.clicked.connect(self.open_checker)

    def open_generator(self):
        self.generatorController = generatorController.Controller()
        self.generatorController.show()

    def open_checker(self):
        self.checkerController = Controller()
        self.checkerController.show()

    def run(self):
        self.main_screen.show()
        self.app.exec_()


if __name__ == '__main__':
    controller = MainScreenController()
    controller.run()