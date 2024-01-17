from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game!")
screen.tracer(0)

snake = Snake()
food = Food()
score_board = ScoreBoard()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_over = False
while not game_over:
    screen.update()
    score_board.update()
    time.sleep(0.2)
    snake.move()

    # did we find food?
    if snake.head.distance(food) < 15:
        print("found it..")
        score_board.score += 1
        snake.feed()
        food.refresh()

    # did we hit the wall
    x = snake.head.xcor()
    y = snake.head.ycor()
    if x < -280 or x > 280 or y > 280 or y < -280:
        score_board.reset()
        snake.reset()

    # did snake hit itself?
    if snake.eating_tail():
        score_board.reset()
        snake.reset()

screen.exitonclick()
