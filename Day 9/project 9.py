import os
import time
from gavel_logo import logo

# PROJECT 9 :
# SECRET AUCTION PROGRAM :


# auction started
bidding_finished = False

# logo
print(logo)

# dictionary that stores the auction data
auction_data = {}


# function that checks the highest bid
def find_highest_bidder(bidding_data):
    highest_bid = 0
    for bidder in bidding_data:
        bid_amount = bidding_data[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid amount of ${highest_bid}.")


# loop will run till there are bidders
while not bidding_finished:
    # user name
    name = input("What is your name? ")

    # bid price
    bid_price = int(input("What's the bid amount? $"))
    auction_data[name] = bid_price

    # other user "yes" or "no"
    other_users = input("Is anyone there who also wants to bid? y/n : ")

    # if there are other users or not
    if other_users == "y":
        time.sleep(1)
        os.system("cls")
        auction_data[name] = bid_price
    elif other_users == "n":
        bidding_finished = True
        find_highest_bidder(bidding_data=auction_data)
    else:
        bidding_finished = True
        print("Invalid Input!, You are out of the bid.")
