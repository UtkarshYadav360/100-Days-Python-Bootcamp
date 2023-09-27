# list comprehension :
# it is the shorter way to make a list using different sequences.

# SYNTAX = new_list = [new_item    for item in list]


# sequences in Python :
# list, range, string, tuple are the sequences in Python.


# without list comprehension
numbers = [1, 2, 3]
new_list = []
for n in numbers:
    add_1 = n + 1
    new_list.append(add_1)
print(new_list)


# with list comprehension
numbers = [1, 2, 3]
new_list = [n + 1 for n in numbers]
print(new_list)


# list comprehension with strings
name = "Angela"
name_alphabets = [letter for letter in name]
print(name_alphabets)


# list comprehension with range
double_nums = [num * 2 for num in range(1, 5)]
print(double_nums)


# conditional list comprehension
# SYNTAX = new_list = [new_item    for item in list    if    test]
names = ["Angela", "Alexa", "Yuri", "Maya", "Elanor", "Freddy"]
short_names = [name for name in names if len(name) < 5]
print(short_names)

long_names = [name.upper() for name in names if len(name) > 5]
print(long_names)
