from turtle import Turtle
import random 
from constants import *

class Ball(Turtle):

    def __init__(self):
        super().__init__(shape="square")
        self.penup()
        self.color('white')
        self.x_orientation = -1
        self.y_orientation = -1
        self.sety(random.randint(-260,260))

    def move(self):
        (x_position, y_position) = self.pos()

        if y_position >= 280 or y_position <= -280:
            self.y_orientation *= -1

        x_position += self.x_orientation*10
        y_position += self.y_orientation*10

        self.goto(x_position,y_position)

    def start_game(self):
        self.x_orientation *= 1
        self.sety(random.randint(-260,260))
        self.setx(0)
