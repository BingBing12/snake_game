from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, 280)
        self.display()

    def display(self):
        self.clear()
        self.write(f"Score: {self.score}", align="center")

    def increment(self):
        self.score += 1
        self.display()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center")


