from turtle import Turtle, Screen

# EXERCISE 2 :
# draw a dashed line

# making an object from the "Turtle" class
timmy = Turtle()
timmy.shape("turtle")
timmy.color("green")

# drawing a dashed line
for _ in range(15):
    timmy.forward(10)
    timmy.penup()  # no drawing when moving
    timmy.forward(10)
    timmy.pendown()  # drawing when moving

# making an object from the "Screen" class
screen = Screen()
screen.exitonclick()
