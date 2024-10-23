from turtle import Turtle
from constants import *

class Platform:
    
    def __init__(self,x_cor = 0):
        self.components = []
        for i in range(4):
            component = Turtle(shape='square')
            component.penup()
            component.color('white')
            component.goto(x_cor,MOVE_STEP*(1 - i))
            component.seth(90)
            self.components.append(component)


    def up(self):
        head = self.components[0]

        if head.ycor() >= SCREEN_HEIGHT//2 - MOVE_STEP:
            return
        
        for component in self.components:
            component.forward(MOVE_STEP)

    def down(self):
        tail = self.components[-1]

        if tail.ycor() <= -(SCREEN_HEIGHT//2 - MOVE_STEP):
            return
        
        for component in self.components:
            component.backward(MOVE_STEP)

    def check_collision(self,pos):
        for component in self.components:
            if component.distance(pos) < 20:
                return True
        
        return False
        