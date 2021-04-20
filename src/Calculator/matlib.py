##
# @file matlib.py
#
# @brief Library with mathematical functions

import math
import re
from collections import deque


##
# @brief Function that adds two parameters and returns them as a result
# @param a is integer or float
# @param b is integer or float
# @return result of add operation
def add(a, b):
    return a + b


##
# @brief Function that subtracts two parameters and returns them as a result
# @param a is integer or float
# @param b is integer or float
# @return result of subtract operation
def sub(a, b):
    return a - b


##
# @brief Function that multiplies two parameters and returns them as a result
# @param a is integer or float
# @param b is integer or float
# @return result of multiply operation
def mul(a, b):
    exp = a * b
    if exp == 0:
        exp = 0
    return exp


##
# @brief Function that divides two parameters and returns them as a result
# @param a is integer or float
# @param b is integer or float
# @return result of divide operation
def div(a, b):
    if b == 0:
        raise ValueError("ZeroDivisionError")
    exp = a / b
    if exp == 0:
        exp = 0
    return exp


##
# @brief Function that calculates factorial of integer
# @param a is integer
# @return result of factorial operation
def factorial(a):
    if a >= 990:
        raise ValueError("Value can't be greater than 899")
    if a > 0:
        val = a * factorial(a - 1)
    elif a == 0:
        return 1
    else:
        raise ValueError("Value can't be less than 0")
    return val


##
# @brief Function that calculates a power b
# @param a is integer or float
# @param b is integer or float max value is 99
# @return result of a power b
def pow(a, b):
    if b > 99:
        raise ValueError("Value can't be greater than 99")
    return a ** b


##
# @brief Function that calculates  root of a where base is b (default base is 2)
# @param a is integer or float
# @param b is integer or float
# @return result of n-root a
def nroot(a, b=2):
    if a < 0:
        raise ValueError("Value can't be less than 0")
    return a ** (1 / float(b))


##
# @brief Function that calculates logarithm of a where base is b (default base is 10)
# @param a is integer or float
# @param b is integer or float
# @return result base-b logarithm of a
def log(a, b=10):
    if a < 0:
        raise ValueError("Value can't be less than 0")
    return math.log(a, b)


##
# @brief Function that parses given expression in string, it determines operands and calls other matlib functions
# for calculation
# @param expression string containing expressions which needs to be calculated
# @return return result of expression
def parse_expression(expression):
    if not syntax(expression):
        raise ValueError("Syntax Error in Expression")

    expression = convert_unary_func(expression)
    exp_postfix = postfix(expression)
    temp_stack = []

    for c in exp_postfix:
        if c not in '+-*/^lr!':
            # add numbers to stack
            temp_stack.append(c)
        elif c in '+-*/^lr!':
            if len(temp_stack) == 1 or c in "l!":
                # calculate functions
                right = temp_stack.pop()
                if c == 'l':
                    result = convert_str(log(float(right)))
                    temp_stack.append(result)
                elif c == '!':
                    result = convert_str(factorial(float(right)))
                    temp_stack.append(result)
            elif len(temp_stack) >= 2:
                # calculate with binary operators
                right = temp_stack.pop()
                left = temp_stack.pop()
                if c == '+':
                    result = convert_str(add(float(left), float(right)))
                    temp_stack.append(result)
                elif c == '-':
                    result = convert_str(sub(float(left), float(right)))
                    temp_stack.append(result)
                elif c == '*':
                    result = convert_str(mul(float(left), float(right)))
                    temp_stack.append(result)
                elif c == '/':
                    result = convert_str(div(float(left), float(right)))
                    temp_stack.append(result)
                elif c == '^':
                    result = convert_str(pow(float(left), float(right)))
                    temp_stack.append(result)
                elif c == 'r':
                    result = convert_str(nroot(float(right), float(left)))
                    temp_stack.append(result)
            else:
                pass
    answer = temp_stack.pop()

    return float(answer)


##
# @brief Checks if value is operator
# @param c string containing operator
# @return boolean
def is_operator(c):
    operators = "+-*/^!"
    return c in operators


