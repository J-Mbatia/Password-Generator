from PyQt5.QtWidgets import *
from passwordCheckerGUI import *


class Controller(QMainWindow, Ui_CheckerWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setupUi(self)

        self.typePassword.setText('')
        self.displayStrength.setText('')
        self.displayRequirement.setText('')
        self.checkPassword.clicked.connect(lambda: self.checkPass())
        self.checkCharacters.stateChanged.connect(lambda: self.hideCharacters())

    def checkPass(self):
        symbols = "v\!@#$%^&*()_-+={}[]|\:;'<>,.?/~`"
        numbers = "1234567890"
        password = self.typePassword.text()

        includeSymbols = any(symbol in password for symbol in symbols)
        includeNumbers = any(number in password for number in numbers)
        includeUppercase = any(letter.isupper() for letter in password)

        if len(password) < 8 or (len(password) < 12 and password.isalpha()) or (
                len(password) >= 8 and not includeUppercase) or (len(password) >= 8 and not includeNumbers):
            self.displayStrength.setText('Weak')
            self.displayRequirement.setText('Password should have more than 8 characters, 1 uppercase letter \nand 1 '
                                            'number.')

        elif (8 <= len(password) <= 11 and includeUppercase and includeNumbers) or (
                8 <= len(password) <= 11 and includeNumbers and includeSymbols):
            self.displayStrength.setText('Medium')
            self.displayRequirement.setText('Password should have at least 12 characters, include uppercase \nletters, '
                                            'numbers, and symbols.')

        elif len(password) >= 12 and includeSymbols and includeNumbers and includeUppercase:
            self.displayStrength.setText('Strong')
            self.displayRequirement.setText('')

    def hideCharacters(self):
        if self.checkCharacters.isChecked():
            self.typePassword.setEchoMode(QtWidgets.QLineEdit.PasswordEchoOnEdit)
        else:
            self.typePassword.setEchoMode(QtWidgets.QLineEdit.Normal)