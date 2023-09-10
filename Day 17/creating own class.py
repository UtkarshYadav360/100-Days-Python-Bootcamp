# creating own class:

# pass statement is used to pass the statement and move to the next line.
# a class is defined using the "class" keyword.
# a class name must be in PascalCase.
# "__init__" is used to initialize the attributes.
# "self" is the actual object that is being initialized.
# we can pass many more arguments while making our class, which becomes the data for the attributes we want to create inside the class.


class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0  # making a new attribute with a default value.
        pass


user_1 = User("001", "Angela")
print(user_1.id, user_1.username, user_1.followers)
