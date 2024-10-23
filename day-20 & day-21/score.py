from turtle import Turtle

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('white')
        self.penup()
        self.goto(0,275)
        self.hideturtle()
        self.write(f'Score: {self.score}',False,'center',("Arial",12,'normal'))

    def increase(self):
        self.clear()
        self.score += 1
        self.write(f'Score: {self.score}',False,'center',("Arial",12,'normal'))

    def game_over(self):
        self.goto(0,10)
        self.write('GAME OVER!',False,'center',("Arial",18,'normal'))
