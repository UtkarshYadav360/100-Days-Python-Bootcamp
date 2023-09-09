# creating a "Class" from an "Object"
# SYNTAX : object = class # pascalCase()

# importing Turtle class and Screen class from the turtle module
from turtle import Turtle, Screen

# making a new "Object" named "timmy", from the "turtle Class", of the "turtle module".
timmy = Turtle()


# accessing "attributes" from the "object"
# SYNTAX : object.attribute
my_screen = Screen()
print(my_screen.canvheight)


# accessing "methods" from the "object"
# SYNTAX : object.method()
timmy.shape("turtle")
timmy.color("chartreuse4")
timmy.forward(100)
my_screen.exitonclick()
