from PyQt5 import QtCore, QtGui, QtWidgets
import sys


class Ui_PrintPassword(object):
    def __init__(self):
        self.statusbar = None
        self.menubar = None
        self.pushButton = None
        self.textEdit = None
        self.label = None
        self.central_widget = None

    def setupUi(self, Main_Window):
        Main_Window.setObjectName("MainWindow")
        Main_Window.resize(553, 432)
        Main_Window.setStyleSheet("background-color: rgb(57, 57, 57);\n""color: rgb(255, 255, 255);")
        self.central_widget = QtWidgets.QWidget(Main_Window)
        self.central_widget.setObjectName("central widget")
        self.label = QtWidgets.QLabel(self.central_widget)
        self.label.setGeometry(QtCore.QRect(120, 50, 301, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.textEdit = QtWidgets.QTextEdit(self.central_widget)
        self.textEdit.setGeometry(QtCore.QRect(20, 190, 521, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.textEdit.setFont(font)
        self.textEdit.setObjectName("textEdit")
        self.pushButton = QtWidgets.QPushButton(self.central_widget, clicked=lambda: self.exit())
        self.pushButton.setGeometry(QtCore.QRect(210, 300, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        Main_Window.setCentralWidget(self.central_widget)
        self.menubar = QtWidgets.QMenuBar(Main_Window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 553, 26))
        self.menubar.setObjectName("menubar")
        Main_Window.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Main_Window)
        self.statusbar.setObjectName("statusbar")
        Main_Window.setStatusBar(self.statusbar)

        self.translateUi(Main_Window)
        QtCore.QMetaObject.connectSlotsByName(Main_Window)

    def exit(self):
        sys.exit()

    def translateUi(self, Main_Window):
        _translate = QtCore.QCoreApplication.translate
        Main_Window.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Here Is Your Password"))
        self.pushButton.setText(_translate("MainWindow", "Exit"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_PrintPassword()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
