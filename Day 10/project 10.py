import os
import time
from calculator_logo import logo

# PROJECT 10 :
# CLACULATOR

# NOTE :
# a function calling itself is called a recursive function and this process is called recurssion.


# add function
def add(n1, n2):
    return n1 + n2


# subtract function
def subtract(n1, n2):
    return n1 - n2


# multiply function
def multiply(n1, n2):
    return n1 * n2


# divide function
def divide(n1, n2):
    return n1 / n2


# exponentiation function
def exponentiation(n1, n2):
    return n1**n2


# modulus function
def modulus(n1, n2):
    return n1 % n2


# dictionary that stores all the operation functions
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
    "**": exponentiation,
    "%": modulus,
}


# function that makes the calculator work
def calculator():
    # logo
    print(logo)

    # first number input
    num1 = float(input("First Number : "))

    # printing the operations
    print("Operations : ")
    for keys in operations:
        print(keys)
    # calculator is not stopped yet
    should_continue = True

    # loop runs till the calculator is not stopped
    while should_continue:
        # operation choice
        choice = input("Choose an operation : ")
        # second number input
        num2 = float(input("Second Number : "))
        # performing the operation
        calculation = operations[choice]
        answer = calculation(num1, num2)

        # output
        print(f"{num1} {choice} {num2} = {answer}")

        # wanna continue the calculation or not
        run_again = input(
            f"\nType 'y' to continue the calculating with {answer}, Type 'e' to exit, Type 'n' to start a new calculation : "
        )
        print()
        if run_again == "y":
            num1 = answer
        elif run_again == "n":
            should_continue = False
            time.sleep(1)
            os.system("cls")
            calculator()  # recurssion is used here
        else:
            should_continue = False
            print("Good Bye!")


calculator()
