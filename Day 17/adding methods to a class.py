# making a class:


class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0
        pass

    # adding method to the class:
    def follow(self, user):
        user.followers += 1
        self.following += 1


user_1 = User("001", "Angela")
user_2 = User("002", "Jack")
user_1.follow(user_2)

print(f"User Id : {user_1.id}")
print(f"User Name : {user_1.username}")
print(f"Followers : {user_1.followers}")
print(f"Following : {user_1.following}")

print()

print(f"User Id : {user_2.id}")
print(f"User Name : {user_2.username}")
print(f"Followers : {user_2.followers}")
print(f"Following : {user_2.following}")
