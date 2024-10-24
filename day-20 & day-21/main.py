from turtle import Screen
import time 
from snake import Snake
from food import Food
from score import Score

screen = Screen()

screen.setup(width=600,height=600)
screen.bgcolor('black')
screen.title('My snake game')
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")
screen.onkey(screen.bye,"x")

while True:
    screen.update()
    time.sleep(0.1)

    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor()> 280 or snake.head.ycor() < -280 or snake.check_collision():
        score.game_over()
        time.sleep(2)

        score.write_score()
        snake.reset()



