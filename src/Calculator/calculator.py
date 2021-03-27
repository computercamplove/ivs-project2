from PyQt5 import QtWidgets
from ui_calculator import Ui_Calculator
import re

class CalculatorWindow(QtWidgets.QMainWindow, Ui_Calculator):
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


    def number_pressed(self):
        btn = self.sender()
        label_num_str = self.display.text()
        result_label = ''

        if '.' not in label_num_str:
            result_label = format(float(self.display.text() + btn.text()), '.15g')
        else: #if 0 after "."
            result_label = self.display.text() + btn.text()

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
        self.display.setText('0')

    def delete_pressed(self):
        label_number_str = self.display.text()

        if len(label_number_str) == 1 or label_number_str == '0':
            self.clear_pressed()
        else:
            result_label = label_number_str[:-1]
            self.display.setText(result_label)

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




