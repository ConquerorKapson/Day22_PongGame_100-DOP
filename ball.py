from turtle import Turtle
from paddle import Paddle

INCREASE = 5
DECREASE = -5


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.shapesize(1)
        self.goto(0, 0)
        self.x = 5
        self.y = 5

    def move(self):
        x = self.xcor() + self.x
        y = self.ycor() + self.y
        self.penup()
        self.goto(x, y)

    def y_bounce(self):
        self.y *= -1

    def x_bounce(self):
        self.x *= -1

    def game_over(self, text):
        self.pencolor("Blue")
        self.write(f"{text} is the winner!!!", align="center", font=("Courier", 24, "bold"))

    def restart(self):
        self.goto(0, 0)
