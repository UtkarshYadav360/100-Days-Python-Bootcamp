# PROJECT 8 :
# CAESAR CIPHER (PART 1 : ENCRYPTION)

# NOTE : index() method is used find the first index position of the specified letter.


# DON'T CHANGE THE CODE BELOW :
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

direction = input("Type, 'encode' to encrypt, Type 'decode' to decrypt : ")
text = input("Type your message : ").lower()
shift = int(input("Type the shift amount : "))


# TODO 1 :
# create a function called "encrypt" that takes "text" and "shift" as input.
def encrypt(plain_text, shift_amount):
    # TODO 2 :
    # inside the "encrypt" function, shift each letter of the "text" forwards in the alphabet by the shift amount and print the encrypted text.
    cipher_text = ""
    for letter in plain_text:
        position = alphabets.index(letter)
        new_position = position + shift_amount
        new_letter = alphabets[new_position]
        cipher_text += new_letter
    print(f"The encoded text is {cipher_text}")


# TODO 3 :
# call the "encrypt" function and pass in the user inputs.You should be able to test the code and encrypt a message.
encrypt(plain_text=text, shift_amount=shift)
