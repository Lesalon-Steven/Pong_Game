from turtle import Screen, Turtle
import time
from ball import Ball
from paddle import Paddle
from scoreboard import Scoreboard

scores = Scoreboard()
screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

ball = Ball()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    ball.move_ball()
    if ball.ycor() > 270 or ball.ycor() < -270:
        ball.bounce_y()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        print("made contact")
        ball.bounce_x()
    # Detect Right paddle Miss
    if ball.xcor() > 380:

        scores.l_point()
        screen.update()

        ball.reset_position()
    # detect Left Paddle Miss
    if ball.xcor() < -380:
        screen.update()
        scores.r_point()
        ball.reset_position()
    screen.update()

screen.exitonclick()
