from turtle import Turtle


SCORE_POSITION = (0, 260)
SCORE_FONT = ("Helvetica", 20, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.color("black")
        self.goto(SCORE_POSITION)
        self.write(f"Score: {self.score}", align="center", font=SCORE_FONT)

    def write_score(self):
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=SCORE_FONT)
