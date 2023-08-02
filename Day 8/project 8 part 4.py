from caesar_cipher_logo import logo  # TODO 1 (COMPLETED)

# PROJECT 8 :
# CAESAR CIPHER (PART 4 : REORGANISING THE CODE)


# TODO 1 :
# print the logo of the caesar cipher

# TODO 2 :
# what if the user enters a shift number greater than the letters in the message.

# TODO 3 :
# what happens if the user enters a number or a symbol or a space?
# fix the code to keep numbers, symbols and spaces.

# TODO 4 :
# ask if the user to restart the caesar cipher program. If "yes" run the function again.

# printing the logo
print(logo)

# alphabets to be used
alphabets = [
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
]


# function the performs "encoding" and "decoding"
def caesar(start_text, shift_amount, cipher_direction):
    final_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for char in start_text:
        # configuring TODO 3 :
        if char in alphabets:
            position = alphabets.index(char)
            new_position = position + shift_amount
            final_text += alphabets[new_position]
        else:
            final_text += char
    print(f"The {cipher_direction}d text is {final_text}")


# configuring TODO 4 :
should_continue = True
while should_continue:
    # "encode" or "decode"
    direction = input("Type, 'encode' to encrypt, Type 'decode' to decrypt : ")

    # message
    text = input("Type your message : ").lower()

    # shift amount
    shift = int(input("Type the shift amount : "))

    # configuring TODO 2 :
    shift %= 26

    # calling the function
    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

    result = input("\nType, 'y' to restart, Type 'n' to stop : ")
    print()
    if result == "n":
        should_continue = False
        print("Good Bye!")
