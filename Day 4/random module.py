# importing random module
import random

# generating a random integer between 1 to 10
random_integer = random.randint(1, 10)
print(random_integer)

# generating a random floating point number between 0.0 to 0.9
random_float = random.random()
print(random_float)

# generating a random floating point number between 0.0 to 5.0
new_random_float = random.random() * 5
print(new_random_float)
