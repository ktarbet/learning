from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

MAX_HEIGHT = 280
OUT_OF_BOUNDS = 320


def hit_wall(b: Ball):
    return b.ycor() >= MAX_HEIGHT or b.ycor() <= -MAX_HEIGHT


def hit_paddle(b: Ball, paddle: Paddle):
    return b.distance(paddle) < 50 and abs(b.xcor()) > OUT_OF_BOUNDS


def out_of_bounds(b: Ball):
    return abs(b.xcor()) >= OUT_OF_BOUNDS


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)
left_paddle = Paddle(-350, screen, "w", "s")
right_paddle = Paddle(350, screen, "Up", "Down")
ball = Ball()
scoreboard = Scoreboard()
screen.listen()
sleep_seconds = 0.15
playing = True
while playing:
    screen.update()
    time.sleep(sleep_seconds)
    print(ball.heading().real)

    ball.move()
    if hit_wall(ball):
        ball.bounce_off_wall()
    elif hit_paddle(ball, left_paddle):
        sleep_seconds -= 0.02
        ball.bounce_off_paddle()
        print("left paddle")
    elif hit_paddle(ball, right_paddle):
        sleep_seconds -= 0.02
        ball.bounce_off_paddle()
        print("right paddle")
    elif out_of_bounds(ball):
        print("out of bounds.")
        if ball.xcor() > 0:
            scoreboard.left_score += 1
        else:
            scoreboard.right_score += 1
        scoreboard.update_score()
        sleep_seconds = 0.15
        ball.serve()

screen.exitonclick()
