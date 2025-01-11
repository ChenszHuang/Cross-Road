from turtle import Turtle
import random

INCREMENT = 5


class CarManager:
    def __init__(self):
        self.all_car = []
        self.colour = [
            "red",
            "blue",
            "green",
            "yellow",
            "purple",
            "orange",
            "pink",
            "black",
            "aqua",
        ]
        self.step = 10

    def create_car(self):
        chance = random.randint(1, 6)
        if chance == 6:
            new_car = Turtle("square")
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            new_car.color(random.choice(self.colour))
            new_car.penup()
            new_car.goto(300, random.randrange(-250, 250, 5))
            self.all_car.append(new_car)

    def move(self):
        for car in self.all_car:
            car.bk(self.step)
            if car.xcor() < -300:
                self.all_car.remove(car)

    def increase_speed(self):
        self.step += INCREMENT
