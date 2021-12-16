from turtle import Turtle


class Instructions(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.set_instructions()

    def set_instructions(self):
        self.write("Click space to start. 'a' to turn left and 's' to turn right.", align="center")

    def clear_instructions(self):
        self.clear()
