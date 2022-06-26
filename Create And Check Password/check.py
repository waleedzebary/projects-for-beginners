from PyQt5 import QtCore, QtGui, QtWidgets
from CheckUserPassword import Ui_checkPassword
from main import checker_password
import sys


class Ui_CheckPassword(object):
    def __init__(self):
        self.statusbar = None
        self.menubar = None
        self.label_2 = None
        self.lineEdit = None
        self.label = None
        self.ui = None
        self.window = None
        self.exitButton = None
        self.checkButton = None
        self.central_widget = None

    def openWindowCheckPassword(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_checkPassword()
        self.ui.setupUi(self.window)
        self.window.show()

    def setupUi(self, Main_Window):
        Main_Window.setObjectName("MainWindow")
        Main_Window.resize(487, 433)
        Main_Window.setStyleSheet("background-color: rgb(57, 57, 57);color: rgb(255, 255, 255);")
        self.central_widget = QtWidgets.QWidget(Main_Window)
        self.central_widget.setObjectName("central widget")
        self.checkButton = QtWidgets.QPushButton(self.central_widget, clicked=lambda: self.check())
        self.checkButton.setGeometry(QtCore.QRect(100, 280, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.checkButton.setFont(font)
        self.checkButton.setObjectName("checkButton")
        self.exitButton = QtWidgets.QPushButton(self.central_widget, clicked=lambda: self.exit())
        self.exitButton.setGeometry(QtCore.QRect(290, 280, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.exitButton.setFont(font)
        self.exitButton.setObjectName("exitButton")
        self.label = QtWidgets.QLabel(self.central_widget)
        self.label.setGeometry(QtCore.QRect(110, 40, 281, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.central_widget)
        self.lineEdit.setGeometry(QtCore.QRect(32, 140, 431, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(self.central_widget)
        self.label_2.setGeometry(QtCore.QRect(30, 190, 291, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        Main_Window.setCentralWidget(self.central_widget)
        self.menubar = QtWidgets.QMenuBar(Main_Window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 487, 26))
        self.menubar.setObjectName("menubar")
        Main_Window.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Main_Window)
        self.statusbar.setObjectName("statusbar")
        Main_Window.setStatusBar(self.statusbar)
        self.translateUi(Main_Window)
        QtCore.QMetaObject.connectSlotsByName(Main_Window)

    def check(self):
        userPassword = self.lineEdit.text()
        check_password = checker_password(str(userPassword))
        self.openWindowCheckPassword()
        self.ui.checkLabel.setText(str(check_password))

    def exit(self):
        sys.exit()

    def translateUi(self, Main_Window):
        _translate = QtCore.QCoreApplication.translate
        Main_Window.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.checkButton.setText(_translate("MainWindow", "Check"))
        self.exitButton.setText(_translate("MainWindow", "Exit"))
        self.label.setText(_translate("MainWindow", "Check Your Password"))
        self.label_2.setText(_translate("MainWindow", "Please Enter Your Password"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_CheckPassword()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
