from turtle import Turtle
import random 

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class Car(Turtle):
    
    def __init__(self):
        super().__init__(shape="square")
        self.color(random.choice(COLORS))
        self.penup()
        self.seth(180)
        self.shapesize(stretch_wid=1,stretch_len=2)
        self.random_start_position()
        
    def move(self, velocity_scale):
        self.forward(MOVE_INCREMENT*velocity_scale)

    def random_start_position(self):
        x_start_positing = random.randint(320,1020)
        y_start_positing = random.randint(-240,250)
        self.goto(x_start_positing, y_start_positing)


class CarManager:

    def __init__(self):
        self.cars = []
        for _ in range(20):
            car = Car()
            self.cars.append(car)

    def move_forward(self,game_level = 1):
        velocity_scale = 1 + game_level/5
        for car in self.cars:
            car.move(velocity_scale)
            
            if car.xcor() <= -325:
                car.random_start_position()