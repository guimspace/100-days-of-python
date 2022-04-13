from turtle import Turtle

TABLE_DIMENSIONS = (153, 274)
TABLE_ZOOM = 4
SCREEN_PADDING = 20

MV_DISTANCE = 3 * TABLE_ZOOM


class Paddle(Turtle):
    def __init__(self, side):
        super().__init__()

        width_margin = round(TABLE_ZOOM * TABLE_DIMENSIONS[1] / 2, 0) - SCREEN_PADDING
        self.height_margin = round(TABLE_ZOOM * TABLE_DIMENSIONS[0] / 2, 0)

        side = 1 if side == "right" else -1

        self.color("white")
        self.speed("fastest")
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto((side * width_margin, 0))

    def key_up(self):
        self.move(1)

    def key_down(self):
        self.move(-1)

    def move(self, heading):
        new_y = self.ycor() + heading * MV_DISTANCE
        if new_y > self.height_margin or new_y < -self.height_margin:
            return
        self.goto(self.xcor(), new_y)
