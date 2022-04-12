import time
from turtle import Turtle, Screen


def main():
    screen = Screen()
    screen.setup(height=600, width=600)
    screen.bgcolor("black")

    screen.tracer(n=0)

    segments = []
    for i in range(3):
        seg = Turtle(shape="square")
        seg.color("white")

        seg.penup()
        seg.goto(-20 * i, 0)

        segments.append(seg)

    while True:
        screen.update()
        time.sleep(0.2)

        for seg in segments:
            seg.forward(10)

    screen.exitonclick()


if __name__ == "__main__":
    main()
