from turtle import Screen, Turtle
import pandas
import time

data = pandas.read_csv("day-25/50_states.csv")

states = data['state'].to_list()
lower_state = [state.lower() for state in states]

x_cord = data['x'].to_list()
y_cord = data['y'].to_list()

turtle = Turtle()
drawer = Turtle(visible=False)
screen = Screen()
screen.title('U.S States game')
img = 'day-25/blank_states_img.gif'
screen.addshape(img)

turtle.shape(img)
drawer.penup()

num_state = 0

guessed = []

while num_state < 50:
    state = screen.textinput(f"{num_state}/50 State Correct","Insert the name of the state: ").lower()

    if state == 'exit':
        break

    if state in guessed:
        continue

    if state in lower_state:

        index = lower_state.index(state)

        drawer.goto(x_cord[index],y_cord[index])

        drawer.write(states[index],False,"center",("arial",8,"normal"))

        num_state += 1

        guessed.append(state)

        time.sleep(0.5)
    

screen.bye()
