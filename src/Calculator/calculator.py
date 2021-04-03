from PyQt5 import QtWidgets
from ui_calculator import Ui_Calculator
import re
import matlib


class CalculatorWindow(QtWidgets.QMainWindow, Ui_Calculator):
    functions = ['!', '^']
    operators = ['+', '-', '*', '/']

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()

        self.btn0.pressed.connect(self.number_pressed)
        self.btn1.pressed.connect(self.number_pressed)
        self.btn2.pressed.connect(self.number_pressed)
        self.btn3.pressed.connect(self.number_pressed)
        self.btn4.pressed.connect(self.number_pressed)
        self.btn5.pressed.connect(self.number_pressed)
        self.btn6.pressed.connect(self.number_pressed)
        self.btn7.pressed.connect(self.number_pressed)
        self.btn8.pressed.connect(self.number_pressed)
        self.btn9.pressed.connect(self.number_pressed)

        self.btn_plus.pressed.connect(self.plus_pressed)
        self.btn_minus.pressed.connect(self.minus_pressed)
        self.btn_mult.pressed.connect(self.mult_pressed)
        self.btn_div.pressed.connect(self.div_pressed)

        self.btn_dot.pressed.connect(self.decimal_pressed)
        self.btn_result.pressed.connect(self.equal_pressed)
        self.btn_delete.pressed.connect(self.delete_pressed)
        self.btn_clear.pressed.connect(self.clear_pressed)
        self.btn_left_b.pressed.connect(self.left_bracket_pressed)
        self.btn_right_b.pressed.connect(self.right_bracket_pressed)

        self.btn_plusminus.pressed.connect(self.unary_operator_pressed)
        self.btn_fact.pressed.connect(self.fact_pressed)
        self.btn_log.pressed.connect(self.log_pressed)
        self.btn_exp.pressed.connect(self.power_pressed)
        self.btn_sqrt.pressed.connect(self.sqrt_pressed)

    def number_pressed(self):
        btn = self.sender()
        lcd_str = self.display.text()
        if lcd_str[0] == '0' and len(lcd_str) == 1 and btn.text() != '.':
            lcd_str = ''
            lcd_result = lcd_str + btn.text()
            self.display.setText(lcd_result)
        elif lcd_str[-1] == '!':
            lcd_result = lcd_str
            self.display.setText(lcd_result)
        else:
            lcd_result = lcd_str + btn.text()
            self.display.setText(lcd_result)

    def decimal_pressed(self):
        lcd_str = self.display.text()
        if '.' not in lcd_str:
            lcd_result = lcd_str + '.'
        else:
            lcd_result = lcd_str

        self.display.setText(lcd_result)

    def plus_pressed(self):
        lcd_str = self.display.text()
        if not self.operator_control(lcd_str[-1]):
            lcd_result = lcd_str + '+'
        else:
            lcd_result = lcd_str

        self.display.setText(lcd_result)

    def minus_pressed(self):
        lcd_str = self.display.text()
        if not self.operator_control(lcd_str[-1]):
            lcd_result = lcd_str + '-'
        else:
            lcd_result = lcd_str

        self.display.setText(lcd_result)

    def mult_pressed(self):
        lcd_str = self.display.text()
        if not self.operator_control(lcd_str[-1]):
            lcd_result = lcd_str + '*'
        else:
            lcd_result = lcd_str

        self.display.setText(lcd_result)

    def div_pressed(self):
        lcd_str = self.display.text()
        if not self.operator_control(lcd_str[-1]):
            lcd_result = lcd_str + '/'
        else:
            lcd_result = lcd_str

        self.display.setText(lcd_result)

    def delete_pressed(self):
        lcd_str = self.display.text()

        if len(lcd_str) == 1 or lcd_str == '0':
            self.clear_pressed()
        else:
            lcd_result = lcd_str[:-1]
            self.display.setText(lcd_result)

    def clear_pressed(self):
        self.display.setText('0')

    def unary_operator_pressed(self):
        lcd_str = self.display.text()
        try:
            lcd_digit = float(lcd_str)
            lcd_digit *= -1
            self.display.setText(format(lcd_digit, '.15g'))
        except ValueError:
            pass

    def fact_pressed(self):
        lcd_str = self.display.text()
        if lcd_str[-1] != '!':
            lcd_result = lcd_str + '!'
        else:
            lcd_result = lcd_str

        self.display.setText(lcd_result)

    def log_pressed(self):
        lcd_str = self.display.text()
        if lcd_str[0] == '0' and len(lcd_str) == 1:
            lcd_str = ''
            lcd_result = lcd_str + 'log('
        elif self.operator_control(lcd_str[-1]):
            lcd_result = lcd_str + 'log('
        else:
            lcd_result = lcd_str

        self.display.setText(lcd_result)

    def power_pressed(self):
        lcd_str = self.display.text()
        if lcd_str[-1] != '^':
            lcd_result = lcd_str + '^'
        else:
            lcd_result = lcd_str

        self.display.setText(lcd_result)

    def sqrt_pressed(self):
        lcd_str = self.display.text()

        if self.operator_control(lcd_str[-1]):
            lcd_result = lcd_str + '\u221a'
        elif lcd_str[0] == '0' and len(lcd_str) == 1:
            lcd_result = '\u221a'
        else:
            lcd_result = lcd_str

        self.display.setText(lcd_result)

    def left_bracket_pressed(self):
        lcd_str = self.display.text()
        if self.operator_control(lcd_str[-1]):
            lcd_result = lcd_str + '('
        else:
            lcd_result = lcd_str

        self.display.setText(lcd_result)

    def right_bracket_pressed(self):
        lcd_str = self.display.text()
        lcd_result = lcd_str + ')'
        self.display.setText(lcd_result)

    def equal_pressed(self):
        lcd_str = self.display.text()
        result_num = 0
        counter = -1

        # TODO: [1] Add functionality for log() and nroot()
        #       [2] Change number's property - number could
        #           have more than 1 digit or could be decimal
        #       [3] Add priority for operators while evaluating
        #       [4] Add priority for brackets while evaluating
        #       [5] Add functionality for Errors

        if lcd_str[-1] in self.operators:
            raise ValueError("Expression ends with operator")

        for c in range(len(lcd_str)):
            if counter == c:
                continue
            if (lcd_str[c] in self.operators) or (lcd_str[c] in self.functions):
                if lcd_str[c] != '!':
                    second_num = int(lcd_str[c + 1])
                else:
                    pass

                if lcd_str[c] == '+':
                    result_num = matlib.add(result_num, second_num)
                    counter = c + 1
                elif lcd_str[c] == '-':
                    result_num = matlib.sub(result_num, second_num)
                    counter = c + 1
                elif lcd_str[c] == '*':
                    result_num = matlib.mul(result_num, second_num)
                    counter = c + 1
                elif lcd_str[c] == '/':
                    result_num = matlib.div(result_num, second_num)
                    counter = c + 1
                elif lcd_str[c] == '!':
                    result_num = matlib.factorial(result_num)
                    counter = c + 1
                elif lcd_str[c] == '^':
                    result_num = matlib.pow(result_num, second_num)
                    counter = c + 1
            else:
                result_num = int(lcd_str[c])

        lcd_result = format(result_num, '.15g')
        self.display.setText(lcd_result)


    def operator_control(self, operator):
        #  function controls if last charackter in string is operator
        for char in self.operators:
            if operator == char:
                return True

