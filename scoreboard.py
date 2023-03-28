from turtle import Turtle


SCORE_POSITION = (0, 260)
SCORE_FONT = ("Helvetica", 20, "normal")
ALIGN = "center"


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.color("black")
        self.goto(SCORE_POSITION)
        self.write(f"Score: {self.score}", align=ALIGN, font=SCORE_FONT)

    def write_score(self):
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score}", align=ALIGN, font=SCORE_FONT)

    def game_over(self):
        self.goto((0, 0))
        self.write("    Your snake is puny!\nCrawl back to your cave!", align=ALIGN, font=SCORE_FONT)
