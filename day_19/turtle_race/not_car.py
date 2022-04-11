from random import randrange
from turtle import Turtle


class NotCar:
    def __init__(self, pos, color=None):
        car = Turtle()

        car.penup()
        car.shape("turtle")
        car.speed("fast")

        if color is None:
            r = randrange(255)
            g = randrange(255)
            b = randrange(255)
            color = (r, g, b)

        car.color(color)

        self.car = car
        self.pos = pos - 1

    def goto(self, x, y):
        self.car.goto(x, y)
