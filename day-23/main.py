import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = Player()
car_manager = CarManager()
score = Scoreboard()

screen.onkey(player.move,"Up")

game_level = 1
game_is_on =  True
while game_is_on:

    car_manager.move_forward(game_level)

    for car in car_manager.cars:
        if player.distance(car) < 20:
            score.print_game_over()
            time.sleep(1)
            game_is_on = False

    if player.ycor() >= 300:
        time.sleep(1)
        game_level += 1
        player.move_to_start_position()
        score.print_level(game_level)

    time.sleep(0.1)
    screen.update()
