# PROJECT 8 :
# CAESAR CIPHER (PART 2 : DECRYPTION)


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

# "encode" or "decode"
direction = input("Type, 'encode' to encrypt, Type 'decode' to decrypt : ")

# message
text = input("Type your message : ").lower()

# shift amount
shift = int(input("Type the shift amount : "))


# function that encodes the message
def encrypt(plain_text, shift_amount):
    cipher_text = ""
    for letter in plain_text:
        position = alphabets.index(letter)
        new_position = position + shift_amount
        new_letter = alphabets[new_position]
        cipher_text += new_letter
    print(f"The 'encoded' text is {cipher_text}")


# TODO 1 :
# create a function called "decrypt" that takes the text and shift amount as input
def decrypt(cipher_text, shift_amount):
    # TODO 2 :
    # insdie the "decrypt" function, shift each letter of the "text" backwards in the alphabets by the shift amount and print the decrypted text.
    plain_text = ""
    for letter in cipher_text:
        position = alphabets.index(letter)
        new_position = position - shift_amount
        plain_text += alphabets[new_position]
    print(f"The 'decoded' text is {plain_text}")


# TODO 3 :
# check if the user want to encrypt or decrypt the message by checking the "direction" variable.Then call the correct function based on that "direction" variable.You should be able to test the code and encrypt and decrypt a message.
if direction == "encode":
    encrypt(plain_text=text, shift_amount=shift)
elif direction == "decode":
    decrypt(cipher_text=text, shift_amount=shift)
