import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import ScoreBoard
import random

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()

screen.listen()
screen.onkey(player.move, "Up")

scoreboard = ScoreBoard()

car_manager = CarManager()

turtle_is_alive = True
while turtle_is_alive:
    time.sleep(0.1)
    scoreboard.update()
    if random.randint(1,6) == 6:
        car_manager.create_car()
    car_manager.move_cars()

    if car_manager.turtle_hit_by_car(player):
        print("ouch...")
        turtle_is_alive = False
        scoreboard.game_over()

    if player.made_it_across():
        player.move_to_start()
        car_manager.increase_speed()
        scoreboard.increase_level()

    screen.update()

screen.exitonclick()