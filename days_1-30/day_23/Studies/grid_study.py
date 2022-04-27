from turtle import Turtle, Screen


def main():
    dimension = 500
    edge = int(dimension / 2)

    screen = Screen()
    screen.setup(width=dimension, height=dimension)
    screen.bgcolor("black")
    screen.tracer(2)

    tim = Turtle()
    tim.color("white")
    tim.hideturtle()
    tim.setheading(90)
    tim.speed("fastest")

    tim.penup()
    tim.goto(-edge, -edge)
    tim.pendown()
    tim.setheading(0)
    for _ in range(4):
        tim.forward(dimension)
        tim.left(90)

    tim.setheading(90)
    x = -edge + 50
    while x < edge:
        tim.penup()
        tim.goto(x, -edge)
        x += 50

        while tim.ycor() < edge:
            tim.pendown()
            tim.forward(10)
            tim.penup()
            tim.forward(10)

    tim.setheading(0)
    y = -edge + 50
    while y < edge:
        tim.penup()
        tim.goto(-edge, y)
        y += 50

        while tim.xcor() < edge:
            tim.pendown()
            tim.forward(10)
            tim.penup()
            tim.forward(10)

    tim.goto(0, 0)
    tim.shape("square")
    tim.showturtle()
    tim.shapesize(stretch_wid=5, stretch_len=5)

    screen.update()
    screen.exitonclick()


if __name__ == "__main__":
    main()
