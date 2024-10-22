from turtle import *
import random
import colorgram

colors = colorgram.extract('day-18/download.webp',30)


tim = Turtle()
screen = Screen()
screen.colormode(255)

y_init_position = -300
x_init_position = -370

tim.penup()

tim.speed(20)

tim.hideturtle()

for _ in range(22):
    tim.setx(x_init_position)
    tim.sety(y_init_position)

    for _ in range(25):
        color = random.choice(colors)
        tim.pencolor(color.rgb)
        tim.dot(20)
        tim.forward(30)

    y_init_position += 30



screen.exitonclick()
