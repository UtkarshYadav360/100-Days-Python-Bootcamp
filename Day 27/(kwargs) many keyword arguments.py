# **kwargs :
# ** operator allows us to use unlimited keyword arguments in a function.
# kwargs stands for the name of the argument. We can also change the argument name. ==> (**kwargs) or (**numbers)
# arguments are stored as a dictionary.


def calculate(n1, **kwargs):
    print(kwargs)
    print(type(kwargs))
    print(kwargs["add"])
    print(kwargs["multiply"])
    n1 += kwargs["add"]
    n1 *= kwargs["multiply"]
    print(n1)


calculate(2, add=3, multiply=5)


# using **kwargs in classes
class Car:
    def __init__(self, **kw):
        self.make = kw["make"]
        # .get() method just return the key and don't give any error if it's value is not found.
        self.model = kw.get("model")


my_car = Car(make="Nissan", model="GT-R")
print(my_car.make)
print(my_car.model)

new_car = Car(make="Tesla")
print(new_car.make)
print(new_car.model)  # None
