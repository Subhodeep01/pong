from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

pos = [(350, 0), (-350, 0)]
pl1_scr = (-200, 280)
pl2_scr = (200, 280)

r_paddle = Paddle(pos[0])
l_paddle = Paddle(pos[1])
ball = Ball()
SB1 = ScoreBoard(pl1_scr)
SB2 = ScoreBoard(pl2_scr)

screen.listen()
screen.onkey(fun=r_paddle.go_up, key="Up")
screen.onkey(fun=r_paddle.go_down, key="Down")

screen.onkey(fun=l_paddle.go_up, key="w")
screen.onkey(fun=l_paddle.go_down, key="s")

game_is_on = True
while game_is_on:
    ball.move()
    screen.update()
    time.sleep(ball.move_speed)
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    if (ball.xcor() > 340 or ball.xcor() < -340) and (ball.distance(r_paddle) < 51 or ball.distance(l_paddle) < 51):
        ball.bounce_x()
    if ball.xcor() > 380:
        ball.refresh()
        SB1.update()
    elif ball.xcor() < -380:
        ball.refresh()
        SB2.update()

screen.exitonclick()
