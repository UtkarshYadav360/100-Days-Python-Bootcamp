import random

# EXERCISE 2 :
# take names of the people who have eaten the food and randomly guess a person who will pay the bill.

# NOTE : split() method splits the string with the specified character and returns a list.

# DON'T CHANGE THE CODE ABOVE :
names_string = input("Give me everybody's names, seperated by comma : ")
names = names_string.split(",")

# WRITE YOUR CODE HERE :
total_names = len(names)

random_choice = random.randint(0, total_names - 1)

random_name = names[random_choice]

print(f"{random_name} is going to buy the meal today.")
