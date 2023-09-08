# PROJECT 15 (USING OOP):
# RE-CONSTRUCTING THE COFFEE MACHINE


# importing the program requirements
from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# machine is on
machine_is_on = True

# making "Objects"
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()

# loop runs till the coffee machine is on
while machine_is_on:
    # asking for the user input
    choice = input(f"What would you like? {menu.get_items()}: ")
    # checking the user input
    if choice == "off":
        machine_is_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(
            drink.cost
        ):
            coffee_maker.make_coffee(drink)
            print()
