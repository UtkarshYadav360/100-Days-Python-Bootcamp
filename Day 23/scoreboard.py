from turtle import Turtle

# CONSTANTS FOR THE SCOREBOARD
FONT = ("Courier", 24, "normal")


# creating the scoreboard class
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.hideturtle()
        self.color("red")
        self.goto(x=-200, y=230)
        self.update_scoreboard()

    def update_scoreboard(self):
        """Updates the scoreboard."""
        self.clear()
        self.write(f"Level: {self.level}", align="center", font=FONT)

    def increase_level(self):
        """Increases the game level."""
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        """Game Over."""
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)
