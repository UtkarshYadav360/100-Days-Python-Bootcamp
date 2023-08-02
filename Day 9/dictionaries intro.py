# making a dictionary :
programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
}
print(programming_dictionary)


# accessing the dictionary values
print(programming_dictionary["Bug"])
print(programming_dictionary["Function"])


# adding new items to the dictionary :
programming_dictionary["Loop"] = "The action of something over and over again."
print(programming_dictionary)


# making an empty dictionary :
empty_dictionary = {}
print(empty_dictionary)
# using this method we can also wipe the existing dictionary


# edit an item in the dictrionary :
programming_dictionary["Bug"] = "A moth in your computer."
print(programming_dictionary["Bug"])


# looping through the dictionary :
for item in programming_dictionary:
    print(item)
    print(programming_dictionary[item])
