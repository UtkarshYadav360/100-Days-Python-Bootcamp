from turtle import Turtle


# making the paddle class
class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        # creating the paddle
        self.shape("square")
        self.color("white")
        self.speed("fastest")
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.penup()
        self.goto(position)

    def move_up(self):
        """Move the paddle upwards."""
        new_y_pos = self.ycor() + 20
        self.goto(x=self.xcor(), y=new_y_pos)

    def move_down(self):
        """Move the paddle downwards."""
        new_y_pos = self.ycor() - 20
        self.goto(x=self.xcor(), y=new_y_pos)
