# W key forwards
# S = backwards
# A = counter clockwise
# D = clockwise
# C = clear

from turtle import Turtle, Screen
tim = Turtle()
screen = Screen()

screen.listen()
screen.onkey(key="w", fun=lambda: tim.forward(10))
screen.onkey(key="s", fun=lambda: tim.forward(-10))
screen.onkey(key="a", fun=lambda: tim.setheading(tim.heading()+5))
screen.onkey(key="d", fun=lambda: tim.setheading(tim.heading()+5))
screen.onkey(key="c", fun=lambda: tim.reset())


screen.exitonclick()