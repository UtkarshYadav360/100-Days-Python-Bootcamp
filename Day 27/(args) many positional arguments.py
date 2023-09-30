# *args :
# * operator allows us to use infinite positional arguments in our function.
# args stand for the name of the argument. We can also change the argument name. ==> (*args) or (*numbers)
# arguments are stored as a tuple.


def add_many(*args):
    print(args)
    print(type(args))
    print(sum(args))


add_many(1, 2, 3, 4, 5)
