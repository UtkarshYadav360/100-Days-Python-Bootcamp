# function to turn around :
def turn_around():
    turn_left()
    turn_left()


# function to turn right :
def turn_right():
    turn_left()
    turn_left()
    turn_left()


# function to win hurdle 3 :
def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()


# calling the function to win hurdle 3 :
while not at_goal():
    if front_is_clear():
        move()
    else:
        jump()
