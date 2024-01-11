from turtle import Turtle, Screen
import random

tim = Turtle()
screen = Screen()
screen.setup(width=500, height=400)

user_guess = screen.textinput("Make you guess", "What color will Win? (red,green,)")

red = Turtle(shape="turtle")
green = Turtle(shape="turtle")
blue = Turtle(shape="turtle")
orange = Turtle(shape="turtle")

turtles = {"red": red, "green": green, "blue": blue, "orange": orange}
x = -200
y = -188
for c in turtles:
    t = turtles[c]
    t.color(c)
    y += 50
    t.penup()
    t.goto(x, y)

# RACE
max_x = -200
while max_x < 230:
    for c in turtles:
        t = turtles[c]
        if t.xcor() > 230:
            max_x = t.xcor()
            winner_color = t.pencolor()
            if winner_color == user_guess:
                print(f"You win! {winner_color} is the winner!")
            else:
                print(f"Sorry {winner_color} is the winner!")
            break
        t.penup()
        xinc = random.randint(0,10)
        t.forward(xinc)

screen.exitonclick()
