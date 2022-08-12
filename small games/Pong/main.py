from turtle import Screen
from Paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard
# screen
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")


game_on = True
while game_on:
    time.sleep(ball.movespeed)
    screen.update()
    ball.up()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

# detect paddles
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320:
            ball.bounce_x()
            scoreboard.r_point()
            scoreboard.update()

    if ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        scoreboard.l_point()
        scoreboard.update()

# missing the ball
    if ball.xcor() > 380:
        ball.reset()
        scoreboard.l_point()
        scoreboard.update()

    if ball.xcor() < -380:
        ball.reset()
        scoreboard.r_point()
        scoreboard.update()



screen.exitonclick()






