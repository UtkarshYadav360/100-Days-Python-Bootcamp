import random

# PROJECT 7 :
# HANGMAN GAME (CHALLANGE 1) :


# words to be used in the game
word_list = ["ardvark", "baboon", "camel"]

# TODO 1 :
# randomly choose a random word from the word_list and assign it to a variable called chosen_word
chosen_word = random.choice(word_list)

# TODO 2 :
# ask the user to guess a letter and assign their answer to a variable called guess.Make guess lowercase.
guess = input("Guess the letter : ").lower()

# TODO 3 :
# check if the letter user guessed is one of the letters in the chosen_word
for letter in chosen_word:
    if letter == guess:
        print("Right")
    else:
        print("Wrong")
