from PyQt5 import QtCore, QtGui, QtWidgets
import sys


class Ui_checkPassword(object):
    def __init__(self):
        self.statusbar = None
        self.menubar = None
        self.pushButton = None
        self.checkLabel = None
        self.label = None
        self.central_widget = None

    def setupUi(self, check_Password):
        check_Password.setObjectName("checkPassword")
        check_Password.resize(575, 453)
        check_Password.setStyleSheet("background-color: rgb(57, 57, 57);color: rgb(255, 255, 255);")
        self.central_widget = QtWidgets.QWidget(check_Password)
        self.central_widget.setObjectName("central widget")
        self.label = QtWidgets.QLabel(self.central_widget)
        self.label.setGeometry(QtCore.QRect(150, 50, 271, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.checkLabel = QtWidgets.QLabel(self.central_widget)
        self.checkLabel.setGeometry(QtCore.QRect(10, 130, 551, 161))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.checkLabel.setFont(font)
        self.checkLabel.setText("")
        self.checkLabel.setObjectName("checkLabel")
        self.pushButton = QtWidgets.QPushButton(self.central_widget, clicked=lambda: self.exit())
        self.pushButton.setGeometry(QtCore.QRect(220, 330, 131, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        check_Password.setCentralWidget(self.central_widget)
        self.menubar = QtWidgets.QMenuBar(check_Password)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 575, 26))
        self.menubar.setObjectName("menubar")
        check_Password.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(check_Password)
        self.statusbar.setObjectName("statusbar")
        check_Password.setStatusBar(self.statusbar)
        self.translateUi(check_Password)
        QtCore.QMetaObject.connectSlotsByName(check_Password)
    
    def exit(self):
        sys.exit()

    def translateUi(self, check_Password):
        _translate = QtCore.QCoreApplication.translate
        check_Password.setWindowTitle(_translate("checkPassword", "MainWindow"))
        self.label.setText(_translate("checkPassword", "Check User Password"))
        self.pushButton.setText(_translate("checkPassword", "Exit"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    checkPassword = QtWidgets.QMainWindow()
    ui = Ui_checkPassword()
    ui.setupUi(checkPassword)
    checkPassword.show()
    sys.exit(app.exec_())
