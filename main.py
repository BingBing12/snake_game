from turtle import Turtle, Screen
import time


def left():
    segments[0].left(90)


def right():
    segments[0].right(90)


screen = Screen()
screen.setup(height=600, width=600)
screen.title("Snakes")
screen.bgcolor("black")
screen.tracer(0)
screen.onkeypress(left, "a")
screen.onkeypress(right, "s")
screen.listen()
length = 10
pos = 0
segments = []
for i in range(length):
    new_segment = Turtle(shape="square")
    new_segment.color("white")
    new_segment.penup()
    new_segment.setx(pos)
    pos -= 20
    segments.append(new_segment)
game_over = False
while not game_over:
    screen.update()
    if segments[0].xcor() > 280 or segments[0].ycor() > 280 or segments[0].xcor() < -280 or segments[0].ycor() < -280:
        game_over = True
    for index in range(length - 1, 0, -1):
        next_pos = segments[index - 1].pos()
        segments[index].setpos(next_pos)
    segments[0].forward(20)
    time.sleep(0.1)
screen.exitonclick()
