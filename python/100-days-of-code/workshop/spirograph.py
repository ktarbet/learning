import turtle
from turtle import Turtle, Screen
import random

def get_rand_color():
    r = random.randint(1, 200)
    g = random.randint(1, 200)
    b = random.randint(1, 200)
    return (r,g,b)

def draw_spirograph(t,angle):
    delta = int(360/angle)
    for _ in range(delta):
        t.color(get_rand_color())
        t.circle(100)
        t.setheading(t.heading()+angle)


turtle.colormode(255)
t = Turtle()
t.speed("fastest")
draw_spirograph(t,5)

screen = Screen()
screen.exitonclick()