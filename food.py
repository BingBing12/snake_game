from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.8, stretch_wid=0.8)
        self.color("red")
        self.speed("fastest")
        self.generate_food()

    def generate_food(self):
        self.clear()
        random_position = (random.randint(-270, 270), random.randint(-270, 270))
        self.goto(random_position)

