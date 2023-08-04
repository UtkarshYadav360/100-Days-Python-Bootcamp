# global variable :
enemies = 2


def increase_enemies():
    enemies = 3  # local variable
    print(f"Enemies inside the function {enemies}.")


increase_enemies()
print(f"Enemies outside the function {enemies}.")


# modifying global variables :
mobs = ["skeleton", "zombie", "creeper"]


def tell_mobs():
    global mobs
    mobs = ["skeleton", "zombie", "spider"]
    print(f"Mobs inside the function {mobs}")


tell_mobs()
print(f"Mobs outside the function {mobs}")
