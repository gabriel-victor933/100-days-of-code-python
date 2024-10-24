from turtle import Turtle

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.color('white')
        self.penup()
        self.hideturtle()
        self.get_high_score()
        self.write_score()
        

    def increase(self):
        self.score += 1
        self.write_score()

    def write_score(self):
        self.clear()
        self.goto(0,275)
        self.write(f'Score: {self.score} - High Score: {self.high_score}',False,'center',("Arial",12,'normal'))


    def game_over(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.set_high_score(self.score)

        self.score = 0

        self.goto(0,10)
        self.write('GAME OVER!',False,'center',("Arial",18,'normal'))

    def get_high_score(self):
        with open("day-20 & day-21/high_score.txt") as file:
            self.high_score = int(file.read())

    def set_high_score(self, new_high_score):
         with open("day-20 & day-21/high_score.txt","w") as file:
            file.write(str(new_high_score))