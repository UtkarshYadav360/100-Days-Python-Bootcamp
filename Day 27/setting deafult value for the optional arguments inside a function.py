# default arguments
# we can specify the argument value, even if it is set by default.
# if the argument value is not specified, then the default value will be used.


# function to add two numbers but it has default arguments passed in it.
def add_two(n1=5, n2=5):
    """Add two number and has default arguments."""
    return n1 + n2


num_sum = add_two()
print(num_sum)

num_sum = add_two(15)
print(num_sum)

num_sum = add_two(20, 20)
print(num_sum)
