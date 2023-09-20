from turtle import Turtle


# creating the scoreboard class
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.left_score = 0
        self.right_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(x=-100, y=180)
        self.write(f"{self.left_score}", align="center", font=("Mooli", 80, "normal"))
        self.goto(x=100, y=180)
        self.write(f"{self.right_score}", align="center", font=("Mooli", 80, "normal"))

    def left_point(self):
        self.left_score += 1
        self.update_scoreboard()

    def right_point(self):
        self.right_score += 1
        self.update_scoreboard()
