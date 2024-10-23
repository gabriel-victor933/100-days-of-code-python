from turtle import Turtle

MOVE_STEP = 20

DIRECTIONS = {
    'north': 90,
    'south': 270,
    'east': 0,
    'west': 180,
}

class Snake:
    def __init__(self):
        self.segments = []
        self.created_snake()
        self.head = self.segments[0]

    def created_snake(self):
        for i in range(3):
            self.add_segment((-MOVE_STEP*i,0))

    def move(self):
        for i in range(len(self.segments)-1,0,-1):
            self.segments[i].goto(self.segments[i-1].pos())
        self.head.forward(MOVE_STEP)

    def up(self):
        if self.head.heading() != DIRECTIONS['south']:
            self.head.setheading(DIRECTIONS['north'])

    def down(self):
        if self.head.heading() != DIRECTIONS['north']:
            self.head.setheading(DIRECTIONS['south'])

    def left(self):
        if self.head.heading() != DIRECTIONS['east']:
            self.head.setheading(DIRECTIONS['west'])

    def right(self):
        if self.head.heading() != DIRECTIONS['west']:
            self.head.setheading(DIRECTIONS['east'])

    def add_segment(self,position):
        segment = Turtle(shape='square')
        segment.penup()
        segment.goto(position)
        segment.color('white')
        self.segments.append(segment)
        segment.speed(10)

    def extend(self):
        self.add_segment(self.segments[-1].pos())

    def check_collision(self):
        for segment in self.segments[1:]:
            if self.head.distance(segment) < 10:
                return True
        
        return False

        