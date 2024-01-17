from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.score = 0
        self.highscore = self.__read_high_score()
        self.hideturtle()

    def __read_high_score(self):
        with open("data.txt", "r") as f:
            return int(f.read())

    def write_high_score(self):
        with open("data.txt", "w") as f:
            f.write(str(self.highscore))


    def reset(self):
        self.highscore = max(self.highscore, self.score)
        self.write_high_score()
        self.score = 0

    def update(self):
        self.clear()
        self.penup()
        self.goto(-30, 280)
        self.pendown()
        self.write(f"Score = {self.score}  High Score: {self.highscore}", align='center',
                   font=("Courier", 12, "normal"))
