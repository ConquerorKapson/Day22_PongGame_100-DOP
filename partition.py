from turtle import Turtle


class Partition(Turtle):
    def __init__(self):
        super().__init__()

    def create_partition(self):
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_len=0.05, stretch_wid=30)
        self.goto(0, 0)

