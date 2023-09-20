from turtle import Turtle


# creating the ball class
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.ball_speed = 0.1

    def move(self):
        """Moves the ball to the right top of the screen."""
        new_x_pos = self.xcor() + self.x_move
        new_y_pos = self.ycor() + self.y_move
        self.goto(new_x_pos, new_y_pos)

    def bounce_y(self):
        """Bounce the ball and changes it's y_direction."""
        self.y_move *= -1
        self.ball_speed *= 0.9

    def bounce_x(self):
        """Bounce the ball and changes it's x_direction."""
        self.x_move *= -1
        self.ball_speed *= 0.9

    def reset_position(self):
        self.goto(0, 0)
        self.ball_speed = 0.1
        self.bounce_x()
