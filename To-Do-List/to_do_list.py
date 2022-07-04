from PyQt5 import QtCore, QtGui, QtWidgets
import sys


class Ui_CreateList(object):
    def __init__(self):
        self.deleteItemButton = None
        self.statusbar = None
        self.menubar = None
        self.myList_Widget = None
        self.lineEdit = None
        self.clearAllButton = None
        self.addItemButton = None
        self.central_widget = None

    def setupUi(self, Create_List):
        Create_List.setObjectName("CreateList")
        Create_List.resize(462, 496)
        self.central_widget = QtWidgets.QWidget(Create_List)
        self.central_widget.setObjectName("central widget")
        self.addItemButton = QtWidgets.QPushButton(self.central_widget, clicked=lambda: self.add_it())
        self.addItemButton.setGeometry(QtCore.QRect(10, 70, 141, 41))
        self.addItemButton.setObjectName("addItemButton")
        self.deleteItemButton = QtWidgets.QPushButton(self.central_widget, clicked=lambda: self.delete_it())
        self.deleteItemButton.setGeometry(QtCore.QRect(160, 70, 141, 41))
        self.deleteItemButton.setObjectName("deleteItemButton")
        self.clearAllButton = QtWidgets.QPushButton(self.central_widget, clicked=lambda: self.clear_it())
        self.clearAllButton.setGeometry(QtCore.QRect(310, 70, 141, 41))
        self.clearAllButton.setObjectName("clearAllButton")
        self.lineEdit = QtWidgets.QLineEdit(self.central_widget)
        self.lineEdit.setGeometry(QtCore.QRect(10, 20, 441, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.myList_Widget = QtWidgets.QListWidget(self.central_widget)
        self.myList_Widget.setGeometry(QtCore.QRect(10, 120, 431, 321))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.myList_Widget.setFont(font)
        self.myList_Widget.setObjectName("myList_Widget")
        Create_List.setCentralWidget(self.central_widget)
        self.menubar = QtWidgets.QMenuBar(Create_List)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 462, 26))
        self.menubar.setObjectName("menubar")
        Create_List.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Create_List)
        self.statusbar.setObjectName("statusbar")
        Create_List.setStatusBar(self.statusbar)
        self.translate_Ui(Create_List)
        QtCore.QMetaObject.connectSlotsByName(Create_List)

    def add_it(self):
        item = self.lineEdit.text()
        self.myList_Widget.addItem(item)
        self.lineEdit.setText("")

    def delete_it(self):
        clicked = self.myList_Widget.currentRow()
        self.myList_Widget.takeItem(clicked)

    def clear_it(self):
        self.myList_Widget.clear()

    def translate_Ui(self, Create_List):
        _translate = QtCore.QCoreApplication.translate
        Create_List.setWindowTitle(_translate("CreateList", "To-Do List"))
        self.addItemButton.setText(_translate("CreateList", "Add Item To List"))
        self.deleteItemButton.setText(_translate("CreateList", "Delete Item From List"))
        self.clearAllButton.setText(_translate("CreateList", "Clear The List"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    CreateList = QtWidgets.QMainWindow()
    ui = Ui_CreateList()
    ui.setupUi(CreateList)
    CreateList.show()
    sys.exit(app.exec_())
