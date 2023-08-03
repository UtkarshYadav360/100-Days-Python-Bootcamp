import random

# PROJECT 11 :
# BLACKJACK GAME (PART 1)


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
# create a deal_card() function that uses the list below to return a random card
def deal_cards():
    """Returns a random card from the deck of cards"""
    # deck of cards
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    random_card = random.choice(cards)
    return random_card


# TODO 2 :
# deal the user and computer 2 cards each using deal_cards()
user_cards = []
computer_cards = []

for _ in range(2):
    user_cards.append(deal_cards())
    computer_cards.append(deal_cards())

print(user_cards)
print(computer_cards)
