import random
import turtle


def random_color():
    r = random.randrange(255)
    g = random.randrange(255)
    b = random.randrange(255)
    return (r, g, b)


def main():
    turtle.colormode(255)

    tim = turtle.Turtle()
    tim.speed("fastest")
    tim.penup()

    step = 30

    x = 0
    y = 0
    d = 1
    while x < 10:
        if y == 10:
            y = 0
            x += 1

            tim.backward(step)
            tim.left(d * 90)
            tim.forward(step)
            tim.left(d * 90)

            d *= -1
            continue

        color = random_color()
        tim.pencolor(color)
        tim.dot(16)

        tim.forward(step)
        y += 1

    turtle.Screen().exitonclick()


if __name__ == "__main__":
    main()
