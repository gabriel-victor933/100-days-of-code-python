from turtle import Turtle, Screen

tim = Turtle()
tom = Turtle()
screen = Screen()

tom.color('red')

def chooseOperation(turtle_name, direction):
    turtle = tim if turtle_name == 'tim' else tom

    if direction == 'forward':
        return move_forward(turtle)
    elif direction == 'backward':
        return move_backward(turtle)
    elif direction == 'right':
        return rotate_right(turtle)
    elif direction == 'left':
        return rotate_left(turtle)

def move_forward(turtle):
    print('running forward')
    turtle.forward(10)

def move_backward(turtle):
    turtle.backward(10)

def rotate_right(turtle):
    turtle.right(3.6)

def rotate_left(turtle):
    turtle.left(3.6)

def clear():
    tim.penup()
    tim.home()
    tim.clear()
    tim.pendown()
    
    

screen.listen()
screen.onkey(lambda: chooseOperation('tim','forward'),'w')
screen.onkey(lambda: chooseOperation('tim','backward'),'s')
screen.onkey(lambda: chooseOperation('tim','right'),'d')
screen.onkey(lambda: chooseOperation('tim','left'),'a')

screen.onkey(lambda: chooseOperation('tom','forward'),'Up')
screen.onkey(lambda: chooseOperation('tom','backward'),'Down')
screen.onkey(lambda: chooseOperation('tom','right'),'Left')
screen.onkey(lambda: chooseOperation('tom','left'),'Right')
screen.onkey(clear,'c')

screen.onkey(clear,'c')

screen.exitonclick()