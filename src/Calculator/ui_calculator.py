from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Calculator(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(319, 399)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 80, 321, 321))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.btn_dot = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_dot.setMinimumSize(QtCore.QSize(61, 61))
        self.btn_dot.setMaximumSize(QtCore.QSize(61, 61))
        self.btn_dot.setStyleSheet("")
        self.btn_dot.setObjectName("btn_dot")
        self.gridLayout.addWidget(self.btn_dot, 4, 2, 1, 1)
        self.btn_div = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_div.setMinimumSize(QtCore.QSize(61, 61))
        self.btn_div.setMaximumSize(QtCore.QSize(61, 61))
        self.btn_div.setStyleSheet("")
        self.btn_div.setObjectName("btn_div")
        self.gridLayout.addWidget(self.btn_div, 3, 4, 1, 1)
        self.btn3 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn3.setMinimumSize(QtCore.QSize(61, 61))
        self.btn3.setMaximumSize(QtCore.QSize(61, 61))
        self.btn3.setStyleSheet("")
        self.btn3.setObjectName("btn3")
        self.gridLayout.addWidget(self.btn3, 3, 3, 1, 1)
        self.btn6 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn6.setMinimumSize(QtCore.QSize(61, 61))
        self.btn6.setMaximumSize(QtCore.QSize(61, 61))
        self.btn6.setStyleSheet("")
        self.btn6.setObjectName("btn6")
        self.gridLayout.addWidget(self.btn6, 2, 3, 1, 1)
        self.btn2 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn2.setMinimumSize(QtCore.QSize(61, 61))
        self.btn2.setMaximumSize(QtCore.QSize(61, 61))
        self.btn2.setStyleSheet("")
        self.btn2.setObjectName("btn2")
        self.gridLayout.addWidget(self.btn2, 3, 2, 1, 1)
        self.btn4 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn4.setMinimumSize(QtCore.QSize(61, 61))
        self.btn4.setMaximumSize(QtCore.QSize(61, 61))
        self.btn4.setStyleSheet("")
        self.btn4.setObjectName("btn4")
        self.gridLayout.addWidget(self.btn4, 2, 1, 1, 1)
        self.btn_minus = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_minus.setMinimumSize(QtCore.QSize(61, 61))
        self.btn_minus.setMaximumSize(QtCore.QSize(61, 61))
        self.btn_minus.setStyleSheet("")
        self.btn_minus.setObjectName("btn_minus")
        self.gridLayout.addWidget(self.btn_minus, 1, 4, 1, 1)
        self.btn_mult = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_mult.setMinimumSize(QtCore.QSize(61, 61))
        self.btn_mult.setMaximumSize(QtCore.QSize(61, 61))
        self.btn_mult.setStyleSheet("")
        self.btn_mult.setObjectName("btn_mult")
        self.gridLayout.addWidget(self.btn_mult, 2, 4, 1, 1)
        self.btn5 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn5.setMinimumSize(QtCore.QSize(61, 61))
        self.btn5.setMaximumSize(QtCore.QSize(61, 61))
        self.btn5.setStyleSheet("")
        self.btn5.setObjectName("btn5")
        self.gridLayout.addWidget(self.btn5, 2, 2, 1, 1)
        self.btn0 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn0.setMinimumSize(QtCore.QSize(61, 61))
        self.btn0.setMaximumSize(QtCore.QSize(61, 61))
        self.btn0.setStyleSheet("")
        self.btn0.setObjectName("btn0")
        self.gridLayout.addWidget(self.btn0, 4, 1, 1, 1)
        self.btn_left_b = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_left_b.setMinimumSize(QtCore.QSize(61, 61))
        self.btn_left_b.setMaximumSize(QtCore.QSize(61, 61))
        self.btn_left_b.setStyleSheet("")
        self.btn_left_b.setObjectName("btn_left_b")
        self.gridLayout.addWidget(self.btn_left_b, 0, 2, 1, 1)
        self.btn_right_b = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_right_b.setMinimumSize(QtCore.QSize(61, 61))
        self.btn_right_b.setMaximumSize(QtCore.QSize(61, 61))
        self.btn_right_b.setStyleSheet("")
        self.btn_right_b.setObjectName("btn_right_b")
        self.gridLayout.addWidget(self.btn_right_b, 0, 3, 1, 1)
        self.btn_result = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_result.setMinimumSize(QtCore.QSize(61, 61))
        self.btn_result.setMaximumSize(QtCore.QSize(61, 61))
        self.btn_result.setStyleSheet("")
        self.btn_result.setObjectName("btn_result")
        self.gridLayout.addWidget(self.btn_result, 4, 4, 1, 1)
        self.btn1 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn1.setMinimumSize(QtCore.QSize(61, 61))
        self.btn1.setMaximumSize(QtCore.QSize(61, 61))
        self.btn1.setStyleSheet("")
        self.btn1.setObjectName("btn1")
        self.gridLayout.addWidget(self.btn1, 3, 1, 1, 1)
        self.btn_delete = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_delete.setMinimumSize(QtCore.QSize(61, 61))
        self.btn_delete.setMaximumSize(QtCore.QSize(61, 61))
        self.btn_delete.setStyleSheet("")
        self.btn_delete.setObjectName("btn_delete")
        self.gridLayout.addWidget(self.btn_delete, 0, 1, 1, 1)
        self.btn_plusminus = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_plusminus.setMinimumSize(QtCore.QSize(61, 61))
        self.btn_plusminus.setMaximumSize(QtCore.QSize(61, 61))
        self.btn_plusminus.setStyleSheet("")
        self.btn_plusminus.setObjectName("btn_plusminus")
        self.gridLayout.addWidget(self.btn_plusminus, 4, 3, 1, 1)
        self.btn_clear = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_clear.setMinimumSize(QtCore.QSize(61, 61))
        self.btn_clear.setMaximumSize(QtCore.QSize(61, 61))
        self.btn_clear.setStyleSheet("")
        self.btn_clear.setObjectName("btn_clear")
        self.gridLayout.addWidget(self.btn_clear, 0, 0, 1, 1)
        self.btn_log = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_log.setMinimumSize(QtCore.QSize(61, 61))
        self.btn_log.setMaximumSize(QtCore.QSize(61, 61))
        self.btn_log.setStyleSheet("")
        self.btn_log.setObjectName("btn_log")
        self.gridLayout.addWidget(self.btn_log, 1, 0, 1, 1)
        self.btn7 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn7.setMinimumSize(QtCore.QSize(61, 61))
        self.btn7.setMaximumSize(QtCore.QSize(61, 61))
        self.btn7.setStyleSheet("")
        self.btn7.setObjectName("btn7")
        self.gridLayout.addWidget(self.btn7, 1, 1, 1, 1)
        self.btn_fact = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_fact.setMinimumSize(QtCore.QSize(61, 61))
        self.btn_fact.setMaximumSize(QtCore.QSize(61, 61))
        self.btn_fact.setStyleSheet("")
        self.btn_fact.setObjectName("btn_fact")
        self.gridLayout.addWidget(self.btn_fact, 2, 0, 1, 1)
        self.btn8 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn8.setMinimumSize(QtCore.QSize(61, 61))
        self.btn8.setMaximumSize(QtCore.QSize(61, 61))
        self.btn8.setStyleSheet("")
        self.btn8.setObjectName("btn8")
        self.gridLayout.addWidget(self.btn8, 1, 2, 1, 1)
        self.btn_sqrt = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_sqrt.setMinimumSize(QtCore.QSize(61, 61))
        self.btn_sqrt.setMaximumSize(QtCore.QSize(61, 61))
        self.btn_sqrt.setStyleSheet("")
        self.btn_sqrt.setObjectName("btn_sqrt")
        self.gridLayout.addWidget(self.btn_sqrt, 3, 0, 1, 1)
        self.btn9 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn9.setMinimumSize(QtCore.QSize(61, 61))
        self.btn9.setMaximumSize(QtCore.QSize(61, 61))
        self.btn9.setStyleSheet("")
        self.btn9.setObjectName("btn9")
        self.gridLayout.addWidget(self.btn9, 1, 3, 1, 1)
        self.btn_exp = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_exp.setMinimumSize(QtCore.QSize(61, 61))
        self.btn_exp.setMaximumSize(QtCore.QSize(61, 61))
        self.btn_exp.setStyleSheet("")
        self.btn_exp.setObjectName("btn_exp")
        self.gridLayout.addWidget(self.btn_exp, 4, 0, 1, 1)
        self.btn_plus = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_plus.setMinimumSize(QtCore.QSize(61, 61))
        self.btn_plus.setMaximumSize(QtCore.QSize(61, 61))
        self.btn_plus.setStyleSheet("")
        self.btn_plus.setObjectName("btn_plus")
        self.gridLayout.addWidget(self.btn_plus, 0, 4, 1, 1)
        self.display = QtWidgets.QLabel(self.centralwidget)
        self.display.setGeometry(QtCore.QRect(8, 10, 303, 71))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.display.setFont(font)
        self.display.setStyleSheet("QLabel {\n"
"    qproperty-alignment:\'AlignVCenter | AlignRight\';\n"
"    border: 1px solid gray;\n"
"}\n"
"\n"
"background-color: white;")
        self.display.setObjectName("display")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_dot.setText(_translate("MainWindow", "."))
        self.btn_div.setText(_translate("MainWindow", "/"))
        self.btn3.setText(_translate("MainWindow", "3"))
        self.btn6.setText(_translate("MainWindow", "6"))
        self.btn2.setText(_translate("MainWindow", "2"))
        self.btn4.setText(_translate("MainWindow", "4"))
        self.btn_minus.setText(_translate("MainWindow", "-"))
        self.btn_mult.setText(_translate("MainWindow", "*"))
        self.btn5.setText(_translate("MainWindow", "5"))
        self.btn0.setText(_translate("MainWindow", "0"))
        self.btn_left_b.setText(_translate("MainWindow", "("))
        self.btn_right_b.setText(_translate("MainWindow", ")"))
        self.btn_result.setText(_translate("MainWindow", "="))
        self.btn1.setText(_translate("MainWindow", "1"))
        self.btn_delete.setText(_translate("MainWindow", "del"))
        self.btn_plusminus.setText(_translate("MainWindow", "+/-"))
        self.btn_clear.setText(_translate("MainWindow", "C"))
        self.btn_log.setText(_translate("MainWindow", "log"))
        self.btn7.setText(_translate("MainWindow", "7"))
        self.btn_fact.setText(_translate("MainWindow", "x!"))
        self.btn8.setText(_translate("MainWindow", "8"))
        self.btn_sqrt.setText(_translate("MainWindow", "sqrt"))
        self.btn9.setText(_translate("MainWindow", "9"))
        self.btn_exp.setText(_translate("MainWindow", "e"))
        self.btn_plus.setText(_translate("MainWindow", "+"))
        self.display.setText(_translate("MainWindow", "0"))
