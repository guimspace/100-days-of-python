from turtle import Turtle

STEP_DISTANCE = 20


class Snake:
    def __init__(self):
        self.segments = []
        for i in range(3):
            self.add_segment((-STEP_DISTANCE * (1 + i), 0), 0)

        self.head = self.segments[0]["seg"]

    def add_segment(self, pos, angle):
        seg = Turtle(shape="square")
        seg.color("white")
        seg.penup()

        seg.goto(pos)
        seg.setheading(angle)
        seg.backward(STEP_DISTANCE)

        self.segments.append({"seg": seg, "mv": "forward"})

    def grow(self):
        seg = self.segments[-1]["seg"]
        self.add_segment(seg.pos(), seg.heading())

    def up(self):
        heading = self.segments[0]["seg"].heading()
        if heading == 90 or heading == 270:
            return
        elif heading == 0:
            self.segments[0]["mv"] = "left"
        else:
            self.segments[0]["mv"] = "right"

    def down(self):
        heading = self.segments[0]["seg"].heading()
        if heading == 90 or heading == 270:
            return
        elif heading == 0:
            self.segments[0]["mv"] = "right"
        else:
            self.segments[0]["mv"] = "left"

    def left(self):
        heading = self.segments[0]["seg"].heading()
        if heading == 0 or heading == 180:
            return
        elif heading == 90:
            self.segments[0]["mv"] = "left"
        else:
            self.segments[0]["mv"] = "right"

    def right(self):
        heading = self.segments[0]["seg"].heading()
        if heading == 0 or heading == 180:
            return
        elif heading == 90:
            self.segments[0]["mv"] = "right"
        else:
            self.segments[0]["mv"] = "left"

    def turn(self, seg):
        if seg["mv"] == "right":
            seg["seg"].right(90)
        elif seg["mv"] == "left":
            seg["seg"].left(90)

    def move(self):
        self.turn(self.segments[0])
        self.segments[0]["seg"].forward(STEP_DISTANCE)

        for i in range(len(self.segments) - 1, 0, -1):
            self.turn(self.segments[i])
            self.segments[i]["seg"].forward(STEP_DISTANCE)
            self.segments[i]["mv"] = self.segments[i - 1]["mv"]

        self.segments[0]["mv"] = "forward"
