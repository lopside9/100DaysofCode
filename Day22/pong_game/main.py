from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

# Creating a screen for the game
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

# # Creating paddles using the Paddle class (from Paddle.py)
r_paddle = Paddle(xcor=350, ycor=0)
l_paddle = Paddle(xcor=-350, ycor=0)
ball = Ball()
scoreboard = Scoreboard()

# Coding screen to listen
screen.listen()

# Coding paddle so it can be controlled with up and down keys
screen.onkey(fun=r_paddle.paddle_move_up, key="Up")
screen.onkey(fun=r_paddle.paddle_move_down, key="Down")
screen.onkey(fun=l_paddle.paddle_move_up, key="w")
screen.onkey(fun=l_paddle.paddle_move_down, key="s")


game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    ball.ball_movement()
    screen.update()

    # Detect collision with the wall
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce_y()

    # Detect collision with r_paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 330 or ball.distance(l_paddle) < 50 and ball.xcor() < -330:
        ball.bounce_x()

    # Detect if right paddle misses ball
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    # Detect if left paddle misses ball
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()
