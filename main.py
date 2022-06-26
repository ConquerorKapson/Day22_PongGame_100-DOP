from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Score
from partition import Partition
import time
X_RIGHT = 420
X = 900
Y = 500

screen = Screen()
screen.setup(width=X, height=Y)
screen.bgcolor("black")
screen.tracer(0)

l_paddle = Paddle(-400, 0)
r_paddle = Paddle(400, 0)

ball = Ball()

l_score = Score()
r_score = Score()

partition = Partition()
partition.create_partition()

screen.listen()
screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(r_paddle.go_down, "Down")
screen.onkeypress(l_paddle.go_down, "s")

game_is_on = True
sleep_time = 0.013
while game_is_on:
    time.sleep(sleep_time)
    ball.move()

    if 230 < ball.ycor() or ball.ycor() < -230:
        ball.y_bounce()

    if 430 < ball.xcor():
        l_score.score += 1
        ball.restart()
        ball.x_bounce()

    if ball.xcor() < -430:
        r_score.score += 1
        ball.restart()
        ball.x_bounce()

    # sleep_time -= max(r_score.score, l_score.score)*0.010

    if ball.distance(r_paddle) < 50 and ball.xcor() > 380 or ball.distance(l_paddle) < 50 and ball.xcor() < -380:
        ball.x_bounce()

    l_score.display(-70, 200)
    r_score.display(70, 200)

    if r_score.score >= 5:
        game_is_on = False
        ball.game_over("Right Side")

    if l_score.score >= 5:
        game_is_on = False
        ball.game_over("Left Side")
    screen.update()

screen.exitonclick()
