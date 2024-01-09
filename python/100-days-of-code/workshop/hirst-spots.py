# import colorgram
#
# colors = colorgram.extract('spots.jpg',20)
# rgbList =[]
# for cg in colors:
#     a = cg.rgb
#     rgbList.append((a.r,a.g,a.b))

rgbList = [ (234, 225, 85), (200, 6, 70), (198, 164, 11), (232, 53, 130), (205, 75, 13), (218, 161, 104), (110, 179, 215), (27, 106, 171), (33, 188, 110), (212, 136, 175), (233, 224, 6), (14, 24, 64), (19, 29, 169), (202, 31, 130), (12, 184, 212), (230, 167, 197)]

#print(colors)
print(rgbList)

# 10 x 10 spots drawing like Hirst
import turtle
from turtle import Turtle, Screen
import random

t = Turtle()

t.shape("triangle")
t.color("black")

print(t.pos())
turtle.setworldcoordinates(0,0,200,200)
turtle.colormode(255)

t.hideturtle()

for r in range(0,10):
    for c in range(0,10):
        t.penup()
        t.goto(50+c*10,r*10+50)
        t.dot(20,random.choice(rgbList))
        turtle.pendown()


print(t.pos())



screen = Screen()
screen.exitonclick()
