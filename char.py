from turtle import Turtle

STEP = 10
STARTING_POSITION = (0, -280)


class MyTurtle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.setheading(90)
        self.respawn()

    def up(self):
        self.fd(STEP)

    def respawn(self):
        self.goto(STARTING_POSITION)
