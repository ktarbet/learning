from turtle import Turtle

FONT = ("Courier", 24, "normal")


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("Black")
        self.score = 0
        self.hideturtle()
        self.level = 1

    def game_over(self):
        self.goto(0, 0)
        self.pendown()
        self.write(f"GAME OVER", align='center', font=FONT)

    def increase_level(self):
        self.level += 1

    def update(self):
        self.clear()
        self.penup()
        self.goto(-200, 260)
        self.pendown()
        self.write(f"Level = {self.level}", align='center', font=FONT)

