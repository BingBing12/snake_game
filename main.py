from turtle import Screen
import time
from snake import Snake
from food import Food
from score import Score
from instructions import Instructions


def left():
    snake.head.left(90)


def right():
    snake.head.right(90)


def start_game():
    instructions.clear_instructions()
    start()


screen = Screen()
screen.setup(height=600, width=600)
screen.title("Snakes")
screen.bgcolor("black")
screen.tracer(0)
screen.onkeypress(left, "a")
screen.onkeypress(right, "s")
screen.onkeypress(start_game, "space")
screen.listen()

snake = Snake()
food = Food()
score = Score()
instructions = Instructions()


def start():
    game_over = False
    while not game_over:
        screen.update()
        for segment in snake.segments[1:]:
            if snake.head.distance(segment) < 10:
                score.game_over()
                game_over = True
        if snake.head.distance(food) < 15:
            food.generate_food()
            score.increment()
            snake.grow()
        if snake.head.xcor() > 280 or snake.head.ycor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() < -280:
            score.game_over()
            game_over = True
        snake.snake_move()
        time.sleep(0.1)


screen.exitonclick()
