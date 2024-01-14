from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, xpos: int, screen, upkey: str, downkey: str):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(xpos, 0)
        self.pendown()
        screen.onkey(self.up, upkey)
        screen.onkey(self.down, downkey)

    def up(self):
        self.penup()
        self.goto(self.xcor(), self.ycor() + 20)
        self.pendown()

    def down(self):
        self.penup()
        self.goto(self.xcor(), self.ycor() - 20)
        self.pendown()
