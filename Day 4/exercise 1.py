# EXERCISE 1 :
# toss the coin and print Heads or Tails.

import random

toss = random.randint(0, 1)
if toss == 0:
    print("Heads")
else:
    print("Tails")
