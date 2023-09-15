# importing the "Turtle" and "Screen" class from the turtle module
from turtle import Turtle, Screen

# making an object from the "Turtle" class
timmy = Turtle()  # makes the screen
timmy.shape("turtle")  # changing the turtle pointer shape
timmy.color("green")  # changing the turtle color
timmy.forward(100)  # turtle moves forward
timmy.right(90)  # turtle faces right

# making an object from the "Screen" class
screen = Screen()  # allow us to change the screen functions
screen.exitonclick()  # screen exits when mouse clicks
