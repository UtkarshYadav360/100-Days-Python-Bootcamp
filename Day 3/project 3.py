# PROJECT 3 :
# TREASURE ISLAND :


# treasure ascii art
logo = '''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
'''

# printing the logo
print(logo)

# greeting to the user
print("Welcome To The Treasure Island!")

# choosing the direction
direction = input(
    "There are two paths to go, Type 'l' to go Left or 'r' to go Right : "
).lower()
if direction == "l":
    print("You choosed the correct path!")

    # making a choice to swim or wait for the boat
    choice = input(
        "Do you want to swim in the river or wanna wait for the boat? 's' / 'w' : "
    ).lower()
    if choice == "w":
        print("You made a great choice!")

        # choosing the door
        door = input(
            "Choose a door, Type 'r' for Red, 'y' for Yellow and 'b' for Blue : "
        ).lower()
        if door == "y":
            print("YAYY! You found the treasure.")
        elif door == "r":
            print("You fell into the lava lake.")
        elif door == "b":
            print("You sink into the water whirpool.")
        else:
            print("Game Over!")
    elif choice == "s":
        print("You've been eaten by the hungry crocodiles.")
    else:
        print("Game Over!")
else:
    print("Game Over")
