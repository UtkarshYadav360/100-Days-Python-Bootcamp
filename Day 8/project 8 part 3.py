# PROJECT 8 :
# CAESAR CIPHER (PART 3 : REORGANISING THE CODE)


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


# TODO 1 :
# combine "encrypt" and "decrypt" functions into a single function called caesar()
def caesar(start_text, shift_amount, cipher_direction):
    final_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for letter in start_text:
        position = alphabets.index(letter)
        new_position = position + shift_amount
        final_text += alphabets[new_position]
    print(f"The {cipher_direction}d text is {final_text}")


# TODO 2 :
# call the caesar() function, passing over the 'text, 'shift' and 'direction' values.
caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
