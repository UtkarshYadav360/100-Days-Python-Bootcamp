# EXERCISE 4 :
# take pizza order from the user and print the total bill.

# DON'T CHANGE THE CODE BELOW :
print("Welcome To The Python Pizza Deliveries!")

size = input("What size pizza do you want? S, M or L : ")
add_pepperoni = input("Do you want pepperoni? Y/N : ")
extra_cheese = input("Do you want extra cheese? Y/N : ")


# WRITE YOUR CODE HERE :
pizza_cost = 0

if size == "S":
    pizza_cost += 15
elif size == "M":
    pizza_cost += 20
elif size == "L":
    pizza_cost += 25

if add_pepperoni == "Y":
    if size == "S":
        pizza_cost += 2
    else:
        pizza_cost += 3

if extra_cheese == "Y":
    pizza_cost += 1

print(f"Your total bill is ${pizza_cost}")
