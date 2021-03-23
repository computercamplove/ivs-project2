import PyQt5.QtWidgets as qtw

class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Calculator IVS')

        # Layout
        self.setLayout(qtw.QVBoxLayout())
        self.keypad()


        self.show()

    def keypad(self):
        container = qtw.QWidget()
        container.setLayout(qtw.QGridLayout())

        dispay = qtw.QLineEdit()
        btn_clear = qtw.QPushButton("C")
        btn_delete = qtw.QPushButton("del")
        btn_log = qtw.QPushButton('log')
        btn_factoial = qtw.QPushButton("x!")
        btn_exp = qtw.QPushButton("e")
        btn_square = qtw.QPushButton("\u221Ax")

        btn_zero = qtw.QPushButton('0')
        btn_one = qtw.QPushButton('1')
        btn_two = qtw.QPushButton('2')
        btn_three = qtw.QPushButton('3')
        btn_four = qtw.QPushButton('4')
        btn_five = qtw.QPushButton('5')
        btn_six = qtw.QPushButton('6')
        btn_seven = qtw.QPushButton('7')
        btn_eight = qtw.QPushButton('8')
        btn_nine = qtw.QPushButton('9')
        btn_dot = qtw.QPushButton('.')

        btn_plus = qtw.QPushButton('+')
        btn_minus = qtw.QPushButton('-')
        btn_mult = qtw.QPushButton('*')
        btn_div = qtw.QPushButton('/')
        btn_result = qtw.QPushButton('=')

        #adding the buttons to layout
        container.layout().addWidget(dispay,0,0,1,5)
        container.layout().addWidget(btn_clear,1,0, 1,2)
        container.layout().addWidget(btn_delete,1,2,1,2)
        container.layout().addWidget(btn_log,2,0)
        container.layout().addWidget(btn_plus,1,4)
        container.layout().addWidget(btn_factoial,3,0)
        container.layout().addWidget(btn_exp,4,0)
        container.layout().addWidget(btn_square,5,0)
        container.layout().addWidget(btn_minus,2,4)
        container.layout().addWidget(btn_seven,2,1)
        container.layout().addWidget(btn_mult, 3,4)
        container.layout().addWidget(btn_eight,2,2)
        container.layout().addWidget(btn_nine,2,3)
        container.layout().addWidget(btn_four,3,1)
        container.layout().addWidget(btn_five,3,2)
        container.layout().addWidget(btn_six,3,3)
        container.layout().addWidget(btn_div, 4, 4)
        container.layout().addWidget(btn_one,4,1)
        container.layout().addWidget(btn_two,4,2)
        container.layout().addWidget(btn_three,4,3)
        container.layout().addWidget(btn_zero,5,1,1,2)
        container.layout().addWidget(btn_dot,5,3)
        container.layout().addWidget(btn_result,5,4)
        self.layout().addWidget(container)


calc = qtw.QApplication([])
mw = MainWindow()
calc.exec_() #run the application
