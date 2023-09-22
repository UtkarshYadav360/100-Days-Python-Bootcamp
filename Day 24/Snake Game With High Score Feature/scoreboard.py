from turtle import Turtle

# CONSTANTS FOR THE SCOREBOARD
FONT = ("mooli", 18, "normal")
ALIGNMENT = "center"

# NOTE : write() used to write the text on the turtle screen


# creating the score board class
class Scoreboard(Turtle):
    def __init__(self):
        """Makes the scoreboard."""
        super().__init__()
        self.score = 0
        # opening the file where high score will be stored
        with open("data.txt") as data:
            # converting the numbered string as an integer
            self.high_score = int(data.read())
        self.color("darkorange")
        self.penup()
        self.goto(x=0, y=270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        """Updates the scoreboard."""
        self.clear()
        self.write(
            f"Score: {self.score}, High Score: {self.high_score}",
            align=ALIGNMENT,
            font=FONT,
        )

    def increase_score(self):
        """Increase the scoreboard."""
        self.score += 1
        self.clear()
        self.write(arg=(f"Score : {self.score}"), font=FONT, align=ALIGNMENT)

    def reset(self):
        """Keep track of the current score and high score, and sets the high score if the current score is greater than the previous one."""
        if self.score > self.high_score:
            self.high_score = self.score
            # opening the file where high score will be stored
            with open("data.txt", mode="w") as data:
                # writing the high score in the file
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()
