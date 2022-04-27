import random
import turtle


def square():
    tim = turtle.Turtle()
    for _ in range(4):
        tim.forward(100)
        tim.right(90)


def dashed_line():
    tim = turtle.Turtle()
    for _ in range(10):
        tim.forward(14)
        tim.penup()
        tim.forward(14)
        tim.pendown()


def draw_polygons():
    tim = turtle.Turtle()
    for n in range(3, 11):
        angle = 360 / n
        for _ in range(n):
            tim.forward(100)
            tim.right(angle)


def random_color():
    r = random.randrange(255)
    g = random.randrange(255)
    b = random.randrange(255)
    return (r, g, b)


def random_walk():
    tim = turtle.Turtle()
    tim.pensize(10)
    tim.speed("fast")
    turtle.colormode(255)

    for _ in range(20):
        color = random_color()
        tim.pencolor(color)

        distance = random.randrange(40)
        tim.forward(distance)

        angle = random.randrange(-360, 360)
        tim.right(angle)


def draw_spirograph():
    tim = turtle.Turtle()
    tim.speed("fastest")
    turtle.colormode(255)

    num_circles = 60
    step = 360 / num_circles
    for _ in range(num_circles):
        color = random_color()
        tim.pencolor(color)

        tim.circle(100)

        tim.left(step)


def main():
    random_walk()
    turtle.Screen().exitonclick()


if __name__ == "__main__":
    main()
