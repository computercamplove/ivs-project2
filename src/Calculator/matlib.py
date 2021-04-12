import math
import re


def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    exp = a * b
    if exp == 0:
        exp = 0
    return exp


def div(a, b):
    if b == 0:
        raise ValueError("Hodnotou 0 nelze delit")
    exp = a / b
    if exp == 0:
        exp = 0
    return exp


def factorial(a):
    if a >= 990:
        raise ValueError("Hodnota nemuze byt vetsi nez 899")
    if a > 0:
        val = a * factorial(a-1)
    elif a == 0:
        return 1
    else:
        raise ValueError("Hodnota nemuze byt mene nez 0")
    return val


def pow(a, b):
    return a ** b


def nroot(a, b=2):
    if a < 0:
        raise ValueError("Hodnota nemuze byt mene nez 0")
    return a ** (1/float(b))


def log(a, b=10):
    if a < 0:
        raise ValueError("Hodnota nemuze byt mene nez 0")
    return math.log(a, b)


def parse_expression(expression):
    """Evaluate math expression."""

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
            if len(temp_stack) == 1 or c in "l!r":
                # calculate functions
                right = temp_stack.pop()
                if c == 'l':
                    result = convert_str(log(float(right)))
                    temp_stack.append(result)
                elif c == '!':
                    result = convert_str(factorial(float(right)))
                    temp_stack.append(result)
                elif c == 'r':
                    result = convert_str(nroot(float(right)))
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
            else:
                pass

    answer = temp_stack.pop()

    return float(answer)


def is_operator(c):
    """Check if character is operator."""
    operators = "+-*/^!"
    return c in operators


def top(a):
    """Get character on the top of stack."""
    if not a:
        return None
    return a[len(a) - 1]


def convert_str(number):
    """Converts float into string."""
    return format(number, '.15g')


def convert_unary_func(expression):
    """
    Function converts a mathematical expression into a suitable
    expression for further postfix translation.
    """

    # replace 'log' to 'l'
    expression = expression.replace('log', 'l')

    # replace '√' to '√()'
    root = re.findall(r'(?<=\u221a)\-*[0-9.]+', expression)
    for i in root:
        expression = expression.replace('√' + i, 'r(' + i + ')')

    # change unary negation operator '-' to '0-'
    for i in range(len(expression)):
        if expression[i] == '(' and expression[i + 1] == '-':
            expression = expression[:i + 1] + '0' + expression[i + 1:]

        elif i == 0 and expression[i] == '-':
            expression = '0' + expression[i:]

    return expression


def postfix(expression):
    """Converts infix expression into postfix expression."""

    exp_list = re.findall(r'[0-9.]+|.', expression)
    numbers = re.findall(r'\d*\.?\d+|\d+', expression)
    op = {'(': 0, '+': 1, '-': 1, '*': 2, '/': 2, '^': 3, '!': 3, ')': 4, 'l': 0, 'r': 0}
    stack = []
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


def syntax(expression):
    """Check syntax of mathe expression."""

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
            elif expression[n] in "+-*/^√." and expression[n + 1] in "+*/!^.":
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
