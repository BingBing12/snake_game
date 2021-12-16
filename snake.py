from turtle import Turtle


class Snake(Turtle):
    def __init__(self):
        super().__init__()
        self.length = 0
        self.segments = []
        self.starting_pos = [(0, 0), (-20, 0), (-40, 0,)]
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for pos in self.starting_pos:
            self.add_segment(pos)

    def add_segment(self, position):
        new_segment = Turtle(shape="square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)
        self.length += 1

    def snake_move(self):
        for index in range(self.length - 1, 0, -1):
            next_pos = self.segments[index - 1].pos()
            self.segments[index].setpos(next_pos)
        self.head.forward(20)

    def grow(self):
        self.add_segment(self.segments[-1].position())