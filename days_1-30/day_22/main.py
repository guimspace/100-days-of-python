import time

from table import Table
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

TABLE_DIMENSIONS = (153, 274)
TABLE_ZOOM = 4
SCREEN_PADDING = 20


def main():
    table = Table()

    player1 = Paddle("left")
    player2 = Paddle("right")
    ball = Ball()
    scoreboard = Scoreboard()

    table.bind_key_press(player1, {"up": "w", "down": "s"})
    table.bind_key_press(player2, {"up": "Up", "down": "Down"})

    height_margin = round(TABLE_ZOOM * TABLE_DIMENSIONS[0] / 2, 0)
    width_margin = round(TABLE_ZOOM * TABLE_DIMENSIONS[1] / 2, 0)

    while scoreboard.is_game_on():
        table.screen.update()
        time.sleep(0.0167)
        ball.move()

        ball_xcor = ball.xcor()
        if ball_xcor > width_margin:
            scoreboard.increment_score(0)
            ball.refresh()
            continue
        elif ball_xcor < -width_margin:
            scoreboard.increment_score(1)
            ball.refresh()
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

    scoreboard.game_over()
    table.screen.exitonclick()


if __name__ == "__main__":
    main()
