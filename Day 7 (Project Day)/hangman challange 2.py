import random

# PROJECT 7 :
# HANGMAN GAME (CHALLANGE 2) :


# words to be used in the game
word_list = ["ardvark", "baboon", "camel"]

# chosen word from the word_list
chosen_word = random.choice(word_list)

# TODO 1 :
# create an empty list called display.For each letter in the chosen_word, add a "_" to "display"
display = []
for _ in range(len(chosen_word)):
    display.append("_")
print(display)

# guessing the letter
guess = input("Guess the letter : ").lower()

# TODO 2 and TODO 3 :
# loop through each position in the chosen_word.If the letter at that position matches "guess" then reveal that letter in the display at that position.
# print display and you should see the guessed letter in the correct position and every other letter replace with "_"
for position in range(len(chosen_word)):
    letter = chosen_word[position]
    if letter == guess:
        display[position] = letter
print(display)
