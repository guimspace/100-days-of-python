from turtle import Turtle, Screen

TABLE_DIMENSIONS = (153, 274)
TABLE_ZOOM = 4
SCREEN_PADDING = 20


class Table:
    def __init__(self):
        self.height_margin = round(TABLE_ZOOM * TABLE_DIMENSIONS[0] / 2, 0)
        self.width_margin = round(TABLE_ZOOM * TABLE_DIMENSIONS[1] / 2, 0)

        screen = Screen()
        screen.setup(height=TABLE_ZOOM * TABLE_DIMENSIONS[0] + 2 * SCREEN_PADDING,
                     width=TABLE_ZOOM * TABLE_DIMENSIONS[1] + 2 * SCREEN_PADDING)
        screen.bgcolor("black")

        screen.listen()
        screen.tracer(n=0)

        tim = Turtle()
        tim.penup()
        tim.goto(0, -self.height_margin)
        tim.setheading(90)
        tim.hideturtle()
        tim.color("white")
        tim.pensize(TABLE_ZOOM)

        while tim.ycor() < self.height_margin - 5 * TABLE_ZOOM:
            tim.forward(5 * TABLE_ZOOM)
            tim.pendown()
            tim.forward(5 * TABLE_ZOOM)
            tim.penup()

        self.screen = screen

    def exitonclick(self):
        self.screen.exitonclick()

    def bind_key_press(self, player, keys):
        self.screen.onkey(player.key_up, keys["up"])
        self.screen.onkey(player.key_down, keys["down"])
