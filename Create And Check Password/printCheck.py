from PyQt5 import QtCore, QtGui, QtWidgets
import sys


class Ui_printCheck(object):
    def __init__(self):
        self.statusbar = None
        self.menubar = None
        self.label_2 = None
        self.TimeLabel = None
        self.TriesLabel = None
        self.label_3 = None
        self.CheckLabel = None
        self.label = None
        self.ExitButton = None
        self.central_widget = None

    def setupUi(self, print_Check):
        print_Check.setObjectName("printCheck")
        print_Check.resize(568, 573)
        print_Check.setStyleSheet("background-color: rgb(57, 57, 57);color: rgb(255, 255, 255)")
        self.central_widget = QtWidgets.QWidget(print_Check)
        self.central_widget.setObjectName("central widget")
        self.ExitButton = QtWidgets.QPushButton(self.central_widget, clicked=lambda: self.exit())
        self.ExitButton.setGeometry(QtCore.QRect(240, 440, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.ExitButton.setFont(font)
        self.ExitButton.setObjectName("ExitButton")
        self.label = QtWidgets.QLabel(self.central_widget)
        self.label.setGeometry(QtCore.QRect(10, 40, 241, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.CheckLabel = QtWidgets.QLabel(self.central_widget)
        self.CheckLabel.setGeometry(QtCore.QRect(270, 35, 281, 171))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.CheckLabel.setFont(font)
        self.CheckLabel.setText("")
        self.CheckLabel.setObjectName("CheckLabel")
        self.label_3 = QtWidgets.QLabel(self.central_widget)
        self.label_3.setGeometry(QtCore.QRect(10, 235, 201, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.TriesLabel = QtWidgets.QLabel(self.central_widget)
        self.TriesLabel.setGeometry(QtCore.QRect(240, 240, 221, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.TriesLabel.setFont(font)
        self.TriesLabel.setText("")
        self.TriesLabel.setObjectName("TriesLabel")
        self.TimeLabel = QtWidgets.QLabel(self.central_widget)
        self.TimeLabel.setGeometry(QtCore.QRect(10, 350, 211, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.TimeLabel.setFont(font)
        self.TimeLabel.setObjectName("TimeLabel")
        self.label_2 = QtWidgets.QLabel(self.central_widget)
        self.label_2.setGeometry(QtCore.QRect(234, 345, 291, 71))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        print_Check.setCentralWidget(self.central_widget)
        self.menubar = QtWidgets.QMenuBar(print_Check)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 568, 26))
        self.menubar.setObjectName("menubar")
        print_Check.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(print_Check)
        self.statusbar.setObjectName("statusbar")
        print_Check.setStatusBar(self.statusbar)
        self.translateUi(print_Check)
        QtCore.QMetaObject.connectSlotsByName(print_Check)

    def exit(self):
        sys.exit()

    def translateUi(self, print_Check):
        _translate = QtCore.QCoreApplication.translate
        print_Check.setWindowTitle(_translate("printCheck", "MainWindow"))
        self.ExitButton.setText(_translate("printCheck", "Exit"))
        self.label.setText(_translate("printCheck", "Check Your Password:"))
        self.label_3.setText(_translate("printCheck", "Tries To Hacking:"))
        self.TimeLabel.setText(_translate("printCheck", "Time To hacking"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    printCheck = QtWidgets.QMainWindow()
    ui = Ui_printCheck()
    ui.setupUi(printCheck)
    printCheck.show()
    sys.exit(app.exec_())
