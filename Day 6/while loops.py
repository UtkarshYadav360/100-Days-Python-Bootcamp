# WINNING THE REEBORGS WORLD HURDLE 1 USING WHILE LOOP :


# function to turn around :
def turn_around():
    turn_left()
    turn_left()


# function to turn right :
def turn_right():
    turn_left()
    turn_left()
    turn_left()


# function to win hurdle 1 :
def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()


# calling the function to win hurdle 1 :
hurdles = 6
while hurdles > 0:
    jump()
    hurdles -= 1
