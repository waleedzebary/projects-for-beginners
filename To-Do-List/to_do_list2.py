from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import sqlite3
import sys


# Create a Database or connect to one
connect = sqlite3.connect('myList.db')
# Create a cursor
cursor = connect.cursor()
# Create a table
cursor.execute("""CREATE TABLE if not exists todo_list(list_item text)""")
# Commit the changes
connect.commit()
# Close our connections
connect.close()


class Ui_CreateList(object):
    def __init__(self):
        self.statusbar = None
        self.menubar = None
        self.save_to_database_Button = None
        self.myList_Widget = None
        self.lineEdit = None
        self.clearAllButton = None
        self.deleteItemButton = None
        self.addItemButton = None
        self.central_widget = None

    def setupUi(self, Create_List):
        Create_List.setObjectName("CreateList")
        Create_List.resize(611, 494)
        self.central_widget = QtWidgets.QWidget(Create_List)
        self.central_widget.setObjectName("central_widget")
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
        self.lineEdit.setGeometry(QtCore.QRect(10, 20, 591, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.myList_Widget = QtWidgets.QListWidget(self.central_widget)
        self.myList_Widget.setGeometry(QtCore.QRect(10, 120, 591, 321))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.myList_Widget.setFont(font)
        self.myList_Widget.setObjectName("myList_Widget")
        self.save_to_database_Button = QtWidgets.QPushButton(self.central_widget, clicked=lambda: self.save_it())
        self.save_to_database_Button.setGeometry(QtCore.QRect(460, 70, 141, 41))
        self.save_to_database_Button.setObjectName("save_to_database_Button")
        Create_List.setCentralWidget(self.central_widget)
        self.menubar = QtWidgets.QMenuBar(Create_List)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 611, 26))
        self.menubar.setObjectName("menubar")
        Create_List.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Create_List)
        self.statusbar.setObjectName("statusbar")
        Create_List.setStatusBar(self.statusbar)
        self.translateUi(Create_List)
        QtCore.QMetaObject.connectSlotsByName(Create_List)
        # Grab all the items from to database
        self.grab_all()

    def grab_all(self):
        # Create a Database or connect to one
        connect1 = sqlite3.connect('myList.db')
        # Create a cursor
        cursor1 = connect1.cursor()
        # Create a table
        cursor1.execute("SELECT * FROM todo_list")
        records = cursor1.fetchall()
        # Commit the changes
        connect1.commit()
        # Close our connections
        connect1.close()
        # Loop records and add to screen
        for record in records:
            self.myList_Widget.addItem(str(record[0]))

    def add_it(self):
        item = self.lineEdit.text()
        self.myList_Widget.addItem(item)
        self.lineEdit.setText("")

    def delete_it(self):
        clicked = self.myList_Widget.currentRow()
        self.myList_Widget.takeItem(clicked)

    def clear_it(self):
        self.myList_Widget.clear()

    def save_it(self):
        # Create a Database or connect to one
        connect2 = sqlite3.connect('myList.db')
        # Create a cursor
        cursor2 = connect2.cursor()
        cursor2.execute('DELETE FROM todo_list;', )
        items = []
        for index in range(self.myList_Widget.count()):
            items.append(self.myList_Widget.item(index))
        for item in items:
            # print(item.text())
            cursor2.execute("INSERT INTO todo_list VALUES (:item)",
                            {
                               'item': item.text(),
                            }
                            )
        # Commit the changes
        connect2.commit()
        # Close our connections
        connect2.close()
        # Pop up Box
        message = QMessageBox()
        message.setWindowTitle("Saved To Database!!!")
        message.setText("Your Information Has Been Saved!")
        message.setIcon(QMessageBox.Information)
        run = message.exec_()

    def translateUi(self, Create_List):
        _translate = QtCore.QCoreApplication.translate
        Create_List.setWindowTitle(_translate("CreateList", "To-Do List"))
        self.addItemButton.setText(_translate("CreateList", "Add Item To List"))
        self.deleteItemButton.setText(_translate("CreateList", "Delete Item From List"))
        self.clearAllButton.setText(_translate("CreateList", "Clear The List"))
        self.save_to_database_Button.setText(_translate("CreateList", "Save To Database"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    CreateList = QtWidgets.QMainWindow()
    ui = Ui_CreateList()
    ui.setupUi(CreateList)
    CreateList.show()
    sys.exit(app.exec_())
