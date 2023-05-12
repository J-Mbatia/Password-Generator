# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'passwordChecker.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_CheckerWindow(object):
    def setupUi(self, CheckerWindow):
        CheckerWindow.setObjectName("CheckerWindow")
        CheckerWindow.resize(400, 500)
        CheckerWindow.setMinimumSize(QtCore.QSize(400, 500))
        CheckerWindow.setMaximumSize(QtCore.QSize(400, 500))
        self.centralwidget = QtWidgets.QWidget(CheckerWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.titlePasswordGenerator = QtWidgets.QLabel(self.centralwidget)
        self.titlePasswordGenerator.setGeometry(QtCore.QRect(80, 20, 291, 161))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.titlePasswordGenerator.setFont(font)
        self.titlePasswordGenerator.setWordWrap(False)
        self.titlePasswordGenerator.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.titlePasswordGenerator.setObjectName("titlePasswordGenerator")
        self.typePassword = QtWidgets.QLineEdit(self.centralwidget)
        self.typePassword.setGeometry(QtCore.QRect(110, 200, 181, 31))
        self.typePassword.setObjectName("typePassword")
        self.labelPassword = QtWidgets.QLabel(self.centralwidget)
        self.labelPassword.setGeometry(QtCore.QRect(150, 180, 101, 16))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        self.labelPassword.setFont(font)
        self.labelPassword.setObjectName("labelPassword")
        self.displayStrength = QtWidgets.QTextBrowser(self.centralwidget)
        self.displayStrength.setGeometry(QtCore.QRect(150, 350, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        self.displayStrength.setFont(font)
        self.displayStrength.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.displayStrength.setAutoFillBackground(False)
        self.displayStrength.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.displayStrength.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.displayStrength.setObjectName("displayStrength")
        self.labelStrength = QtWidgets.QLabel(self.centralwidget)
        self.labelStrength.setGeometry(QtCore.QRect(170, 320, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        self.labelStrength.setFont(font)
        self.labelStrength.setObjectName("labelStrength")
        self.checkCharacters = QtWidgets.QCheckBox(self.centralwidget)
        self.checkCharacters.setGeometry(QtCore.QRect(150, 240, 111, 18))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(11)
        self.checkCharacters.setFont(font)
        self.checkCharacters.setObjectName("checkCharacters")
        self.checkPassword = QtWidgets.QPushButton(self.centralwidget)
        self.checkPassword.setGeometry(QtCore.QRect(160, 270, 75, 23))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        self.checkPassword.setFont(font)
        self.checkPassword.setObjectName("checkPassword")
        self.displayRequirement = QtWidgets.QLabel(self.centralwidget)
        self.displayRequirement.setGeometry(QtCore.QRect(70, 410, 281, 41))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(10)
        self.displayRequirement.setFont(font)
        self.displayRequirement.setText("")
        self.displayRequirement.setObjectName("displayRequirement")
        CheckerWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(CheckerWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 400, 22))
        self.menubar.setObjectName("menubar")
        CheckerWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(CheckerWindow)
        self.statusbar.setObjectName("statusbar")
        CheckerWindow.setStatusBar(self.statusbar)

        self.retranslateUi(CheckerWindow)
        QtCore.QMetaObject.connectSlotsByName(CheckerWindow)

    def retranslateUi(self, CheckerWindow):
        _translate = QtCore.QCoreApplication.translate
        CheckerWindow.setWindowTitle(_translate("CheckerWindow", "MainWindow"))
        self.titlePasswordGenerator.setText(_translate("CheckerWindow", "Password Checker"))
        self.labelPassword.setText(_translate("CheckerWindow", "Enter Password"))
        self.labelStrength.setText(_translate("CheckerWindow", "STRENGTH"))
        self.checkCharacters.setText(_translate("CheckerWindow", "Hide Characters"))
        self.checkPassword.setText(_translate("CheckerWindow", "Check"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CheckerWindow = QtWidgets.QMainWindow()
    ui = Ui_CheckerWindow()
    ui.setupUi(CheckerWindow)
    CheckerWindow.show()
    sys.exit(app.exec_())
