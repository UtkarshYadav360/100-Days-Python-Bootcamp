from turtle import Turtle, Screen
import random

# EXERCISE 3 :
# generate a random walk


# random RGB colors for turtle
def random_color():
    """Generates a random float number between 0 and 1 and assign it to R,G,B."""
    R = random.random()
    G = random.random()
    B = random.random()
    timmy.color(R, G, B)


# making the random walk
def random_walk():
    """Generate a random walk for the turtle."""
    for _ in range(200):
        directions = [0, 90, 180, 270]
        timmy.forward(30)
        timmy.setheading(
            random.choice(directions)
        )  # sets the turtle heading to the specified direction
        random_color()


# making an object from the Turtle class
timmy = Turtle()
timmy.speed(5)
timmy.pensize(10)
random_walk()

# making an object from the Screen class
screen = Screen()
screen.setup(600, 600)
screen.exitonclick()
