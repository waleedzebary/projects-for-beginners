from PyQt5 import QtCore, QtGui, QtWidgets
from printPassword import Ui_PrintPassword
import string
import random
import sys


class Ui_CreatePassword(object):
    def __init__(self):
        self.window = None
        self.ui = None
        self.password = []
        self.statusbar = None
        self.menubar = None
        self.ExitButton = None
        self.label_2 = None
        self.SpecialCharacters = None
        self.Numbers = None
        self.LowerLetters = None
        self.UpperLetters = None
        self.CreateButton = None
        self.label = None
        self.lineEdit = None
        self.central_widget = None
        self.upper = string.ascii_uppercase
        self.lower = string.ascii_lowercase
        self.number = string.digits
        self.specialCharacters = string.punctuation

    def openWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_PrintPassword()
        self.ui.setupUi(self.window)
        self.window.show()

    def setupUi(self, Create_Password):
        Create_Password.setObjectName("CreatePassword")
        Create_Password.resize(602, 612)
        Create_Password.setStyleSheet("background-color: rgb(57, 57, 57);\n""color: rgb(255, 255, 255);")
        self.central_widget = QtWidgets.QWidget(Create_Password)
        self.central_widget.setObjectName("central widget")
        self.lineEdit = QtWidgets.QLineEdit(self.central_widget)
        self.lineEdit.setGeometry(QtCore.QRect(140, 130, 321, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("color: rgb(20, 20, 20);\n""background-color: rgb(225, 225, 225);\n")
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(self.central_widget)
        self.label.setGeometry(QtCore.QRect(130, 40, 361, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setStyleSheet("")
        self.label.setObjectName("label")
        self.CreateButton = QtWidgets.QPushButton(self.central_widget, clicked=lambda: self.createPassword())
        self.CreateButton.setGeometry(QtCore.QRect(140, 470, 131, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.CreateButton.setFont(font)
        self.CreateButton.setStyleSheet("background-color: rgb(234, 234, 234);\n""color: rgb(0, 0, 0);")
        self.CreateButton.setObjectName("CreateButton")
        self.UpperLetters = QtWidgets.QCheckBox(self.central_widget)
        self.UpperLetters.setGeometry(QtCore.QRect(140, 209, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.UpperLetters.setFont(font)
        self.UpperLetters.setStyleSheet("\n""background-color: rgb(57, 57, 57);")
        self.UpperLetters.setObjectName("UpperLetters")
        self.LowerLetters = QtWidgets.QCheckBox(self.central_widget)
        self.LowerLetters.setGeometry(QtCore.QRect(140, 250, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.LowerLetters.setFont(font)
        self.LowerLetters.setStyleSheet("background-color: rgb(57, 57, 57);")
        self.LowerLetters.setObjectName("LowerLetters")
        self.Numbers = QtWidgets.QCheckBox(self.central_widget)
        self.Numbers.setGeometry(QtCore.QRect(140, 289, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Numbers.setFont(font)
        self.Numbers.setStyleSheet("background-color: rgb(57, 57, 57);\n""")
        self.Numbers.setObjectName("Numbers")
        self.SpecialCharacters = QtWidgets.QCheckBox(self.central_widget)
        self.SpecialCharacters.setGeometry(QtCore.QRect(140, 330, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.SpecialCharacters.setFont(font)
        self.SpecialCharacters.setStyleSheet("background-color: rgb(57, 57, 57);\n""")
        self.SpecialCharacters.setObjectName("SpecialCharacters")
        self.label_2 = QtWidgets.QLabel(self.central_widget)
        self.label_2.setGeometry(QtCore.QRect(50, 390, 521, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.ExitButton = QtWidgets.QPushButton(self.central_widget, clicked=lambda: self.exit())
        self.ExitButton.setGeometry(QtCore.QRect(340, 470, 131, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.ExitButton.setFont(font)
        self.ExitButton.setStyleSheet("background-color: rgb(234, 234, 234);\n""color: rgb(0, 0, 0);")
        self.ExitButton.setObjectName("ExitButton")
        Create_Password.setCentralWidget(self.central_widget)
        self.menubar = QtWidgets.QMenuBar(Create_Password)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 602, 26))
        self.menubar.setObjectName("menubar")
        Create_Password.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Create_Password)
        self.statusbar.setObjectName("statusbar")
        Create_Password.setStatusBar(self.statusbar)
        self.translateUi(Create_Password)
        QtCore.QMetaObject.connectSlotsByName(Create_Password)

    def check_box(self):
        length = self.lineEdit.text()
        if self.LowerLetters.isChecked():
            password_list1 = []
            for i in range(int(length)):
                password_list1.append(random.choice(self.lower))
            random.shuffle(password_list1)
            self.password = ("".join(password_list1))
        if self.UpperLetters.isChecked():
            password_list2 = []
            for i in range(int(length)):
                password_list2.append(random.choice(self.upper))
            random.shuffle(password_list2)
            self.password = ("".join(password_list2))
        if self.Numbers.isChecked():
            password_list3 = []
            for i in range(int(length)):
                password_list3.append(random.choice(self.number))
            random.shuffle(password_list3)
            self.password = ("".join(password_list3))
        if self.SpecialCharacters.isChecked():
            password_list4 = []
            for i in range(int(length)):
                password_list4.append(random.choice(self.specialCharacters))
            random.shuffle(password_list4)
            self.password = ("".join(password_list4))
        if self.LowerLetters.isChecked() and self.UpperLetters.isChecked():
            password_list5 = []
            for i in range(int(length)):
                password_list5.append(random.choice(self.lower + self.upper))
            random.shuffle(password_list5)
            self.password = ("".join(password_list5))
        if self.LowerLetters.isChecked() and self.Numbers.isChecked():
            password_list6 = []
            for i in range(int(length)):
                password_list6.append(random.choice(self.lower + self.number))
            random.shuffle(password_list6)
            self.password = ("".join(password_list6))
        if self.LowerLetters.isChecked() and self.SpecialCharacters.isChecked():
            password_list7 = []
            for i in range(int(length)):
                password_list7.append(random.choice(self.lower + self.specialCharacters))
            random.shuffle(password_list7)
            self.password = ("".join(password_list7))
        if self.LowerLetters.isChecked() and self.UpperLetters.isChecked() and self.Numbers.isChecked():
            password_list8 = []
            for i in range(int(length)):
                password_list8.append(random.choice(self.lower + self.upper + self.number))
            random.shuffle(password_list8)
            self.password = ("".join(password_list8))
        if self.LowerLetters.isChecked() and self.Numbers.isChecked() and self.SpecialCharacters.isChecked():
            password_list9 = []
            for i in range(int(length)):
                password_list9.append(random.choice(self.lower + self.upper + self.specialCharacters))
            random.shuffle(password_list9)
            self.password = ("".join(password_list9))
        if self.LowerLetters.isChecked() and self.UpperLetters.isChecked() and self.Numbers.isChecked() \
                and self.SpecialCharacters.isChecked():
            password_list10 = []
            for i in range(int(length)):
                password_list10.append(random.choice(self.lower + self.upper + self.number + self.specialCharacters))
            random.shuffle(password_list10)
            self.password = ("".join(password_list10))
        if self.UpperLetters.isChecked() and self.Numbers.isChecked():
            password_list11 = []
            for i in range(int(length)):
                password_list11.append(random.choice(self.upper + self.number))
            random.shuffle(password_list11)
            self.password = ("".join(password_list11))
        if self.UpperLetters.isChecked() and self.SpecialCharacters.isChecked():
            password_list12 = []
            for i in range(int(length)):
                password_list12.append(random.choice(self.upper + self.specialCharacters))
            random.shuffle(password_list12)
            self.password = ("".join(password_list12))
        if self.UpperLetters.isChecked() and self.Numbers.isChecked() and self.SpecialCharacters.isChecked():
            password_list13 = []
            for i in range(int(length)):
                password_list13.append(random.choice(self.upper + self.number + self.specialCharacters))
            random.shuffle(password_list13)
            self.password = ("".join(password_list13))
        if self.Numbers.isChecked() and self.SpecialCharacters.isChecked():
            password_list14 = []
            for i in range(int(length)):
                password_list14.append(random.choice(self.number + self.specialCharacters))
            random.shuffle(password_list14)
            self.password = ("".join(password_list14))
        return self.password

    def createPassword(self):
        password = self.check_box()
        self.openWindow()
        self.ui.textEdit.setText(str(password))

    def exit(self):
        sys.exit()

    def translateUi(self, Create_Password):
        _translate = QtCore.QCoreApplication.translate
        Create_Password.setWindowTitle(_translate("CreatePassword", "MainWindow"))
        self.label.setText(_translate("CreatePassword", "Create Password Generator"))
        self.CreateButton.setText(_translate("CreatePassword", "Create"))
        self.UpperLetters.setText(_translate("CreatePassword", "Upper Letters"))
        self.LowerLetters.setText(_translate("CreatePassword", "Lower Letters"))
        self.Numbers.setText(_translate("CreatePassword", "Numbers"))
        self.SpecialCharacters.setText(_translate("CreatePassword", "Special Characters"))
        self.label_2.setText(_translate("CreatePassword", "Choose options to configure the password"))
        self.ExitButton.setText(_translate("CreatePassword", "Exit"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    CreatePassword = QtWidgets.QMainWindow()
    ui = Ui_CreatePassword()
    ui.setupUi(CreatePassword)
    CreatePassword.show()
    sys.exit(app.exec_())
