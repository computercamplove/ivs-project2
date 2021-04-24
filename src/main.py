#!/usr/bin/python

##
# @mainpage IVS project documentation
# Doxygen documentation for IVS second project
# Project implements simple calculator. Calculator can be used to calculate addition, subraction, multiplication, division, logarithm, power, n-root.
# Calculator supports parantheses and nesting of parantheses.
# User interacts with Calculator through GUI, which allows easy user-friendly usage.

import sys
from PyQt5.QtWidgets import QApplication
from calculator import CalculatorWindow
from platform import system
app = QApplication(sys.argv)
if system() == 'Linux':
    app.setStyle('Windows')
calculator = CalculatorWindow()

sys.exit(app.exec_())
