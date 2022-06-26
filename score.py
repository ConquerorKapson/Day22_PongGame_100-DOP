from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0

    def display(self, x, y):
        self.clear()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(x, y)
        self.write(f"{self.score}", align="center", font=("courier", 24, "normal"))
