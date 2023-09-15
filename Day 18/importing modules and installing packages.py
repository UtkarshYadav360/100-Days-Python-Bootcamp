# There are a few methods to import a module :

# 1) import turtle
# basic way to import a module, where we need to use the module name each time we make an object.
# EXAMPLE ==> timmy = turtle.Turtle()


# 2) from turtle import Turtle, Screen
# just import the specifed classes from the module, we don't need to use the module name each time while making an object.
# EXAMPLE ==> timmy = Turtle()


# 3) from turtle import *
# import every class from the module, using it can be confusing.
# EXAMPLE ==>
# shape("turtle")
# color("green")

# right(90)
# forward(100)
# right(90)
# forward(100)
# right(90)
# forward(100)
# right(90)
# forward(100)

# exitonclick()


# 4) import turtle as t
# it is almost same as the basic import, but we have to use the alias name while making an object.
# EXAMPLE ==> timmy = t.Turtle()


# Here's a module names "heroes", which is used to generate heroes name. But it cannot be imported and used before installing.
import heroes

print(heroes.gen())
print(heroes.genarr(3))
