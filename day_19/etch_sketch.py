from turtle import Turtle, Screen


def main():
    def mv_fd():
        tim.forward(10)

    def mv_rt():
        tim.right(10)

    def mv_lt():
        tim.left(10)

    def mv_bk():
        tim.backward(10)

    def sc_clear():
        tim.clear()

    tim = Turtle()

    screen = Screen()
    screen.listen()

    screen.onkey(mv_fd, "w")
    screen.onkey(mv_lt, "a")
    screen.onkey(mv_rt, "d")
    screen.onkey(mv_bk, "s")
    screen.onkey(sc_clear, "c")

    screen.exitonclick()


if __name__ == "__main__":
    main()
