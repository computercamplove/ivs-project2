from PyQt5 import QtWidgets
from ui_calculator import Ui_Calculator
import re
import matlib

class CalculatorWindow(QtWidgets.QMainWindow, Ui_Calculator):

    first_number = None
    typing = False  # to check if second number still typynig
    equal = False

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()

        #connect buttons
        self.btn0.clicked.connect(self.number_pressed)
        self.btn1.clicked.connect(self.number_pressed)
        self.btn2.clicked.connect(self.number_pressed)
        self.btn3.clicked.connect(self.number_pressed)
        self.btn4.clicked.connect(self.number_pressed)
        self.btn5.clicked.connect(self.number_pressed)
        self.btn6.clicked.connect(self.number_pressed)
        self.btn7.clicked.connect(self.number_pressed)
        self.btn8.clicked.connect(self.number_pressed)
        self.btn9.clicked.connect(self.number_pressed)

        self.btn_dot.clicked.connect(self.decimal_pressed)
        self.btn_plusminus.clicked.connect(self.unary_operator_pressed)

        self.btn_clear.clicked.connect(self.clear_pressed)
        self.btn_delete.clicked.connect(self.delete_pressed)
        self.btn_left_b.clicked.connect(self.bracket_pressed)
        self.btn_right_b.clicked.connect(self.bracket_pressed)

        self.btn_minus.clicked.connect(self.binary_operator_pressed)
        self.btn_plus.clicked.connect(self.binary_operator_pressed)
        self.btn_div.clicked.connect(self.binary_operator_pressed)
        self.btn_mult.clicked.connect(self.binary_operator_pressed)

        self.btn_result.clicked.connect(self.equals_pressed)

        self.btn_minus.setCheckable(True)
        self.btn_plus.setCheckable(True)
        self.btn_div.setCheckable(True)
        self.btn_mult.setCheckable(True)



    def number_pressed(self):
        btn = self.sender()
        plus = self.btn_plus.isChecked()
        minus = self.btn_minus.isChecked()
        mult = self.btn_mult.isChecked()
        div = self.btn_div.isChecked()

        if self.equal:
            label_num_str = ''
            self.equal = False
        else:
            label_num_str = self.display.text()

        if (plus or minus or mult or div) and (not self.typing):
            result_label = btn.text()
            self.typing = True
        else:
            if '.' not in label_num_str:
                result_label = format(float(label_num_str + btn.text()), '.15g')
            else: #if 0 after "."
                result_label = label_num_str + btn.text()

        self.display.setText(result_label)
    
    def decimal_pressed(self):
        if '.' in self.display.text():
            pass
        else:
            self.display.setText(self.display.text() + '.')

    def unary_operator_pressed(self):
        label_number = float(self.display.text())
        label_number *= -1
        result_label = format(label_number, '.15g')

        self.display.setText(result_label)

    def clear_pressed(self):
        self.typing = False
        self.equal = False
        self.btn_minus.setChecked(False)
        self.btn_plus.setChecked(False)
        self.btn_div.setChecked(False)
        self.btn_mult.setChecked(False)

        self.display.setText('0')

    def delete_pressed(self):
        label_number_str = self.display.text()

        if len(label_number_str) == 1 or label_number_str == '0':
            self.clear_pressed()
        else:
            result_label = label_number_str[:-1]
            self.display.setText(result_label)
    

    def binary_operator_pressed(self):
        btn = self.sender()
        self.first_number = float(self.display.text())

        btn.setChecked(True)

    def equals_pressed(self):
        second_number = float(self.display.text())
        self.equal = True
        if self.btn_plus.isChecked():
            label_number = matlib.add(self.first_number, second_number)
            self.display.setText(format(label_number, '.15g'))
            self.btn_plus.setChecked(False)
        elif self.btn_minus.isChecked():
            label_number = matlib.sub(self.first_number, second_number)
            self.display.setText(format(label_number, '.15g'))
            self.btn_minus.setChecked(False)
        elif self.btn_mult.isChecked():
            label_number = matlib.mul(self.first_number, second_number)
            self.display.setText(format(label_number, '.15g'))
            self.btn_mult.setChecked(False)
        elif self.btn_div.isChecked(): ##if button '/' pressed
            label_number = matlib.div(self.first_number, second_number)
            self.display.setText(format(label_number, '.15g'))
            self.btn_div.setChecked(False)

        self.typing = False  #done to type second number

        












    def bracket_pressed(self):

        # TODO: add more functionality after creating
        #   slot for binary operators
        
        btn = self.sender()
        label_number_str = self.display.text()

        if btn.text() == '(':
            if re.match(r"[\+\-\/\*]", label_number_str[-1]):
                self.display.setText(self.display.text() + '(')
        else: #button text is ")"
            if not re.match(r"[\+\-\/\*]", label_number_str[-1]):
                self.display.setText(self.display.text() + ')')




