from PyQt5 import QtWidgets
from PyQt5.Qt import Qt
from ui_calculator import Ui_Calculator
import matlib


class CalculatorWindow(QtWidgets.QMainWindow, Ui_Calculator):
    """Class used to connect GUI and matlib."""

    def __init__(self):
        """Initializes the calculator."""

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
        """
        Detect if key on keyboard is pressed and calls appropriate method.
        Reacts only on specific keys.
        :param event:
        """

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
        else:
            pass

    def number_pressed(self, key=None):
        """Appends the number to the display."""

        btn = self.sender()  # determines which button is clicked
        lcd_str = self.display.text()

        if key is not None:
            #  if argument is passed to method button takes value of key event
            btn_text = key
        else:
            btn_text = btn.text()

        if not self.lcd_string(lcd_str):
            #  display already contain 27 characters and returns previous input
            lcd_result = lcd_str
        else:
            lcd_result = lcd_str + btn_text

        self.display.setText(lcd_result)

    def decimal_pressed(self):
        """Appends the period to the display."""

        lcd_str = self.display.text()
        if not self.lcd_string(lcd_str):
            #  display already contain 27 characters and returns previous input
            lcd_result = lcd_str
        else:
            lcd_result = lcd_str + '.'

        self.display.setText(lcd_result)

    def plus_pressed(self):
        """Appends the plus '+' character to the display."""

        lcd_str = self.display.text()
        if not self.lcd_string(lcd_str):
            #  display already contain 27 characters and returns previous input
            lcd_result = lcd_str
        else:
            lcd_result = lcd_str + '+'

        self.display.setText(lcd_result)

    def minus_pressed(self):
        """Appends the minus '-' character to the display."""

        lcd_str = self.display.text()
        if not self.lcd_string(lcd_str):
            #  display already contain 27 characters and returns previous input
            lcd_result = lcd_str
        else:
            lcd_result = lcd_str + '-'

        self.display.setText(lcd_result)

    def mult_pressed(self):
        """Appends the asterisk '*' character to the display."""

        lcd_str = self.display.text()
        if not self.lcd_string(lcd_str):
            #  display already contain 27 characters and returns previous input
            lcd_result = lcd_str
        else:
            lcd_result = lcd_str + '*'

        self.display.setText(lcd_result)

    def div_pressed(self):
        """Appends the slash '/' character to the display."""

        lcd_str = self.display.text()
        if not self.lcd_string(lcd_str):
            #  display already contain 27 characters and returns previous input
            lcd_result = lcd_str
        else:
            lcd_result = lcd_str + '/'

        self.display.setText(lcd_result)

    def delete_pressed(self):
        """Delete last character from the display."""

        lcd_str = self.display.text()

        if len(lcd_str) == 1 or lcd_str == '0':
            self.clear_pressed()
        else:
            lcd_result = lcd_str[:-1]
            self.display.setText(lcd_result)

    def clear_pressed(self):
        """Clears the display."""

        self.display.setText('')

    def unary_operator_pressed(self):
        """Negates one number on the display."""
        lcd_str = self.display.text()
        try:
            lcd_digit = float(lcd_str)
            lcd_digit *= -1
            self.display.setText(format(lcd_digit, '.15g'))
        except ValueError:
            pass

    def fact_pressed(self):
        """Appends the exclamation mark '!' to the display."""

        lcd_str = self.display.text()
        if not self.lcd_string(lcd_str):
            #  display already contain 27 characters and returns previous input
            lcd_result = lcd_str
        else:
            lcd_result = lcd_str + '!'

        self.display.setText(lcd_result)

    def log_pressed(self):
        """Appends beginning of function 'log(' to the display."""

        lcd_str = self.display.text()
        if not self.lcd_string(lcd_str):
            #  display already contain 27 characters and returns previous input
            lcd_result = lcd_str
        else:
            lcd_result = lcd_str + "log("

        self.display.setText(lcd_result)

    def power_pressed(self):
        """Appends caret '^' character to the display."""

        lcd_str = self.display.text()
        if not self.lcd_string(lcd_str):
            #  display already contain 27 characters and returns previous input
            lcd_result = lcd_str
        else:
            lcd_result = lcd_str + '^'

        self.display.setText(lcd_result)

    def sqrt_pressed(self):
        """Appends square root character to the display."""

        lcd_str = self.display.text()
        if not self.lcd_string(lcd_str):
            #  display already contain 27 characters and returns previous input
            lcd_result = lcd_str
        else:
            lcd_result = lcd_str + '\u221a'

        self.display.setText(lcd_result)

    def left_bracket_pressed(self):
        """Appends left parenthesis to the display."""

        lcd_str = self.display.text()
        if not self.lcd_string(lcd_str):
            #  display already contain 27 characters and returns previous input
            lcd_result = lcd_str
        else:
            lcd_result = lcd_str + '('

        self.display.setText(lcd_result)

    def right_bracket_pressed(self):
        """Appends right parenthesis to the display."""

        lcd_str = self.display.text()
        if not self.lcd_string(lcd_str):
            #  display already contain 27 characters and returns previous input
            lcd_result = lcd_str
        else:
            lcd_result = lcd_str + ')'

        self.display.setText(lcd_result)

    def equal_pressed(self):
        """Sends string expression to parser in matlib to evaluate input from display."""

        lcd_str = self.display.text()
        lcd_result = format(matlib.parse_expression(lcd_str), '.15g')
        self.display.setText(lcd_result)

    def lcd_string(self, string):
        if len(string) < 27:
            return True
        else:
            return False

    #  parser without operator priotiy and parenthesis
    """
                    if lcd_str[-1] in self.operators:
                raise ValueError("Expression ends with operator")

            print(lcd_str)
            number_arr = re.findall(r'[-]?\d*\.?\d+|[-+]?\d+', lcd_str)
            print(number_arr)
            result_num = re.findall(r'[-]?\d*\.?\d+|[-+]?\d+', lcd_str)[0]
            counter_neg = 0  # variable to check if first number is negative
            for c in range(len(lcd_str)):
                # cycle finds operator between first number and second number
                if float(result_num) < 0 and counter_neg == 0:
                    #  when first number is negative cycle ignor first operator to next in
                    c += 1
                    counter_neg += 1
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
            """
