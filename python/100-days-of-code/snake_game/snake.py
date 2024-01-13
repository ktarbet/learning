
from turtle import Screen, Turtle

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
class Snake:

    def __init__(self):
        self.snake_body = []
        x = 0
        for i in range(0, 3):
            self.__add_segment(i)
        self.head = self.snake_body[0]

    def __add_segment(self, i):
        t = Turtle("square")
        t.color("white")
        t.penup()
        t.goto(-20 * i, 0)
        self.snake_body.append(t)

    def feed(self):
        self.__add_segment(len(self.snake_body))

    def move(self):
        for i in range(len(self.snake_body) - 1, 0, -1):
            new_x = self.snake_body[i - 1].xcor()
            new_y = self.snake_body[i - 1].ycor()
            self.snake_body[i].goto(new_x, new_y)
        self.snake_body[0].forward(20)


    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def eating_tail(self):
        for segment in self.snake_body[1:]:
            if self.head.distance(segment) < 10:
                return True

        return False

