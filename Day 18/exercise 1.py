from turtle import Turtle, Screen

# EXERCISE 1 :
# draw a square

# making an object from the "Turtle" class
timmy = Turtle()
timmy.shape = "turtle"
timmy.color("green")

# drawing the square
timmy.right(90)
timmy.forward(100)
timmy.right(90)
timmy.forward(100)
timmy.right(90)
timmy.forward(100)
timmy.right(90)
timmy.forward(100)


# making an object from the "Screen" class
screen = Screen()
screen.exitonclick()
