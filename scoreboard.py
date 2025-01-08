from turtle import Turtle

ALIGN = "center"
FONT = ("Arial", 12, "bold")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.score = 0
        self.goto(-230, 260)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Level : {self.score}", align=ALIGN, font=FONT)

    def increment(self):
        self.score += 1
        self.update_score()
