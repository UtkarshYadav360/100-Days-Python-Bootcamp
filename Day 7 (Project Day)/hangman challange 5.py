import os  # USED IN CLEARING THE SCREEN
import time  # USED IN CLEARING THE SCREEN
import random
from hangman_art import stages, logo  # TODO 1 (COMPLETED)
from hangman_word_list import word_list  # TODO 2 (COMPLETED)

# PROJECT 7 :
# HANGMAN GAME (CHALLANGE 5) :

# TODO 1 :
# add more words to the "word_list"

# TODO 2 :
# print the hangman game logo

# TODO 3 :
# if the user has enterd a letter they,ve already guessed, print the letter and let them know.

# TODO 4 :
# if the letter is not in the "chosen_word" let them know it is not in the word.


# game is not over yet
game_over = False

# chosen word from the word_list
chosen_word = random.choice(word_list)

# total lives
lives = 6

# printing the game logo
print(logo)

print(chosen_word)

# creating the blanks "_"
display = []
for _ in range(len(chosen_word)):
    display += "_"

# loop will run till the game is not over
while not game_over:
    # guessing the letter
    guess = input("Guess the letter : ").lower()

    # CLEARING THE SCREEN AFTER EVERY INPUT
    time.sleep(2)
    os.system("cls")

    # TODO 3 (COMPLETED)
    if guess in display:
        print(f"You've already guessed {guess}")

    # checking the guessd letter in the chosen_word
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    # game will over when the lives becomes 0
    if guess not in chosen_word:
        print(f"You've guessed {guess}, that's not in the word.")  # TODO 4 (COMPLETED)
        lives -= 1
        if lives == 0:
            game_over = True
            print(f"\nThe word is {chosen_word}")
            print("You Lose!")

    # joining all the list elements and turning them into a string
    print(f"{' '.join(display)}")

    # checking all the blanks "_" are filled with the correct letter
    if "_" not in display:
        game_over = True
        print("You Win!")

    # printing the state of hangman stages that corresponds to the current number of lives that user have
    print(stages[lives])
