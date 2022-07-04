from PyQt5 import QtCore, QtGui, QtWidgets
import sys


class Ui_calculator(object):
    def __init__(self):
        self.statusbar = None
        self.menubar = None
        self.zeroButton = None
        self.decimalButton = None
        self.equalButton = None
        self.plusminusButton = None
        self.twoButton = None
        self.threeButton = None
        self.addButton = None
        self.oneButton = None
        self.fiveButton = None
        self.sixButton = None
        self.fourButton = None
        self.minusButton = None
        self.eightButton = None
        self.nineButton = None
        self.multiplyButton = None
        self.sevenButton = None
        self.divideButton = None
        self.arrowButton = None
        self.cButton = None
        self.percentButton = None
        self.outputLabel = None
        self.central_widget = None

    def setupUi(self, calculator):
        calculator.setObjectName("calculator")
        calculator.resize(361, 568)
        self.central_widget = QtWidgets.QWidget(calculator)
        self.central_widget.setObjectName("central widget")
        self.outputLabel = QtWidgets.QLabel(self.central_widget)
        self.outputLabel.setGeometry(QtCore.QRect(10, 10, 341, 91))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.outputLabel.setFont(font)
        self.outputLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.outputLabel.setFrameShadow(QtWidgets.QFrame.Raised)
        self.outputLabel.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.outputLabel.setObjectName("outputLabel")
        self.percentButton = QtWidgets.QPushButton(self.central_widget, clicked=lambda: self.press_it("%"))
        self.percentButton.setGeometry(QtCore.QRect(10, 110, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.percentButton.setFont(font)
        self.percentButton.setObjectName("percentButton")
        self.cButton = QtWidgets.QPushButton(self.central_widget, clicked=lambda: self.press_it("C"))
        self.cButton.setGeometry(QtCore.QRect(100, 110, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.cButton.setFont(font)
        self.cButton.setObjectName("cButton")
        self.arrowButton = QtWidgets.QPushButton(self.central_widget, clicked=lambda: self.remove_it())
        self.arrowButton.setGeometry(QtCore.QRect(190, 110, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.arrowButton.setFont(font)
        self.arrowButton.setObjectName("arrowButton")
        self.divideButton = QtWidgets.QPushButton(self.central_widget, clicked=lambda: self.press_it("/"))
        self.divideButton.setGeometry(QtCore.QRect(275, 110, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.divideButton.setFont(font)
        self.divideButton.setObjectName("divideButton")
        self.sevenButton = QtWidgets.QPushButton(self.central_widget, clicked=lambda: self.press_it("7"))
        self.sevenButton.setGeometry(QtCore.QRect(10, 190, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.sevenButton.setFont(font)
        self.sevenButton.setObjectName("sevenButton")
        self.multiplyButton = QtWidgets.QPushButton(self.central_widget, clicked=lambda: self.press_it("*"))
        self.multiplyButton.setGeometry(QtCore.QRect(275, 190, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.multiplyButton.setFont(font)
        self.multiplyButton.setObjectName("multiplyButton")
        self.nineButton = QtWidgets.QPushButton(self.central_widget, clicked=lambda: self.press_it("9"))
        self.nineButton.setGeometry(QtCore.QRect(190, 190, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.nineButton.setFont(font)
        self.nineButton.setObjectName("nineButton")
        self.eightButton = QtWidgets.QPushButton(self.central_widget, clicked=lambda: self.press_it("8"))
        self.eightButton.setGeometry(QtCore.QRect(100, 190, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.eightButton.setFont(font)
        self.eightButton.setObjectName("eightButton")
        self.fourButton = QtWidgets.QPushButton(self.central_widget, clicked=lambda: self.press_it("4"))
        self.fourButton.setGeometry(QtCore.QRect(10, 270, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.fourButton.setFont(font)
        self.fourButton.setObjectName("fourButton")
        self.minusButton = QtWidgets.QPushButton(self.central_widget, clicked=lambda: self.press_it("-"))
        self.minusButton.setGeometry(QtCore.QRect(275, 270, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.minusButton.setFont(font)
        self.minusButton.setObjectName("minusButton")
        self.sixButton = QtWidgets.QPushButton(self.central_widget, clicked=lambda: self.press_it("6"))
        self.sixButton.setGeometry(QtCore.QRect(190, 270, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.sixButton.setFont(font)
        self.sixButton.setObjectName("sixButton")
        self.fiveButton = QtWidgets.QPushButton(self.central_widget, clicked=lambda: self.press_it("5"))
        self.fiveButton.setGeometry(QtCore.QRect(100, 270, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.fiveButton.setFont(font)
        self.fiveButton.setObjectName("fiveButton")
        self.oneButton = QtWidgets.QPushButton(self.central_widget, clicked=lambda: self.press_it("1"))
        self.oneButton.setGeometry(QtCore.QRect(10, 350, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.oneButton.setFont(font)
        self.oneButton.setObjectName("oneButton")
        self.addButton = QtWidgets.QPushButton(self.central_widget, clicked=lambda: self.press_it("+"))
        self.addButton.setGeometry(QtCore.QRect(275, 350, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.addButton.setFont(font)
        self.addButton.setObjectName("addButton")
        self.threeButton = QtWidgets.QPushButton(self.central_widget, clicked=lambda: self.press_it("3"))
        self.threeButton.setGeometry(QtCore.QRect(190, 350, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.threeButton.setFont(font)
        self.threeButton.setObjectName("threeButton")
        self.twoButton = QtWidgets.QPushButton(self.central_widget, clicked=lambda: self.press_it("2"))
        self.twoButton.setGeometry(QtCore.QRect(100, 350, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.twoButton.setFont(font)
        self.twoButton.setObjectName("twoButton")
        self.plusminusButton = QtWidgets.QPushButton(self.central_widget, clicked=lambda: self.plus_minus_it())
        self.plusminusButton.setGeometry(QtCore.QRect(10, 430, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.plusminusButton.setFont(font)
        self.plusminusButton.setObjectName("plusminusButton")
        self.equalButton = QtWidgets.QPushButton(self.central_widget, clicked=lambda: self.math_it())
        self.equalButton.setGeometry(QtCore.QRect(275, 430, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.equalButton.setFont(font)
        self.equalButton.setObjectName("equalButton")
        self.decimalButton = QtWidgets.QPushButton(self.central_widget, clicked=lambda: self.dot_it())
        self.decimalButton.setGeometry(QtCore.QRect(190, 430, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.decimalButton.setFont(font)
        self.decimalButton.setObjectName("decimalButton")
        self.zeroButton = QtWidgets.QPushButton(self.central_widget, clicked=lambda: self.press_it("0"))
        self.zeroButton.setGeometry(QtCore.QRect(100, 430, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.zeroButton.setFont(font)
        self.zeroButton.setObjectName("zeroButton")
        calculator.setCentralWidget(self.central_widget)
        self.menubar = QtWidgets.QMenuBar(calculator)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 361, 26))
        self.menubar.setObjectName("menubar")
        calculator.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(calculator)
        self.statusbar.setObjectName("statusbar")
        calculator.setStatusBar(self.statusbar)
        self.translateUi(calculator)
        QtCore.QMetaObject.connectSlotsByName(calculator)

    def math_it(self):
        screen = self.outputLabel.text()
        try:
            answer = eval(screen)
            self.outputLabel.setText(str(answer))
        except:
            self.outputLabel.setText("ERROR")

    def remove_it(self):
        screen = self.outputLabel.text()
        screen = screen[:-1]
        self.outputLabel.setText(screen)

    def plus_minus_it(self):
        screen = self.outputLabel.text()
        if "-" in screen:
            self.outputLabel.setText(screen.replace("-", ""))
        else:
            self.outputLabel.setText(f'-{screen}')

    def dot_it(self):
        screen = self.outputLabel.text()
        if screen[-1] == ".":
            pass
        else:
            self.outputLabel.setText(f'{screen}.')

    def press_it(self, pressed):
        if pressed == "C":
            self.outputLabel.setText("0")
        else:
            if self.outputLabel.text() == "0":
                self.outputLabel.setText("")
            self.outputLabel.setText(f'{self.outputLabel.text()}{pressed}')

    def translateUi(self, calculator):
        _translate = QtCore.QCoreApplication.translate
        calculator.setWindowTitle(_translate("calculator", "Calculator"))
        self.outputLabel.setText(_translate("calculator", "0"))
        self.percentButton.setText(_translate("calculator", "%"))
        self.cButton.setText(_translate("calculator", "C"))
        self.arrowButton.setText(_translate("calculator", "<<"))
        self.divideButton.setText(_translate("calculator", "/"))
        self.sevenButton.setText(_translate("calculator", "7"))
        self.multiplyButton.setText(_translate("calculator", "*"))
        self.nineButton.setText(_translate("calculator", "9"))
        self.eightButton.setText(_translate("calculator", "8"))
        self.fourButton.setText(_translate("calculator", "4"))
        self.minusButton.setText(_translate("calculator", "-"))
        self.sixButton.setText(_translate("calculator", "6"))
        self.fiveButton.setText(_translate("calculator", "5"))
        self.oneButton.setText(_translate("calculator", "1"))
        self.addButton.setText(_translate("calculator", "+"))
        self.threeButton.setText(_translate("calculator", "3"))
        self.twoButton.setText(_translate("calculator", "2"))
        self.plusminusButton.setText(_translate("calculator", "+/-"))
        self.equalButton.setText(_translate("calculator", "="))
        self.decimalButton.setText(_translate("calculator", "."))
        self.zeroButton.setText(_translate("calculator", "0"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    calcu = QtWidgets.QMainWindow()
    ui = Ui_calculator()
    ui.setupUi(calcu)
    calcu.show()
    sys.exit(app.exec_())
