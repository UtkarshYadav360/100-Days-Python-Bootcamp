# HIGER ORDER FUNCTIONS :
# a function is said to be higher order function if it contains another function as a parameter or returns a function as output.
def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


# this is a higher order function
def calculate(a, b, fun):
    return fun(a, b)


calculate(5, 2, add)
