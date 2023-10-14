from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(250, 274)
        font = QtGui.QFont()
        font.setItalic(True)
        font.setUnderline(False)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("background-color: purple;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.cl_number = QtWidgets.QCheckBox(self.centralwidget)
        self.cl_number.setGeometry(QtCore.QRect(40, 120, 181, 17))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.cl_number.setFont(font)
        self.cl_number.setStyleSheet("background-color: yellow;\n"
"color: blue;\n"
"border: 2px solid black;\n"
"")
        self.cl_number.setObjectName("cl_number")
        self.cl_alphabet = QtWidgets.QCheckBox(self.centralwidget)
        self.cl_alphabet.setGeometry(QtCore.QRect(40, 150, 201, 17))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.cl_alphabet.setFont(font)
        self.cl_alphabet.setStyleSheet("background-color: yellow;\n"
"color: blue;\n"
"border: 2px solid black;")
        self.cl_alphabet.setObjectName("cl_alphabet")
        self.btn_OK = QtWidgets.QPushButton(self.centralwidget)
        self.btn_OK.setGeometry(QtCore.QRect(70, 190, 81, 23))
        self.btn_OK.setStyleSheet("color: blue;\n"
"background-color: yellow;\n"
"border: 2px solid black;\n"
"border-radius: 5px;")
        self.btn_OK.setObjectName("btn_OK")
        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(40, 20, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.title.setFont(font)
        self.title.setStyleSheet("background-color: yellow;\n"
"color: blue;\n"
"border: 2px solid black;\n"
"border-radius: 5px;")
        self.title.setObjectName("title")
        self.result = QtWidgets.QLabel(self.centralwidget)
        self.result.setGeometry(QtCore.QRect(40, 80, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.result.setFont(font)
        self.result.setStyleSheet("background-color: yellow;\n"
"color: blue;\n"
"border: 2px solid black;\n"
"border-radius: 5px;")
        self.result.setObjectName("result")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 250, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.cl_number.setText(_translate("MainWindow", "Використовувати числа"))
        self.cl_alphabet.setText(_translate("MainWindow", "Використовувати алфавіт"))
        self.btn_OK.setText(_translate("MainWindow", "Згенерувати"))
        self.title.setText(_translate("MainWindow", "Генератор паролів"))
        self.result.setText(_translate("MainWindow", "Тут буде результат"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
