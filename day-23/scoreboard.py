from turtle import Turtle

FONT = ("Courier", 24, "normal")
FONT_GAMEOVER = ("Courier", 26, "bold")

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__(visible = False)
        self.penup()
        self.goto(-215,260)
        self.print_level()


    def print_level(self, game_level = 1):
        self.clear()
        self.write(f"Level: {game_level}",False,'center',FONT)

    def print_game_over(self):
        self.goto(0,0)
        self.write(f"Game Over",False,'center',FONT_GAMEOVER)
