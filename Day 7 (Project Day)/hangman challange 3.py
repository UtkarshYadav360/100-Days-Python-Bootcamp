import random

# PROJECT 7 :
# HANGMAN GAME (CHALLANGE 3) :

# game is not over yet
game_over = False

# words to be used in the game
word_list = ["ardvark", "baboon", "camel"]

# chosen word from the word_list
chosen_word = random.choice(word_list)

# creating the blanks "_"
display = []
for _ in range(len(chosen_word)):
    display.append("_")

# TODO 1 :
# use a while loop to let the user guess again.The loop should only stop once the user has guessed all the letters in the chosen_word and "display" has no more blanks "_" . Then you can tell the user they've won.

while not game_over:
    # guessing the letter
    guess = input("Guess the letter : ").lower()

    # checking the guessd letter in the chosen_word
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    # TODO 2 :
    # join all the elements in the list and display it as a string.
    print(f"{' '.join(display)}")

    if "_" not in display:
        game_over = True
        print("You Win!")
