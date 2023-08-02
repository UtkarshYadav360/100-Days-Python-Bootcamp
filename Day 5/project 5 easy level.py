import random

# PROJECT 5 :
# PYTHON PASSWORD GENERATOR (EASY LEVEL):


# letters available
letters_available = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
]

# numbers available
numbers_available = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

# symbols available
symbols_available = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

# greeting to the user
print("Welcome To The Python Password Generator!\n EASY LEVEL PROGRAM.")

# letters input
letters_count = int(input("How many letter you want in your password? "))

# numbers input
numbers_count = int(input("How many numbers you want in your password? "))

# symbols input
symbols_count = int(input("How many symbols you want in your password? "))

# password
password = ""

# generating random letters
for _ in range(letters_count):
    password += random.choice(letters_available)

# generating random numbers
for _ in range(numbers_count):
    password += random.choice(numbers_available)

# generating random symbols
for _ in range(symbols_count):
    password += random.choice(symbols_available)

# final output
print(f"You can use {password} as your password.")
