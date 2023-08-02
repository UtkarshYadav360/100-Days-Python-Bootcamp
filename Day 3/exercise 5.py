# EXERCISE 5 :
# make a love calculator

# NOTE : lower() function turns all letters to the lowercase.
# NOTE : count() method counts the number of times a letter occurs in the string.

# DON'T CHANGE THE CODE BELOW :
print("Welcome To The Love Calculator!")
name1 = input("What is your name?\n")
name2 = input("What is their name?\n")


# WRITE YOUR CODE HERE :
combined_names = name1 + name2
lowered_names = combined_names.lower()

t = lowered_names.count("t")
r = lowered_names.count("r")
u = lowered_names.count("u")
e = lowered_names.count("e")

l = lowered_names.count("l")
o = lowered_names.count("o")
v = lowered_names.count("v")
e = lowered_names.count("e")

true = t + r + u + e
love = l + o + v + e
love_score = str(true) + str(love)

int_love_score = int(love_score)

if int_love_score < 10 or int_love_score > 90:
    print(
        f"Your love score is {int_love_score} and you go together like coke and mentos."
    )
elif int_love_score >= 40 and int_love_score <= 50:
    print(f"Your love score is {int_love_score} and you are alright together.")
else:
    print(f"Your love score is {int_love_score}")
