from turtle import Turtle
from constants import *

class Score(Turtle):

    def __init__(self):
        super().__init__(visible=False)
        self.player1_score = 0
        self.player2_score = 0
        self.color('white')
        self.penup()
        self.goto((0,SCREEN_HEIGHT//2 - 45))
        self.print_screen()

    def print_screen(self):
        self.clear()
        self.write(f"{self.player1_score}   {self.player2_score}", False, "center",('Arial',28,'normal'))
