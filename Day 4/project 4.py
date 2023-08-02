import random

# PROJECT 4 :
# ROCK, PAPER, SCISSORS GAME :


# game images
rock = """  
    _______
---'   ____)  
      (_____)  
      (_____)  
      (____)
---.__(___)  
"""

paper = """  
    _______
---'   ____)____  
          ______)  
          _______)  
         _______)
---.__________)  
"""

scissors = """  
    _______
---'   ____)____  
          ______)  
       __________)  
      (____)
---.__(___)  
"""

# greeting to the user
print("Welcome To The Rock, Paper, Scissors Game!")

# instructions to the user
print("Type 'r' for Rock, 'p' for Paper and 's' for Scissors.")

# computer choice
computer_random_choice = random.randint(0, 2)
if computer_random_choice == 0:
    computer_choice = rock
elif computer_random_choice == 1:
    computer_choice = paper
else:
    computer_choice = scissors

# user choice
user_input = input("Make a choice : ")
if user_input == "r":
    user_choice = rock
elif user_input == "p":
    user_choice = paper
elif user_input == "s":
    user_choice = scissors

# winning conditions
if computer_choice == user_choice:
    print(f"\nYou Choose :\n{user_choice}\nComputer Choose :\n{computer_choice}")
    print("It's A Tie!")
elif computer_choice == rock and user_choice == paper:
    print(f"\nYou Choose :\n{user_choice}\nComputer Choose :\n{computer_choice}")
    print("You Win!")
elif computer_choice == paper and user_choice == scissors:
    print(f"\nYou Choose :\n{user_choice}\nComputer Choose :\n{computer_choice}")
    print("You Win!")
elif computer_choice == scissors and user_choice == rock:
    print(f"\nYou Choose :\n{user_choice}\nComputer Choose :\n{computer_choice}")
    print("You Win!")
else:
    print(f"\nYou Choose :\n{user_choice}\nComputer Choose :\n{computer_choice}")
    print("You Lose!")
