from turtle import Turtle, Screen

import consts
from road_map import RoadMap


class Road:
    def __init__(self):
        self.map = RoadMap()

        screen = Screen()
        screen.setup(width=consts.ROAD_LENGTH,
                     height=consts.NUM_LANES * consts.BLOCK_SIZE)
        screen.bgcolor("gray")
        screen.listen()
        screen.tracer(2)
        self.screen = screen

        self.tim = Turtle()
        self.tim.speed("fastest")

        self.draw_lanes()
        self.draw_sidewalk(True)
        self.draw_sidewalk(False)

        self.screen.tracer(0)
        del self.tim

    def bind_keys(self, carl):
        self.screen.onkey(carl.mv_forward, "Up")
        self.screen.onkey(carl.mv_back, "Down")
        self.screen.onkey(carl.mv_right, "Right")
        self.screen.onkey(carl.mv_left, "Left")

    def draw_lanes(self):
        self.tim.color("white")
        self.tim.hideturtle()
        self.tim.pensize(2)

        for i in range(1, consts.NUM_LANES - 2, 1):
            self.tim.penup()
            self.tim.goto(-consts.X_EDGE, self.map.get_lane(i))

            while self.tim.xcor() < consts.X_EDGE:
                self.tim.pendown()
                self.tim.forward(40)
                self.tim.penup()
                self.tim.forward(40)

    def draw_sidewalk(self, side):
        self.tim.penup()
        self.tim.pensize(2)

        y = self.map.get_lane(0 if side else consts.NUM_LANES - 2)
        self.tim.goto(-consts.X_EDGE, y)

        self.tim.pendown()
        self.tim.forward(consts.ROAD_LENGTH)

        self.tim.penup()
        self.tim.pensize(40)

        y = self.map.get_center(0 if side else consts.NUM_LANES - 1)
        self.tim.goto(-consts.X_EDGE, y)

        self.tim.pendown()
        self.tim.forward(consts.ROAD_LENGTH)

    def exitonclick(self):
        self.screen.exitonclick()
