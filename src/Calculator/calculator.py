from PyQt5 import QtWidgets
from PyQt5.Qt import Qt
from ui_calculator import Ui_Calculator
import re
import matlib


class CalculatorWindow(QtWidgets.QMainWindow, Ui_Calculator):
    functions = ['!', '^']
    operators = ['+', '-', '*', '/']
    typing = True

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

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_0 or event.key() == Qt.Key_1 or \
                event.key() == Qt.Key_2 or event.key() == Qt.Key_3 or \
                event.key() == Qt.Key_4 or event.key() == Qt.Key_5 or \
                event.key() == Qt.Key_6 or event.key() == Qt.Key_7 or \
                event.key() == Qt.Key_8 or event.key() == Qt.Key_9:
            self.number_pressed(event.text())
        elif event.key() == Qt.Key_Backspace:
            self.delete_pressed()
        elif event.key() == Qt.Key_Plus:
            self.plus_pressed()
        elif event.key() == Qt.Key_Minus:
            self.minus_pressed()
        elif event.key() == Qt.Key_Asterisk:
            self.mult_pressed()
        elif event.key() == Qt.Key_Slash:
            self.div_pressed()
        elif event.key() == Qt.Key_Enter or event.key() == Qt.Key_Return:
            self.equal_pressed()
        elif event.key() == Qt.Key_Period or event.key() == Qt.Key_Comma:
            self.decimal_pressed()
        elif event.key() == Qt.Key_ParenLeft:
            self.left_bracket_pressed()
        elif event.key() == Qt.Key_ParenRight:
            self.right_bracket_pressed()

    def number_pressed(self, key = None):
        btn = self.sender()
        lcd_str = self.display.text()

        if key is not None:
            btn_text = key
        else:
            btn_text = btn.text()

        if (lcd_str[0] == '0' and len(lcd_str) == 1 and btn_text != '.') or (self.typing == False and not self.operator_control(lcd_str[-1])):
            lcd_str = ''
            lcd_result = lcd_str + btn_text
            self.display.setText(lcd_result)
        elif lcd_str[-1] == '!':
            lcd_result = lcd_str
            self.display.setText(lcd_result)
        else:
            lcd_result = lcd_str + btn_text
            self.display.setText(lcd_result)

        self.typing = True

    def decimal_pressed(self):
        lcd_str = self.display.text()
        if lcd_str[-1] == '.' or self.operator_control(lcd_str[-1]) or lcd_str[-1] in self.functions:
            lcd_result = lcd_str
        else:
            lcd_result = lcd_str + '.'

        self.display.setText(lcd_result)

    def plus_pressed(self):
        lcd_str = self.display.text()
        if not self.operator_control(lcd_str[-1]) and lcd_str[-1] != '.':
            lcd_result = lcd_str + '+'
        else:
            lcd_result = lcd_str

        self.display.setText(lcd_result)

    def minus_pressed(self):
        lcd_str = self.display.text()
        if len(lcd_str) == 1 and lcd_str == '0':
            lcd_str = ''
            lcd_result = lcd_str + '-'
        elif not self.operator_control(lcd_str[-1]) and lcd_str[-1] != '.':
            lcd_result = lcd_str + '-'

        else:
            lcd_result = lcd_str

        self.display.setText(lcd_result)

    def mult_pressed(self):
        lcd_str = self.display.text()
        if not self.operator_control(lcd_str[-1]) and lcd_str[-1] != '.':
            lcd_result = lcd_str + '*'
        else:
            lcd_result = lcd_str

        self.display.setText(lcd_result)

    def div_pressed(self):
        lcd_str = self.display.text()
        if not self.operator_control(lcd_str[-1]) and lcd_str[-1] != '.':
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
        self.typing = False

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
        if lcd_str[-1] != '.' and lcd_str[-1] != '^':
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
        if lcd_str[-1] != '^' and lcd_str[-1] != '.':
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
        if lcd_str[0] == '0' and len(lcd_str) == 1:
            lcd_result = '('
        elif self.operator_control(lcd_str[-1]):
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
        second_num = ''

        # TODO: [1] Add functionality for log() and nroot()
        #       [2] Done /Numbers
        #       [3] Add priority for operators while evaluating
        #       [4] Add priority for brackets while evaluating
        #       [5] Add functionality for Errors
        #       [6] Done / Connect to keyboard

        if lcd_str[-1] in self.operators:
            raise ValueError("Expression ends with operator")

        print(lcd_str)
        number_arr = re.findall(r'[-]?\d*\.?\d+|[-+]?\d+', lcd_str)
        print(number_arr)
        result_num = re.findall(r'[-]?\d*\.?\d+|[-+]?\d+', lcd_str)[0]
        counter_neg = 0    # variable to check if first number is negative
        for c in range(len(lcd_str)):
            # cycle finds operator between first number and second number
            if float(result_num) < 0 and counter_neg == 0:
                #  when first number is negative cycle ignor first operator to next in
                c +=1
                counter_neg +=1
            else:
                if (lcd_str[c] in self.operators) or (lcd_str[c] in self.functions):
                    if lcd_str[c] != '!':
                        new_str = lcd_str[c + 1:]
                        second_num = re.findall(r'[-+]?\d*\.\d+|\d+', new_str)[0]
                        print("Here First argument " + result_num)
                        print("Here Second argument  " + second_num)
                    else:
                        pass


                    if lcd_str[c] == '+':
                        result_num = format(matlib.add(float(result_num), float(second_num)), '.15g')
                        print(result_num)
                    elif lcd_str[c] == '-':
                        result_num = format(matlib.sub(float(result_num), float(second_num)), '.15g')
                    elif lcd_str[c] == '*':
                        result_num = format(matlib.mul(float(result_num), float(second_num)), '.15g')
                    elif lcd_str[c] == '/':
                        result_num = format(matlib.div(float(result_num), float(second_num)), '.15g')
                    elif lcd_str[c] == '!':
                        result_num = format(matlib.factorial(float(result_num)), '.15g')
                    elif lcd_str[c] == '^':
                        result_num = format(matlib.pow(float(result_num), float(second_num)), '.15g')
                else:
                    pass

        if result_num == '-0':
            result_num = '0'

        lcd_result = format(float(result_num), '.15g')
        self.display.setText(lcd_result)
        self.typing = False


    def operator_control(self, operator):
        #  function controls if last charackter in string is operator
        for char in self.operators:
            if operator == char:
                return True
