import turtle as t
from hirst_image_colors import image_colors
import random

# PROJECT 18 :
# HIRST PAINTING

# NOTE : turtle.colormode() allow us to choose the color between 0 to 1 or 0 to 255.


# making an object from the turtle class
t.colormode(255)
timmy = t.Turtle()
timmy.penup()
timmy.speed("fastest")
timmy.hideturtle()
timmy.setheading(
    225
)  # setting the turtle head direction to the desired position on the screen
timmy.forward(300)  # (forward distance * number of dots) 50 * 6 = 300
timmy.setheading(0)  # setting the turtle head direction to the original position

# number of dots to be drawn
number_of_dots = 100

# loop runs till the hundred dots will be created
for dots in range(1, number_of_dots + 1):
    timmy.dot(20, random.choice(image_colors))  # generates colored dots
    timmy.forward(50)

    # make 10 dots in 10 lines
    if dots % 10 == 0:
        timmy.setheading(90)
        timmy.forward(50)
        timmy.setheading(180)
        timmy.forward(500)
        timmy.setheading(0)


# making an object from the screen class
screen = t.Screen()
screen.exitonclick()
