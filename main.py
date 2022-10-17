from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

#setting up the screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
#0 in this function turns off the animation. update method is required to show the animation each time.
screen.tracer(0)

#creating paddles from Paddle class
l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))

ball = Ball()

scoreboard = Scoreboard()


screen.listen()
screen.onkey(l_paddle.go_up, key="w")
screen.onkey(l_paddle.go_down, key="s")
screen.onkey(r_paddle.go_up, key="Up")
screen.onkey(r_paddle.go_down, key="Down")

sleep_time = 0.1

game_is_on = True
while game_is_on:
    #pauses the while loop for 0.05 second
    time.sleep(sleep_time)
    screen.update()
    ball.move()

    #detect collision with wall
    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.bounce_y()

    #detect collision with paddles
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        sleep_time *= 0.9

    #detect when r_paddle misses the ball
    if ball.xcor() > 380:
        ball.reset()
        scoreboard.l_point()
        sleep_time = 0.1

    #detect when l_paddle misses the ball
    if ball.xcor() < -380:
        ball.reset()
        scoreboard.r_point()
        sleep_time = 0.1

#screen will stay and will only disappear if its clicked.
screen.exitonclick()