import turtle as t

# EXERCISE 1 :
# MAKE AN ETCH-A-SKETCH

# w ==> forward
# s ==> backward
# a ==> counter-clockwise
# d ==> clockwise
# c ==> clear drawing


# functions to be move performed
def move_forward():
    """moves the turtle in forward direction"""
    timmy.forward(10)


def move_backward():
    """moves the turtle in forward direction"""
    timmy.backward(10)


def turn_left():
    """moves the turtle left"""
    timmy.left(10)


def turn_right():
    """move the turtle right"""
    timmy.right(10)


def clear_screen():
    """clear the screen"""
    timmy.clear()  # clear the screen
    timmy.penup()
    timmy.home()  # move turtle to it's  original position
    timmy.pendown()


# making an object from the "Turtle" class
timmy = t.Turtle()


# making an object from the "Screen" class
screen = t.Screen()
screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="c", fun=clear_screen)
screen.exitonclick()
