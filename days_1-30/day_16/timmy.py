from turtle import Turtle, Screen


def main():
    timmy = Turtle()
    timmy.shape("turtle")

    timmy.forward(100)
    timmy.right(40)
    timmy.forward(100)

    Screen().exitonclick()


if __name__ == "__main__":
    main()
