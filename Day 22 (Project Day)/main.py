from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# creating the screen
screen = Screen()
screen.bgcolor("black")
screen.setup(height=600, width=800)
screen.title("Pong")
screen.tracer(0)


# creating the paddle
right_paddle = Paddle(position=(360, 0))
left_paddle = Paddle(position=(-360, 0))

# creating the ball
ball = Ball()

# creating the scoreboard
scoreboard = Scoreboard()

# adding controls to the game
screen.listen()
screen.onkeypress(key="k", fun=right_paddle.move_up)
screen.onkeypress(key="m", fun=right_paddle.move_down)
screen.onkeypress(key="a", fun=left_paddle.move_up)
screen.onkeypress(key="z", fun=left_paddle.move_down)

# game is on
game_on = True
while game_on:
    time.sleep(ball.ball_speed)
    screen.update()
    ball.move()

    # detecting the collision with the wall
    if ball.ycor() == 290 or ball.ycor() == -290:
        ball.bounce_y()

    # detecting the collision with the paddle
    if (
        ball.distance(right_paddle) < 40
        and ball.xcor() > 320
        or ball.distance(left_paddle) < 40
        and ball.xcor() < -320
    ):
        ball.bounce_x()

    # detecting right paddle miss
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.left_point()

    # detecting left paddle miss
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.right_point()

screen.exitonclick()
