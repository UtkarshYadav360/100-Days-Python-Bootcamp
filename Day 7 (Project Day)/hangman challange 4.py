import random

# PROJECT 7 :
# HANGMAN GAME (CHALLANGE 4) :

# stages of the game
stages = [
    """
  +---+
  |   |
      |
      |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
      |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
  |   |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========""",
    """
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========""",
]

# game is not over yet
game_over = False

# words to be used in the game
word_list = ["ant", "baboon", "bat"]

# chosen word from the word_list
chosen_word = random.choice(word_list)

# TODO 1 :
# create a variable called "lives" to keep track of the number of lives left.Set lives equal to 6.
lives = 6

# creating the blanks "_"
display = []
for _ in range(len(chosen_word)):
    display += "_"

# loop will run till the game is not over
while not game_over:
    # guessing the letter
    guess = input("Guess the letter : ").lower()

    # checking the guessd letter in the chosen_word
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    # TODO 2 :
    # if guess is not a letter in the chosen_word, then reduce "lives" by 1.If the "lives" goes down 0, the game will end.
    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            game_over = True
            print("You Lose!")

    print(f"{' '.join(display)}")

    # checking all the blanks "_" are filled with the correct letter
    if "_" not in display:
        game_over = True
        print("You Win!")

    # TODO 3 :
    # print the ascii art from "stages" that corresponds to the current number of "lives" the user has remaining.
    print(stages[lives])
