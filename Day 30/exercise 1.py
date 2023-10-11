# EXERCISE 1 :
# INDEX ERROR HANDLING


# DON'T CHANGE THE CODE BELOW :
fruits = eval(input())


# MODIFY THIS FUNCTION :
# TODO : CATCH THE EXCEPTION AND MAKE SURE THE CODE RUNS WITHOUT ANY ERROR
def make_pie(index):
    try:
        fruit = fruits[index]
    except IndexError:
        print("Fruit Pie")
    else:
        print(fruit + "pie")


# DON'T CHANGE THE CODE BELOW :
make_pie(4)  # raise IndexError on list with less than 5 items.
