# making function that takes input using "positional arguments":
def greet(name):
    print(f"Hello {name}")
    print("What's going on?")


greet("Utkarsh")


# making a function that takes two inputs using "keyword arguments":
def greet_again(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}")


greet_again(name="Utkarsh", location="Ghaziabad")
