from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        self.cars = []
        self.distance = STARTING_MOVE_DISTANCE

    def create_car(self):
        car = self.get_recycled_car()
        if car is None:
            car = Turtle("square")
            car.recycled = False

        if not car.recycled:
            car.shapesize(stretch_wid=1, stretch_len=2)
            self.cars.append(car)
        color = random.choice(COLORS)
        car.color(color)
        car.setheading(180)
        car.penup()
        car.goto(300, random.randint(-250, 250))

    def __cleanup(self):
        """
        remove cars that made it across
        """


    def move_cars(self):
        for car in self.cars:
            car.forward(self.distance)

    def turtle_hit_by_car(self, player):
        for car in self.cars:
            if car.distance(player) < 20:
                return True

        return False

    def increase_speed(self):
        self.distance += MOVE_INCREMENT

    def get_recycled_car(self):
        for car in self.cars:
            if car.xcor() < -300:
                print("recycling this car, may need to re-paint and purchase new wheels")
                car.recycled = True
                return car

        return None

