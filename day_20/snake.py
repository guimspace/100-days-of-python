from turtle import Turtle

STEP_DISTANCE = 20


class Snake:
    def __init__(self):
        segments = []
        for i in range(3):
            seg = Turtle(shape="square")
            seg.color("white")
            seg.penup()
            seg.speed("fastest")

            seg.goto(-STEP_DISTANCE * i, 0)

            segments.append({
                "seg": seg,
                "mv": "forward"
            })

        self.segments = segments

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
