from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time


# SETTING UP THE SCREEN
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")  # sets the background color of the turtle window
screen.title("Snake Game")  # sets the title of the turtle window
screen.tracer(0)  # on/off the turtle animation and set delay to update drawings

# creating the snake
snake = Snake()

# creating the food
food = Food()

# creating the scoreboard
scoreboard = Scoreboard()

# adding controls to the game
screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)


# game is on
game_on = True

# make a delay of 0.1 seconds and refresh the screen when the game is started
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()  # snake moves one step forward, each time the screen refreshes

    # detecting the collision with food
    if snake.snake_head.distance(food) < 15:
        food.refresh()
        snake.extend_snake()
        scoreboard.increase_score()

    # detecting the collision with wall
    if (
        snake.snake_head.xcor() > 298
        or snake.snake_head.xcor() < -300
        or snake.snake_head.ycor() > 300
        or snake.snake_head.ycor() < -298
    ):
        scoreboard.reset()
        snake.reset()

    # detecting the collision with tail
    for segment in snake.segments[1:]:
        if snake.snake_head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()

# exit the screen on single mouse click
screen.exitonclick()
