from turtle import Screen
from platform import Platform
from ball import Ball 
from score import Score 
import time
from constants import *

screen = Screen()

screen.setup(SCREEN_WIDTH,SCREEN_HEIGHT)
screen.bgcolor('black')
screen.tracer(0)

platform1 = Platform(-470)
platform2 = Platform(470)

ball = Ball()

score = Score()

screen.update()
screen.listen()
screen.onkey(platform1.up,"w")
screen.onkey(platform1.down,"s")
screen.onkey(platform2.up,"Up")
screen.onkey(platform2.down,"Down")

while True:
    ball.move()

    if platform1.check_collision(ball.pos()) or platform2.check_collision(ball.pos()):
        ball.x_orientation *= -1
    
    if ball.xcor() <= -(SCREEN_WIDTH//2) or ball.xcor() >= (SCREEN_WIDTH//2): 
        time.sleep(2)
        if ball.x_orientation > 0:
            score.player1_score += 1
        else:
            score.player2_score += 1
        score.print_screen()
        ball.start_game()

    screen.update()
    time.sleep(0.1)

screen.exitonclick()