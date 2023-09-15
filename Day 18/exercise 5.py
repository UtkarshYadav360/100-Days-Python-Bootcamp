from turtle import Turtle, Screen
import random

# EXERCSIE 5 :
# draw a spirograph


# random RGB colors for the turtle
def random_color():
    """Generating random color for the turtle."""
    R = random.random()
    G = random.random()
    B = random.random()
    timmy.color(R, G, B)


# making an object from the "Turtle" class
timmy = Turtle()
timmy.speed("fastest")


# drawing the spirograph
def draw_spirograph(gap_size):
    """Takes the gapsize in between the circles and makes the spirograph."""
    for _ in range(int(360 / gap_size)):
        random_color()
        timmy.circle(100)  # makes a circle with radius 100
        timmy.setheading(
            timmy.heading() + gap_size
        )  # setting the new head position for the turtle by adding 10 degrees to the current head position


draw_spirograph(3)

# making an object from the "Screen" class
screen = Screen()
screen.exitonclick()
