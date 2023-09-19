from turtle import Turtle
import random

# NOTE : shapesize() changes the shape stretch size, and resize the shape.
# NOTE : distance() compares the turtle (x, y) position with the given turtle (x, y) position.


# creating the food class
class Food(Turtle):
    # this function makes the food for the snake
    def __init__(self):
        """Makes the food for the snake."""
        super().__init__()
        self.penup()
        self.shape("circle")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)  # food size is 10 by 10
        self.color("darkred")
        self.speed("fastest")
        self.refresh()

    # this function refresh the food position each time the snake head hits the food
    def refresh(self):
        """Refresh/Randomize the food position each time the snake head hits the food."""
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
