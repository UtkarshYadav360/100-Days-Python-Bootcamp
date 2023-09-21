from turtle import Turtle

# CONSTANTS FOR THE PLAYER
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


# creating the player class
class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.goto_start()
        self.setheading(90)

    def move_forward(self):
        """Moves the player forward."""
        self.forward(MOVE_DISTANCE)

    def is_at_finish_point(self):
        """Return True if the player is at the top, else return False."""
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False

    def goto_start(self):
        """Moves player to the starting position, when the player reaches the top."""
        self.goto(STARTING_POSITION)
