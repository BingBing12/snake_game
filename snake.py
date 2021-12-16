from turtle import Turtle


class Snake(Turtle):
    def __init__(self):
        super().__init__()
        self.length = 3
        self.segments = []
        self.pos = 0
        self.add_segments()
        self.head = self.segments[0]

    def add_segments(self):
        for i in range(self.length):
            new_segment = Turtle(shape="square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.setx(self.pos)
            self.pos -= 20
            self.segments.append(new_segment)

    def snake_move(self):
        for index in range(self.length - 1, 0, -1):
            next_pos = self.segments[index - 1].pos()
            self.segments[index].setpos(next_pos)
        self.head.forward(20)
