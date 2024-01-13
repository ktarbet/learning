from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.score = 0
        self.hideturtle()

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER", align='center', font=("Courier", 12, "normal"))

    def update(self):
        self.clear()
        self.penup()
        self.goto(-30, 280)
        self.pendown()
        self.write(f"Score = {self.score}", align='center', font=("Courier", 12, "normal"))
