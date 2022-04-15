from turtle import Turtle
from road_map import RoadMap

BLOCK_SIZE = 50
NUM_LANES = 2 + 10
ROAD_LEN = 14 * BLOCK_SIZE


class Carl(Turtle):
    def __init__(self):
        super().__init__()

        self.map = RoadMap(NUM_LANES, BLOCK_SIZE, ROAD_LEN)
        self.shape("turtle")
        self.color("green")
        self.penup()

        self.x_edge = ROAD_LEN / 2
        self.y_edge = NUM_LANES * BLOCK_SIZE / 2

        self.x_middle = self.map.get_middle()
        self.y_center = self.map.get_center(0)

        self.finish_line = self.map.get_center(NUM_LANES - 1)

        self.refresh()

    def refresh(self):
        self.goto(self.x_middle, self.y_center)
        self.setheading(90)

    def has_arrived(self):
        return self.ycor() >= self.finish_line

    def move(self, x, y):
        new_x = self.xcor() + x * BLOCK_SIZE
        if new_x > self.x_edge or new_x < -self.x_edge:
            return

        new_y = self.ycor() + y * BLOCK_SIZE
        if new_y > self.y_edge or new_y < -self.y_edge:
            return

        self.goto(new_x, new_y)

    def mv_forward(self):
        self.setheading(90)
        self.move(0, 1)

    def mv_back(self):
        self.setheading(270)
        self.move(0, -1)

    def mv_right(self):
        self.setheading(0)
        self.move(1, 0)

    def mv_left(self):
        self.setheading(180)
        self.move(-1, 0)
