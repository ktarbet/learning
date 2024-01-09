import turtle
from turtle import Turtle, Screen
import random

t = Turtle()

t.shape("turtle")

t.color("red")


def draw_square(size):
    for i in range(0, 4):
        t.forward(size)
        t.right(90)

def get_rand_color():
    r = random.randint(1, 200)
    g = random.randint(1, 200)
    b = random.randint(1, 200)
    return (r,g,b)


draw_square(100)

# make dashed line.
t.forward(100)
for _ in range(10):
    t.forward(5)
    t.penup()
    t.forward(5)
    t.pendown()

# draw n-sided shapes with different colors
t.clear()
t.reset()
turtle.colormode(255)

for n in range(4, 8):


    t.pencolor(get_rand_color())
    angle = 360 / n
    distance = 100
    for _ in range(n):
        t.forward(distance)
        t.right(angle)


t.clear()
t.reset()
# random walk
turtle.speed(9)
angles =[0,90,180,270]
t.pensize(5)
for _ in range(100):
    angle = random.choice(angles)
    print(angle)
    t.pencolor(get_rand_color())
    t.right(angle)
    t.forward(20)

screen = Screen()
screen.exitonclick()
