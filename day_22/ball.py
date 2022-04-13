from random import randrange
from turtle import Turtle

TABLE_WIDTH = 274
TABLE_ZOOM = 4

FPS = 60


class Ball(Turtle):
    def __init__(self):
        super().__init__()

        self.shape("circle")
        self.color("white")
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.penup()

        self.refresh()

        self.step = round(TABLE_ZOOM * TABLE_WIDTH / 2 * (1 / FPS), 2)

    def refresh(self):
        self.goto(0, 0)
        heading = randrange(2) * 180 + randrange(-30, 30)
        self.setheading(heading)

    def move(self):
        self.forward(self.step)
