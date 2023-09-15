from turtle import Turtle, Screen
import random

# EXERCISE 3 :
# draw a triangle, square, pentagon, hexagon, heptagon, octagon, nonagon and decagon

# NOTE : To get the angle of the shape ==>  (360/sides of the shape)


# random RGB colors for the turtle
def change_color():
    """Generates a random float number between 0 and 1 and assign it to R,G,B"""
    R = random.random()
    G = random.random()
    B = random.random()
    timmy.color(R, G, B)


# making an object from the "Turtle" class
timmy = Turtle()
timmy.speed(10)  # sets the turtle speed
timmy.penup()
timmy.hideturtle()  # make turtle invisible
timmy.showturtle()  # make turtle visible
timmy.pendown()


# drawing the shapes
def draw_shapes(number_of_sides):
    angle_of_shapes = 360 / number_of_sides
    for _ in range(number_of_sides):
        timmy.forward(100)
        timmy.right(angle_of_shapes)
    change_color()


# calling the function to draw shapes
for shape_sides in range(3, 11):
    draw_shapes(shape_sides)

# making an object from the "Screen" class
timmy.right(51)
screen = Screen()
screen.exitonclick()
