from PyQt5 import QtWidgets
from passwordGenerator import Ui_GeneratorWindow
from passwordChecker import Ui_CheckerWindow
from passcraftMainScreen import Ui_MainScreen
from checkerController import Controller


class MainScreenController:

    def __init__(self):
        self.app = QtWidgets.QApplication([])
        self.main_screen = QtWidgets.QMainWindow()
        self.ui = Ui_MainScreen()
        self.ui.setupUi(self.main_screen)
        self.ui.generatorButton.clicked.connect(self.open_generator)
        self.ui.checkerButton.clicked.connect(self.open_checker)

    def open_generator(self):
        self.windowGenerator = QtWidgets.QMainWindow()
        self.generator_ui = Ui_GeneratorWindow()
        self.generator_ui.setupUi(self.windowGenerator)
        self.windowGenerator.show()

    def open_checker(self):
        self.checkerController = Controller()
        self.checkerController.show()

    def run(self):
        self.main_screen.show()
        self.app.exec_()


if __name__ == '__main__':
    controller = MainScreenController()
    controller.run()

