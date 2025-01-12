from turtle import Screen
from char import MyTurtle
from car_manager import CarManager
from scoreboard import ScoreBoard
import time, random


screen = Screen()
screen.setup(height=600, width=550)
screen.tracer(0)
screen.listen()
screen.colormode()

player = MyTurtle()
score = ScoreBoard()
car = CarManager()
screen.onkeypress(player.up, "Up")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.create_car()
    car.move()
    if player.at_finish_line():
        player.respawn()
        score.increment()
        car.increase_speed()
    # collides with car
    for c in car.all_car:
        if player.distance(c) < 20:
            score.game_over()
            game_is_on = False


# dosen menambah perubahan disini
screen.exitonclick()
