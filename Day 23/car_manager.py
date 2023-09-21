from turtle import Turtle
import random

# CONSTANTS FOR THE CARS
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


# creating the car manager class
class CarManager(Turtle):
    def __init__(self):
        # all cars will be stored here
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def generate_cars(self):
        """Generate cars along the y axis."""
        # SLOWING DOWN THE SPEED OF GENERATING THE CARS
        random_number = random.randint(1, 6)  # generating a random number from 1 to 6
        if random_number == 1:  # if the random is 1 then the car will be created
            new_car = Turtle()
            new_car.shape("square")
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            new_car.color(random.choice(COLORS))
            new_car.penup()
            random_y_pos = random.randint(-250, 250)
            new_car.goto(x=300, y=random_y_pos)
            self.all_cars.append(new_car)

    def move_cars(self):
        """Move the cars from right to left direction"""
        for car in self.all_cars:
            car.backward(self.car_speed)

    def level_up(self):
        """Speed up the cars each time the player got a level up."""
        self.car_speed += MOVE_INCREMENT
