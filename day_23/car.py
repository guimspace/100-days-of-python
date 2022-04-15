import random
from turtle import Turtle

import consts


class Car(Turtle):
    def __init__(self, heading, y_init):
        super().__init__()

        self.y_init = y_init

        self.shape("square")
        self.shapesize(stretch_len=1.6)
        self.setheading(heading)
        self.penup()

        self.refresh()

    def refresh(self):
        self.hideturtle()
        self.color(self.random_color())

        if self.heading() == 0:
            self.goto(-consts.X_EDGE, self.y_init)
        else:
            self.goto(consts.X_EDGE, self.y_init)

    def random_color(self):
        r = random.randrange(255)
        g = random.randrange(255)
        b = random.randrange(255)

        return (r, g, b)
