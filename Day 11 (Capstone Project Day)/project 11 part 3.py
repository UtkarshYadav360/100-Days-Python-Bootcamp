import random

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


# game is not over yet'
game_over = False

# computer cards and user cards are stored here
user_cards = []
computer_cards = []

# generating random cards and appending them to "user_cards" and "computer_cards"
for _ in range(2):
    user_cards.append(deal_cards())
    computer_cards.append(deal_cards())

# loop will the till the game is not over
while not game_over:
    # TODO 1:
    # call the calculate_score() function.If the user or computer has a blackjack or the user score is greater than 21 then he game will end.
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f"Your Cards : {user_cards}, current score = {user_score}")
    print(f"Computer's First Card : {computer_cards[0]}")
    if user_score == 0 or computer_score == 0 or user_score > 21:
        game_over = True
        # TODO 2 :
        # if the game is not ended, ask the user if they want to draw another card.If yes use deal_card() function to add another card to the "user_cards" list.If no, then the game has ended.
    else:
        user_should_deal = input("Type 'y' to get another card, Type 'n' to pass : ")
        if user_should_deal == "y":
            user_cards.append(deal_cards())
        else:
            game_over = True

# TODO 2 :
# once the user is done, it's time to let the computer play.The computer should keep draawing cards as long as it has a score less than 17.
while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_cards())
    computer_score = calculate_score(computer_cards)
