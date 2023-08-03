import random

# PROJECT 11 :
# BLACKJACK GAME (PART 2)


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


# computer cards and user cards are stored here
user_cards = []
computer_cards = []

# generating random cards and appending them to "user_cards" and "computer_cards"
for _ in range(2):
    user_cards.append(deal_cards())
    computer_cards.append(deal_cards())


# TODO 1 :
# create a function called calculate_score() that takes a list of cards as input and returns the score.
# sum() function can be used to calculate the sum.
def calculate_score(cards):
    # TODO 2 :
    # inside the calculate_score() function check for a blackjack(a hand with only 2 cards : ace + 10) and return 0 instead of the actual score.0 will represent a blackjack in our game.
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    # TODO 3 :
    # inside calculate_score() function check for an 11(ace).If the score is already over 21, remove the 11 and replace it with a 1.You might need to look upon the append() and remove() functions
    if (11 in cards) and (sum(cards) > 21):
        cards.remove(11)
        cards.append(1)

    return sum(cards)
