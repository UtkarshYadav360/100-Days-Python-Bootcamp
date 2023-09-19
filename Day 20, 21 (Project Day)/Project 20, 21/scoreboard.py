from turtle import Turtle

# CONSTANTS FOR THE SCOREBOARD
FONT = ("mooli", 18, "normal")
ALIGNMENT = "center"

# NOTE : write() used to write the text on the turtle screen


# creating the score board class
class Scoreboard(Turtle):
    # this function makes the scoreboard
    def __init__(self):
        """Makes the scoreboard."""
        super().__init__()
        self.score = 0
        self.color("darkorange")
        self.penup()
        self.goto(x=0, y=270)
        self.hideturtle()
        self.write(arg=(f"Score : {self.score}"), font=FONT, align=ALIGNMENT)

    # this function increase/update the scoreboard
    def increase_score(self):
        """Increase/Update the scoreboard."""
        self.score += 1
        self.clear()
        self.write(arg=(f"Score : {self.score}"), font=FONT, align=ALIGNMENT)

    # this function shows the game over message on the turtle screen
    def game_over(self):
        """Shows the game over message on the turtle screen."""
        self.goto(0, 0)
        self.write(
            arg=(f"Game Over!"),
            font=(("mooli", 30, "normal")),
            align=ALIGNMENT,
        )
