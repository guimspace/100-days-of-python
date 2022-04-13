import time

from table import Table
from paddle import Paddle
from ball import Ball

TABLE_DIMENSIONS = (153, 274)
TABLE_ZOOM = 4
SCREEN_PADDING = 20


def main():
    table = Table()

    player1 = Paddle("left")
    player2 = Paddle("right")
    ball = Ball()

    table.bind_key_press(player1, {"up": "w", "down": "s"})
    table.bind_key_press(player2, {"up": "Up", "down": "Down"})

    height_margin = round(TABLE_ZOOM * TABLE_DIMENSIONS[0] / 2, 0)
    width_margin = round(TABLE_ZOOM * TABLE_DIMENSIONS[1] / 2, 0)

    game_on = True
    while game_on:
        table.screen.update()
        time.sleep(0.0167)
        ball.move()

        ball_xcor = ball.xcor()
        if ball_xcor > width_margin or ball_xcor < -width_margin:
            game_on = False
            continue

        ball_ycor = ball.ycor()
        if ball_ycor > height_margin:
            ball.reflect_direction(270)
        elif ball_ycor < -height_margin:
            ball.reflect_direction(90)

        if player1.distance(ball) < 50 and ball_xcor - 40 <= -width_margin:
            ball.reflect_direction(0)
        if player2.distance(ball) < 50 and ball_xcor + 40 >= width_margin:
            ball.reflect_direction(180)

    table.screen.exitonclick()


if __name__ == "__main__":
    main()
