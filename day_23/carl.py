from turtle import Turtle

import consts
from road_map import RoadMap


class Carl(Turtle):
    def __init__(self):
        super().__init__()

        self.num_lane = 0

        self.map = RoadMap()
        self.shape("turtle")
        self.color("green")
        self.penup()

        self.x_middle = self.map.get_middle()
        self.y_center = self.map.get_center(0)

        self.finish_line = self.map.get_center(consts.NUM_LANES - 1)

        self.refresh()

    def refresh(self):
        self.goto(self.x_middle, self.y_center)
        self.setheading(90)

    def has_arrived(self):
        return self.ycor() >= self.finish_line

    def move(self, x, y):
        new_x = self.xcor() + x * consts.BLOCK_SIZE
        if new_x > consts.X_EDGE or new_x < -consts.X_EDGE:
            return

        new_y = self.ycor() + y * consts.BLOCK_SIZE
        if new_y > consts.Y_EDGE or new_y < -consts.Y_EDGE:
            return

        self.goto(new_x, new_y)

    def mv_forward(self):
        self.num_lane += 1
        self.setheading(90)
        self.move(0, 1)

    def mv_back(self):
        self.num_lane -= 1
        self.setheading(270)
        self.move(0, -1)

    def mv_right(self):
        self.setheading(0)
        self.move(1, 0)

    def mv_left(self):
        self.setheading(180)
        self.move(-1, 0)
