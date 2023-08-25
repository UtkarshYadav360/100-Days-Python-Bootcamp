from menu import MENU, resources

# PROJECT 15 :
# COFFEE MACHINE


def is_resource_suffecient(order_ingredients):
    """Takes the ingredients needed to make the coffee and return True if they are suffecient else return False."""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
        return True


def process_coins():
    """Returns the total calculated, from the coins inserted."""
    print("Please insert coins.")
    total = int(input("How many quarters? :")) * 0.25
    total += int(input("How many dime? :")) * 0.1
    total += int(input("How many nickles? :")) * 0.05
    total += int(input("How many pennys? :")) * 0.01
    return total


def is_transaction_successful(money_recieved, drink_cost):
    """Return True if the payment is successful and False if the money is insuffecient."""
    if money_recieved >= drink_cost:
        change = round((money_recieved - drink_cost), 2)
        print(f"Here's ${change} in change.")
        global money
        money += drink_cost
        return True
    else:
        print("Sorry there's not enough money. Money refunded.")
        return False


def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}☕ coffee.")


# machine is on
machine_is_on = True

# there is no money in the machine
money = 0

# loop tuns till the coffee machine is on
while machine_is_on:
    # asking for user input
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    # checking the user input
    if choice == "off":
        machine_is_on = False
    elif choice == "report":
        print(
            f"Water: {resources['water']}ml \nMilk: {resources['milk']}ml \nCoffee: {resources['coffee']}g\nMoney: ${money}"
        )
    else:
        drink = MENU[choice]
        if is_resource_suffecient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])
                print()
