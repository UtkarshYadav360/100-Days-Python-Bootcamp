from art import logo, vs
from game_data import data
import random
import os  # [USED IN CLEARING THE SCREEN]
import time  # [USED IN CLEARING THE SCREEN]

# PROJECT 14 :
# HIGHER LOWER GAME


def format_data(account):
    """Takes the account data and returns the printable foramt."""
    account_name = account["name"]
    account_description = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_description}, from {account_country}"


def check_answer(guess, a_followers, b_followers):
    """Takes the guess and followers count and returns if they got it right."""
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"


# game starts from here
game_started = True

# game score
score = 0

# printing the game logo
print(logo)

# generating random account 'B'
account_b = random.choice(data)

# make the game repeatable
while game_started:
    # generating a random account from the game data
    # making the account at position 'B' become the next account at position 'A'
    account_a = account_b
    account_b = random.choice(data)
    if account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A : {format_data(account_a)}")
    print(vs)
    print(f"Compare B : {format_data(account_b)}")

    # ask user to guess
    guess = input("Who has more followers? Type 'A' or 'B' : ").lower()

    # check if user is correct
    # --> get the follower count of each acoount <--
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]

    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    # give user feedback on their guess
    # --> score keeping <--
    if is_correct:
        score += 1
        print(f"You're right! Current score : {score}")
        # clear the screen between rounds
        time.sleep(1)
        os.system("cls")
    else:
        game_started = False
        print(f"Sorry, that's wrong! Final score : {score}")
