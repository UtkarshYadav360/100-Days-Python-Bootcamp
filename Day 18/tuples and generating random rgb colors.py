import turtle as t
import random

# tuples are immutable (cannot be modified)

# making a tuple :
tup1 = (1,)  # tuple with single element
print(tup1, type(tup1))

tup2 = (1, 2, 3, 4, 5)
print(tup2, type(tup2))

# accessing tuple elements using indexing
print(tup2[0])
print(tup2[1])
print(tup2[2])
print(tup2[3])
print(tup2[4])


# RE-CREATION OF EXERCISE 4 :


def random_color():
    "Generating a random color for the turtle."
    R = random.randint(0, 255)
    G = random.randint(0, 255)
    B = random.randint(0, 255)
    random_color = (R, G, B)
    return random_color


def random_walk():
    """Generating a random walk for the turtle."""
    for _ in range(200):
        directions = [0, 90, 180, 270]
        timmy.forward(30)
        timmy.setheading(random.choice(directions))
        timmy.color(random_color())


timmy = t.Turtle()
timmy.speed(5)
timmy.pensize(10)
t.colormode(255)  # used to set the color model for the turtle pen

random_walk()

screen = t.Screen()
screen.exitonclick()
