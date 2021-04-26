###########################################
# IVS projekt 2 - Calculator GUI / Help   #
# author: Abikenova Zhamilya              #
###########################################

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_HelpCalc(object):
    def setupUi(self, HelpCalc):
        HelpCalc.setObjectName("HelpCalc")
        HelpCalc.resize(620, 500)
        self.centralwidget = QtWidgets.QWidget(HelpCalc)
        self.centralwidget.setObjectName("centralwidget")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(0, 0, 620, 500))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.plainTextEdit.setReadOnly(True)
        HelpCalc.setCentralWidget(self.centralwidget)

        self.retranslateUi(HelpCalc)
        QtCore.QMetaObject.connectSlotsByName(HelpCalc)

    def retranslateUi(self, HelpCalc):
        _translate = QtCore.QCoreApplication.translate
        HelpCalc.setWindowTitle(_translate("HelpCalc", "Help"))
        self.plainTextEdit.setPlainText(_translate("HelpCalc", "AC         Clear all of the calculation.\n"
                    "            \n"
                    "log(n)   Logarithmic function. Base 10 is the default setting. \'n\' is number greater than 0.\n"
                    "              Examples: log(10), log(50-20+3).\n"
                    "                     \n"
                    "n!           Factorial function where \'n\' is number greater than 0. Examples: 5!, (1+4)!\n"
                    "                     \n"
                    "n√x       Power root function. Default root n is 2, \'x\' - number or math expression. \n"
                    "              Examples: 3√(8), √(5+11).\n"
                    "                     \n"
                    "x^n       Power function, where \'x\' is number and \'n\' is power number. \n"
                    "              Examples: 3^2, (-3)^2, 2^(5-9). \n"
                    "                     \n"
                    "Ans       Stores the result of the last calculation performed.\n"
                    "                     \n"
                    ".             Decimal point.\n"
                    "                     \n"
                    "(  )         Parenthesis.\n"
                    "                     \n"
                    "=           Calculate math expression.\n"
                    "\n"
                    "DEL       Delete last sign. \n"
                    "\n"
                    "+           Addition. Examples: 2+2, 5+3√(5+11)\n"
                    "\n"
                    "-            Subtraction. Examples: 2-2, 5-3√(11)\n"
                    "\n"
                    "/            Division. Examples: 3/2, 3/(-2), log(10)/2^2.\n"
                    "\n"
                    "*            Multiplication. 3*2, log(5*10)"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    HelpCalc = QtWidgets.QMainWindow()
    ui = Ui_HelpCalc()
    ui.setupUi(HelpCalc)
    HelpCalc.show()
    sys.exit(app.exec_())
