import math
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
    #Here will be function for parsing expressions
    None
