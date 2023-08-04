from game_logo import logo
import random

# PROJECT 12 :
# NUMBER GUESSING GAME

EASY_LEVEL_CHANCES = 10
HARD_LEVEL_CHANCES = 5


# function to get user guess against actual answer'
def check_answer(guess, answer, attempts):
    """Check answer against the guessed number
    and returns the attempts left to guess the number."""
    if guess > answer:
        print("Too High!")
        return attempts - 1
    elif guess < answer:
        print("Too Low!")
        return attempts - 1
    else:
        print(f"You got it, the answer is {answer}.")


# function to set difficulty
def set_difficulty():
    """Set the game difficulty and,
    return total attempts to guess the number."""
    level = input("Choose a difficulty, 'easy' / 'hard' : ")
    if level == "easy":
        return EASY_LEVEL_CHANCES
    else:
        return HARD_LEVEL_CHANCES


# function to run the game
def game():
    """This function performs the task to run the game"""
    # logo
    print(logo)
    # greeting to the user
    print("Welcome To The Number Guessing Game!")
    print("I am thinking of a number between 1 to 100.")

    # choosing a random number between 1 to 100
    answer = random.randint(1, 100)

    # game mode chances
    attempts = set_difficulty()

    guess = 0
    # loop runs till the answer is not correct
    while guess != answer:
        print(f"You have {attempts} attempts remaining to guess the number.")

        # guessing the number]
        guess = int(input("Guess the number : "))

        # what if the attemps are 0
        attempts = check_answer(guess, answer, attempts)
        if attempts == 0:
            print(f"You are out of attempts, You Lose!")
            return
        elif guess != answer:
            print("Guess Again!")


# calling the function that runs the game
game()
