import turtle as t
import random

# PROJECT 19 :
# TURTLE RACE


# NOTE : fillcolor() fills the turtle with the specified color. But it's body is outlined with black color.
# NOTE : xcor() returns the x-coordinates of the turtle


# colors of the turtle
colors = ["red", "darkgoldenrod", "orangered", "green", "blue", "purple"]

# y axis for the turtles
y_positions = [-70, -40, -10, 20, 50, 80]

# race is not started
race_started = False

# all turtles will be stored here
all_turtles = []

# making the turtle screen
screen = t.Screen()
screen.setup(width=500, height=400)  # sets the width and height of the turtle window
user_bet = screen.textinput(
    title="Make Your Bet", prompt="Which turtle will win the race? Choose a color : "
)  # makes a popup window asking for the bet


# making turtles
for number_of_turtles in range(0, 6):
    turtles = t.Turtle(shape="turtle")
    turtles.penup()
    turtles.fillcolor(colors[number_of_turtles])
    turtles.goto(x=-240, y=y_positions[number_of_turtles])
    all_turtles.append(turtles)

# race starts when the user enters their bet
if user_bet:
    race_started = True

# turtles start to move when the race is started
while race_started:
    for turtle in all_turtles:
        if turtle.xcor() > 220:
            race_started = False
            winning_color = turtle.fillcolor()
            if winning_color == user_bet:  #
                print(f"You've Won! The {winning_color} turtle is the winner.")
            else:
                print(f"You've Lost! The {winning_color} turtle is the winner.")

        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)
screen.exitonclick()