##
# @brief Function gives top value on stack
# @param a is stack on which we want top value
# @return top value of stack
def top(a):
    if not a:
        return None
    return a[len(a) - 1]


##
# @brief Function converts number to string
# @param number can be integer or float
# @return converted string

def convert_str(number):
    if type(number) != int and type(number) != float:
        raise TypeError
    return format(number, '.15g')


##
# @brief Function converts a mathematical expression into a suitable expression for further postfix translation
# @param expression to be converted
# @return converted expression

def convert_unary_func(expression):
    expression = expression.replace('log', 'l')
    expression = expression.replace('√', 'r')

    for i in range(len(expression)):
        # change unary negation operator '-' to '0-'
        if expression[i] == '(' and expression[i + 1] == '-':
            expression = expression[:i + 1] + '0' + expression[i + 1:]

        elif i == 0 and expression[i] == '-':
            expression = '0' + expression[i:]

        # default n=2 for root
        elif expression[i] == 'r':
            if expression[i] == 'r' and expression[i - 1] not in '0123456789' and i != 0:
                expression = expression[:i] + '2' + expression[i:]
            elif i == 0 and expression[i] == 'r':
                expression = '2' + expression[i:]
            else:
                pass

    return expression


##
# @brief Converts infix expression into postfix expression
# @param expression to be converted to postfix
# @return posfix expression

def postfix(expression):
    exp_list = re.findall(r'[0-9.]+|.', expression)
    numbers = re.findall(r'\d*\.?\d+|\d+', expression)
    op = {'(': 0, '+': 1, '-': 1, '*': 2, '/': 2, '^': 3, '!': 3, ')': 4, 'l': 0, 'r': 0}
    stack = deque()
    que = []

    for c in exp_list:
        if c in numbers:
            # if number - add to output
            que.append(c)
        elif is_operator(c):
            while True:
                top_char = top(stack)

                if top_char is None or top_char == '(':
                    stack.append(c)
                    break
                else:
                    if op[c] > op[top_char]:
                        # character has greater precedence than character on the top of stack
                        stack.append(c)
                        break
                    else:
                        # character has less precedence than character on the top of stack
                        que.append(stack.pop())

        elif c == '(' or c == 'l' or c == 'r':
            # character '(lr' has precedence 0
            stack.append(c)

        elif c == ')':
            pop_char = stack.pop()

            while pop_char != '(':
                # start pop from stuck until '('
                que.append(pop_char)
                pop_char = stack.pop()

            if top(stack) is not None and top(stack) in 'lr':
                # if functions "l" or "r" on top of stack
                que.append(stack.pop())
            else:
                pass

    while top(stack) is not None:
        # append everything left in stack to output
        que.append(stack.pop())

    return que


##
# @brief Check syntax of math expression
# @param expression to be checked for syntax errors
# @return bool

def syntax(expression):
    if expression[-1] in "+-*/^(√." or expression[0] in "*/^.)!":
        # last character in expression not number or not right parenthesis
        # or expression starts with not right character
        return False
    else:
        left = []
        right = []

        for n in range(len(expression)):
            if len(expression) == 1 and expression[n] in "+-*/!^)(√":
                # one character in expression is operator
                return False
            elif expression[n] in "√" and expression[n + 1] in "√+-*/!^.)":
                return False
            elif expression == "√(" or expression == "log(":
                return False
            elif (expression[n] in "+-*/^." and expression[n + 1] in "+*/!^.)") or (expression[n] in "^" and
                                                                                    expression[n + 1] in "-"):
                # operators in expression one by one
                return False
            elif expression[n] in "()":
                # for balanced parentheses
                if expression[n] == '(':
                    left.append(expression[n])
                else:
                    right.append(expression[n])
            else:
                pass

        # check balanced parentheses
        if len(left) != len(right):
            return False

        # check if number has right amount of period
        digit = re.findall(r'[0-9.]+', expression)
        for i in digit:
            if i.count('.') > 1:
                return False

        return True
