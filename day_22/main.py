import time

from table import Table
from paddle import Paddle
from ball import Ball


def main():
    table = Table()

    player1 = Paddle("left")
    player2 = Paddle("right")
    ball = Ball()

    table.bind_key_press(player1, {"up": "w", "down": "s"})
    table.bind_key_press(player2, {"up": "Up", "down": "Down"})

    game_on = True
    while game_on:
        table.screen.update()
        time.sleep(0.0167)
        ball.move()

    table.screen.exitonclick()


if __name__ == "__main__":
    main()
