from random import randint

from turtle import Turtle

SCREEN_LIMITS = 600 / 2 - 20


class Food(Turtle):
    def __init__(self):
        super().__init__()

        self.shape("circle")
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color("blue")
        self.speed("fastest")

        self.penup()

    def refresh(self):
        random_x = randint(-SCREEN_LIMITS, SCREEN_LIMITS)
        random_y = randint(-SCREEN_LIMITS, SCREEN_LIMITS)
        self.goto(x=random_x, y=random_y)
