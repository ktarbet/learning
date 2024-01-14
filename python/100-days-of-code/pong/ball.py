from turtle import Turtle

NE = 45
SE = 315
NW = 135
SW = 225


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.setheading(NE)

    def bounce_off_wall(self):
        if self.heading() == NE:
            self.setheading(SE)
        elif self.heading() == SE:
            self.setheading(NE)
        elif self.heading() == NW:
            self.setheading(SW)
        elif self.heading() == SW:
            self.setheading(NW)

    def bounce_off_paddle(self):
        if self.heading() == NE:
            self.setheading(NW)
        elif self.heading() == SE:
            self.setheading(SW)
        elif self.heading() == NW:
            self.setheading(NE)
        elif self.heading() == SW:
            self.setheading(SE)

    def move(self):
        self.forward(20)

    def serve(self):
        self.goto(0, 0)
        self.bounce_off_paddle()
