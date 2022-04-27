from random import randrange
from turtle import Turtle

TABLE_WIDTH = 274
TABLE_ZOOM = 4

TIME_TO_TARGET = 4
FPS = 60


class Ball(Turtle):
    def __init__(self):
        super().__init__()

        self.shape("circle")
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.penup()

        self.refresh()

        self.step = round(TABLE_ZOOM * TABLE_WIDTH / TIME_TO_TARGET * (1 / FPS), 2)

    def reflect_direction(self, direction):
        new_heading = 90 + self.heading()
        self.setheading(new_heading)

    def refresh(self):
        self.goto(0, 0)
        heading = randrange(2) * 180 + randrange(-30, 30)
        self.setheading(heading)

    def move(self):
        self.forward(self.step)
