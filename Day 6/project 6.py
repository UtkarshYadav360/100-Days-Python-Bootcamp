# PROJECT 6 :
# REEBORGS WORLD HURDLE 4 :


# function to turn around :
def turn_around():
    turn_left()
    turn_left()


# function to turn right :
def turn_right():
    turn_left()
    turn_left()
    turn_left()


# function to win hurdle 4 :
def jump():
    turn_left()
    while wall_on_right():
        move()
    turn_right()
    move()
    turn_right()
    while front_is_clear():
        move()
    turn_left()


# calling the function to win hurdle 4 :
while not at_goal():
    if wall_in_front():
        jump()
    else:
        move()
