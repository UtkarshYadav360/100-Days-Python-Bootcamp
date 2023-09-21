import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# creating the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("coral")
screen.tracer(0)

# creating the player
player = Player()

# creating the cars
cars = CarManager()

# creating the scoreboard
scoreboard = Scoreboard()

# adding controls to the game
screen.listen()
screen.onkeypress(key="Up", fun=player.move_forward)

# game is on
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.generate_cars()
    cars.move_cars()

    # detecting the collision with the cars
    for car in cars.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    # detecting the collision with the top
    if player.is_at_finish_point():
        player.goto_start()
        cars.level_up()
        scoreboard.increase_level()


screen.exitonclick()
