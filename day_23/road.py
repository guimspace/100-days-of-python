from turtle import Turtle, Screen
from road_map import RoadMap

BLOCK_SIZE = 50
NUM_LANES = 2 + 10
ROAD_LEN = 14 * BLOCK_SIZE


class Road:
    def __init__(self):
        self.x_edge = ROAD_LEN / 2
        self.map = RoadMap(NUM_LANES, BLOCK_SIZE)

        screen = Screen()
        screen.setup(width=ROAD_LEN, height=NUM_LANES * BLOCK_SIZE)
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
        del self.x_edge

    def bind_keys(self, carl):
        self.screen.onkey(carl.mv_forward, "Up")
        self.screen.onkey(carl.mv_back, "Down")
        self.screen.onkey(carl.mv_right, "Right")
        self.screen.onkey(carl.mv_left, "Left")

    def draw_lanes(self):
        self.tim.color("white")
        self.tim.hideturtle()
        self.tim.pensize(2)

        for i in range(1, NUM_LANES - 2, 1):
            self.tim.penup()
            self.tim.goto(-self.x_edge, self.map.get_lane(i))

            while self.tim.xcor() < self.x_edge:
                self.tim.pendown()
                self.tim.forward(40)
                self.tim.penup()
                self.tim.forward(40)

    def draw_sidewalk(self, side):
        self.tim.penup()
        self.tim.pensize(2)
        self.tim.goto(-self.x_edge, self.map.get_lane(0 if side else NUM_LANES - 2))
        self.tim.pendown()
        self.tim.forward(ROAD_LEN)

        self.tim.penup()
        self.tim.pensize(40)
        self.tim.goto(-self.x_edge, self.map.get_center(0 if side else NUM_LANES - 1))
        self.tim.pendown()
        self.tim.forward(ROAD_LEN)

    def exitonclick(self):
        self.screen.exitonclick()
