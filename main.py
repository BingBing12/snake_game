from turtle import Turtle, Screen
import time
from snake import Snake


def left():
    snake.head.left(90)


def right():
    snake.head.right(90)


screen = Screen()
screen.setup(height=600, width=600)
screen.title("Snakes")
screen.bgcolor("black")
screen.tracer(0)
screen.onkeypress(left, "a")
screen.onkeypress(right, "s")
screen.listen()

snake = Snake()

game_over = False
while not game_over:
    screen.update()
    if snake.head.xcor() > 280 or snake.head.ycor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() < -280:
        game_over = True
    snake.snake_move()
    time.sleep(0.1)
screen.exitonclick()
