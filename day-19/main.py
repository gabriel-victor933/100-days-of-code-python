from turtle import Turtle, Screen
import random

colors = ['red','orange','yellow','green','blue','purple']

screen = Screen()
screen.setup(width=500,height=400)
user_bet = screen.textinput("Make your bet", "Witch turtle will win the race? Enter a color: ")


turtles = []

for i in range(len(colors)):
    turtle = Turtle('turtle')
    turtle.penup()
    y_position = - 90 + 40*i
    turtle.goto(-240,y_position)
    turtle.color(colors[i])
    turtles.append(turtle)

while True:
    for turtle in turtles:
        turtle.forward(random.randint(0,10))
    
    xcords = []
    for turtle in turtles:
        xcords.append(turtle.xcor())

    max_xcord = max(xcords)

    if max_xcord >= 250 - 20:
        index = xcords.index(max_xcord)
        winner = turtles[index]
        break

if user_bet == winner.pencolor():
    print('You Win!')
else: 
    print('You Lose!')

screen.bye()