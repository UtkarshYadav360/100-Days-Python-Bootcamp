import os
import time
import random
from blackjack_logo import logo

# PROJECT 11 :
# BLACKJACK GAME (PART 3)


# RULES OF THE GAME :
# 1) the deck is unlimited in size
# 2) there are no jokers
# 3) the jack/queen/king all count as 10
# 4) the ace can count as 1 or 11
# # use the following list as the deck of cards
# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# 5) the cards in the list hace equal probability of being drawn
# 6) cards are not removed from the game as they are shown


# TODO 1 :
# create a function called compare() and pass in the "user_score" and "computer_score".If the computer and user both have the same score, then it's a draw.If the computer has a blackjack(0), then the user loses.If the user has a blackjack(0), then the user wins.If the user score is over than 21, then the user loses.If the computer score is over than 21, then the computer loses.If none of the above then then player with the highest score will win.

# TODO 2 :
# ask the user if they want to play again.If yes clear the console and restart the game.


# function to deal cards
def deal_cards():
    """Returns a random card from the deck of cards"""
    # deck of cards
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    random_card = random.choice(cards)
    return random_card


# function to return the score
def calculate_score(cards):
    """This function takes a list of cards as input,
    and returns 0 if there is a blackjack,
    and if score is more than 21 and have ace; change 11(ace) into 1,
    and returns the score."""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if (11 in cards) and (sum(cards) > 21):
        cards.remove(11)
        cards.append(1)
    return sum(cards)


# configuring TODO 1 :
def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw!"
    elif computer_score == 0:
        return "Lose!, opponent has a blackjack."
    elif user_score == 0:
        return "You Win!, with a blackjack."
    elif user_score > 21:
        return "You went over, You Lose!"
    elif computer_score > 21:
        return "Opponent went over, You Win!"
    elif user_score > computer_score:
        return "You Win!"
    else:
        return "You Lose!"


# this function makes the game run
def play_game():
    # logo
    print(logo)

    # computer cards and user cards are stored here
    user_cards = []
    computer_cards = []

    # game is not over yet'
    game_over = False

    # generating random cards and appending them to "user_cards" and "computer_cards"
    for _ in range(2):
        user_cards.append(deal_cards())
        computer_cards.append(deal_cards())

    # loop will the till the game is not over
    while not game_over:
        # if user or computer has blackjack or the use score is greater than 21 the game will end.
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your Cards : {user_cards}, current score = {user_score}")
        print(f"Computer's First Card : {computer_cards[0]}")
        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_over = True
        # wanna draw another card or not
        else:
            user_should_deal = input(
                "\nType 'y' to get another card, Type 'n' to pass : "
            )
            if user_should_deal == "y":
                user_cards.append(deal_cards())
            else:
                game_over = True

    # loop will run till the computer is less than 17 and not equal to 0;  (making computer play the game)
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_cards())
        computer_score = calculate_score(computer_cards)

    # printing the final statements
    print(f"\nYour final hand : {user_cards}, final score : {user_score}")
    print(f"Computer final hand {computer_cards}, final score : {computer_score}")
    print(compare(user_score, computer_score))


# calling the function to play the game
play_game()

# configuring TODO 2 :
while input("\nDo you wanna play again? Type 'y' or 'n' : ") == "y":
    print()
    time.sleep(1)
    os.system("cls")
    play_game()
else:
    print("Good Bye!")
