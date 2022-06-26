from PyQt5 import QtCore, QtGui, QtWidgets
from check import Ui_CheckPassword
from createPassword import Ui_CreatePassword
import sys


class Ui_MainWindow(object):

    def __init__(self):
        self.statusbar = None
        self.menubar = None
        self.label = None
        self.CheckRadioButton = None
        self.CreateRadioButton = None
        self.ExitButton = None
        self.SubmitButton = None
        self.central_widget = None
        self.ui = None
        self.window = None

    def openWindowCreatePassword(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_CreatePassword()
        self.ui.setupUi(self.window)
        self.window.show()

    def openWindowCheckPassword(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_CheckPassword()
        self.ui.setupUi(self.window)
        self.window.show()

    def setupUi(self, Main_Window):
        Main_Window.setObjectName("MainWindow")
        Main_Window.resize(405, 442)
        Main_Window.setStyleSheet("background-color: rgb(57, 57, 57);\n""color: rgb(255, 255, 255);")
        self.central_widget = QtWidgets.QWidget(Main_Window)
        self.central_widget.setObjectName("central widget")
        self.SubmitButton = QtWidgets.QPushButton(self.central_widget, clicked=lambda: self.select())
        self.SubmitButton.setGeometry(QtCore.QRect(58, 320, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.SubmitButton.setFont(font)
        self.SubmitButton.setStyleSheet("background-color: rgb(234, 234, 234);\n""color: rgb(0, 0, 0);")
        self.SubmitButton.setObjectName("SubmitButton")
        self.ExitButton = QtWidgets.QPushButton(self.central_widget, clicked=lambda: self.exit())
        self.ExitButton.setGeometry(QtCore.QRect(240, 320, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.ExitButton.setFont(font)
        self.ExitButton.setStyleSheet("background-color: rgb(234, 234, 234);\n""color: rgb(0, 0, 0);")
        self.ExitButton.setObjectName("ExitButton")
        self.CreateRadioButton = QtWidgets.QRadioButton(self.central_widget)
        self.CreateRadioButton.setGeometry(QtCore.QRect(90, 30, 241, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.CreateRadioButton.setFont(font)
        self.CreateRadioButton.setObjectName("CreateRadioButton")
        self.CheckRadioButton = QtWidgets.QRadioButton(self.central_widget)
        self.CheckRadioButton.setGeometry(QtCore.QRect(90, 80, 241, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.CheckRadioButton.setFont(font)
        self.CheckRadioButton.setObjectName("CheckRadioButton")
        self.label = QtWidgets.QLabel(self.central_widget)
        self.label.setGeometry(QtCore.QRect(60, 190, 291, 71))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        Main_Window.setCentralWidget(self.central_widget)
        self.menubar = QtWidgets.QMenuBar(Main_Window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 405, 26))
        self.menubar.setObjectName("menubar")
        Main_Window.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Main_Window)
        self.statusbar.setObjectName("statusbar")
        Main_Window.setStatusBar(self.statusbar)
        self.CreateRadioButton.setChecked(True)
        self.translateUi(Main_Window)
        QtCore.QMetaObject.connectSlotsByName(Main_Window)

    def select(self):
        if self.CreateRadioButton.isChecked():
            self.openWindowCreatePassword()
        if self.CheckRadioButton.isChecked():
            self.openWindowCheckPassword()

    def exit(self):
        sys.exit()

    def translateUi(self, Main_Window):
        _translate = QtCore.QCoreApplication.translate
        Main_Window.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.SubmitButton.setText(_translate("MainWindow", "Submit"))
        self.ExitButton.setText(_translate("MainWindow", "Exit"))
        self.CreateRadioButton.setText(_translate("MainWindow", "Create Password"))
        self.CheckRadioButton.setText(_translate("MainWindow", "Check Password"))
        self.label.setText(_translate("MainWindow", "Choose Your Topping"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
