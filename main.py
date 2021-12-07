from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor('black')
screen.setup(width = 800, height = 600)
screen.title('Pong')
screen.tracer(0)

right_paddle = Paddle('right')
left_paddle = Paddle('left')
ball = Ball()

scoreboard = Scoreboard()

game_on = True
screen.listen()
screen.onkeypress(right_paddle.go_up, "Up")
screen.onkeypress(left_paddle.go_up, "w")
screen.onkeypress(right_paddle.go_down, "Down")
screen.onkeypress(left_paddle.go_down, "s")

while game_on:
    time.sleep(0.1)
    screen.update()
    ball.move_ball()
    # collision with wall
    if ball.ycor() > 280 or ball.ycor() < - 280:
        ball.bounce_y()
    # collision with paddle
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or \
            ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # out of bonds
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()




screen.exitonclick()