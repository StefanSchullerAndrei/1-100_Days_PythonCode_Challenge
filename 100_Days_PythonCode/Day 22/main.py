from turtle import Screen, Turtle
from Paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=1200, height=1000)
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((550, 0))
l_paddle = Paddle((-550, 0))

ball = Ball()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    # Detect collision
    if ball.ycor() > 300 or ball.ycor() < -300:
        ball.bounce()
screen.exitonclick()