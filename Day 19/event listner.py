from turtle import Turtle, Screen


# function to be performed
def move_forward():
    timmy.forward(10)


timmy = Turtle()
screen = Screen()
screen.listen()  # sets the focus on the turtle screen in order to collect key events
screen.onkey(
    key="space", fun=move_forward
)  # when space key is pressed the turtle moves forward
screen.exitonclick()
